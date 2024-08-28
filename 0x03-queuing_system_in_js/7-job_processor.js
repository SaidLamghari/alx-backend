// Auteur SAID LAMGHARI
import kue from 'kue';
import redis from 'redis';

// Crée une connexion au serveur Redis
const redisClient = redis.createClient();

// Crée une instance de la queue Kue en
// spécifiant le client Redis à utiliser
const queue = kue.createQueue({
  redis: redisClient
});

// Définir les numéros de téléphone blacklistés
// Ces numéros ne doivent pas recevoir de notifications
const blacklistedNumbers = [
  '4153518780',
  '4153518781'
];

// Fonction pour envoyer une notification
// Cette fonction simule l'envoi d'une notification et
// gère les erreurs liées aux numéros blacklistés
function sendNotification(phoneNumber, message, job, done) {
  // Met à jour la progression du job à 0%
  job.progress(0, 100);

  // Vérifie si le numéro de téléphone est blacklisté
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Marque le job comme échoué et passe une
    // erreur indiquant que le numéro est blacklisté
    job.fail(new Error(`Phone number ${phoneNumber} is blacklisted`));
    // Indique que le job est terminé avec une erreur
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Met à jour la progression du job à 50%
  job.progress(50, 100);
  // Affiche un message simulant l'envoi de la notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  // Indique que le job est terminé avec succès
  done();
}

// Crée et configure la queue Kue pour traiter les jobs
// Le nombre maximum de jobs traités simultanément est fixé à 2
queue.process('push_notification_code_2', 2, (job, done) => {
  // Extrait les données du job (numéro de téléphone et message)
  const { phoneNumber, message } = job.data;
  // Appelle la fonction pour envoyer
  // la notification en passant les données du job
  sendNotification(phoneNumber, message, job, done);
});

// Affiche un message indiquant que le serveur
// de traitement de jobs est en cours d'exécution
console.log('Job processor is running...');
