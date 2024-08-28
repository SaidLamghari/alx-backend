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

// Fonction pour envoyer une notification
// Cette fonction est une simulation d'envoi de notification,
// elle affiche simplement les détails dans la console
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Traitement des jobs dans la queue 'push_notification_code'
// Cette fonction est appelée pour chaque job
// dans la queue avec le type 'push_notification_code'
queue.process('push_notification_code', (job, done) => {
  // Extraire les données du job (numéro de téléphone et message)
  const { phoneNumber, message } = job.data;
  
  // Appelle la fonction pour envoyer la
  // notification avec les données extraites
  sendNotification(phoneNumber, message);
  
  // Indique que le traitement du job est terminé
  done();
});
