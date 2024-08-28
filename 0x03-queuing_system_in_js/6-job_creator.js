// Auteur SAID LAMGHARI
import kue from 'kue';
import redis from 'redis';

// Crée une connexion au serveur Redis
const redisClient = redis.createClient();

// Crée une instance de la queue Kue,
// en spécifiant le client Redis à utiliser
const queue = kue.createQueue({
  redis: redisClient
});

// Crée un objet contenant les données
// du job à ajouter dans la queue
const jobData = {
  phoneNumber: '123-456-7890',
  message: 'Hello, this is a test notification!'
};

// Crée un job dans la queue nommée 'push_notification_code'
// Le job utilise les données définies dans 'jobData'
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      // Affiche un message d'erreur si la création du job échoue
      console.error(`Error creating job: ${err.message}`);
    } else {
      // Affiche un message de confirmation
      // lorsque le job est créé avec succès
      console.log(`Notification job created: ${job.id}`);
    }
  });

// Écoute l'événement 'complete', qui est
// déclenché lorsque le job est terminé avec succès
job.on('complete', () => {
  // Affiche un message indiquant que le job a été complété
  console.log('Notification job completed');
});

// Écoute l'événement 'failed', qui
// est déclenché si le job échoue
job.on('failed', (errorMessage) => {
  // Affiche un message indiquant que
  // le job a échoué, avec le message d'erreur
  console.log(`Notification job failed: ${errorMessage}`);
});
