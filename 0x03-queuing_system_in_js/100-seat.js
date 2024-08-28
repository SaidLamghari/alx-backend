// Auteur SAID LAMGHARI
const express = require('express');
const redis = require('redis');
const kue = require('kue');
const { promisify } = require('util');

// Créez une instance de l'application Express
const app = express();
const port = 1245;

// Initialisez le client Redis et la queue Kue
const client = redis.createClient();
const queue = kue.createQueue();

// Promisify les méthodes Redis pour
// pouvoir les utiliser avec des promesses
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Définissez le nombre initial de sièges
// disponibles et un drapeau pour les réservations
const INITIAL_SEATS = 50;
let reservationEnabled = true;

// Fonction pour initialiser le nombre de
// sièges disponibles dans Redis
async function initializeSeats() {
  await setAsync('available_seats', INITIAL_SEATS);
}

// Initialisez les sièges disponibles
// au démarrage de l'application
initializeSeats();

// Fonction pour réserver un siège en mettant
// à jour le nombre de sièges disponibles
async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

// Fonction pour obtenir le nombre
// actuel de sièges disponibles
async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return seats ? parseInt(seats, 10) : 0;
}

// Route pour obtenir le nombre de sièges disponibles
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  // Répond avec le nombre de
  // sièges disponibles sous forme de JSON
  res.json({ numberOfAvailableSeats: availableSeats.toString() });
});

// Route pour réserver un siège
app.get('/reserve_seat', (req, res) => {
  // Vérifie si les réservations sont autorisées
  if (!reservationEnabled) {
    return res.json({ status: 'Reservations are blocked' });
  }

  // Crée un job dans la queue Kue pour réserver un siège
  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    // Répond que la réservation est en cours de traitement
    res.json({ status: 'Reservation in process' });
  });

  // Écoute les événements de la queue pour
  // savoir si le job a réussi ou échoué
  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  }).on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err}`);
  });
});

// Route pour traiter les jobs dans la queue Kue
app.get('/process', async (req, res) => {
  // Répond que le traitement de la queue a commencé
  res.json({ status: 'Queue processing' });

  // Configure le traitement des jobs 'reserve_seat' dans la queue Kue
  queue.process('reserve_seat', async (job, done) => {
    try {
      // Obtient le nombre actuel de sièges disponibles
      const availableSeats = await getCurrentAvailableSeats();

      // Vérifie si le nombre de sièges disponibles est suffisant
      if (availableSeats <= 0) {
        reservationEnabled = false; // Désactive les réservations si plus de sièges disponibles
        return done(new Error('Not enough seats available'));
      }

      // Réserve un siège en mettant à jour
      // le nombre de sièges disponibles
      await reserveSeat(availableSeats - 1);
      done(); // Signale que le job est terminé avec succès
    } catch (error) {
      done(error); // Signale une erreur si quelque chose a échoué
    }
  });
});

// Démarre le serveur sur le port défini
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
