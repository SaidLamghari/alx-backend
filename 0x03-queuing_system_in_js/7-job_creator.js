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

// Définir les données des jobs à ajouter dans la queue
// Chaque élément de ce tableau représente un
// job avec un numéro de téléphone et un message
const jobs = [
  { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
  { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153518743', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153538781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153118782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153718781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4159518782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4158718781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153818782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4154318781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4151218782', message: 'This is the code 4321 to verify your account' }
];

// Fonction pour créer des jobs dans la queue
// Prend en paramètre un numéro de téléphone et un message
function createJob(phoneNumber, message) {
  // Crée un job dans la queue avec le type 'push_notification_code_2'
  // Le job utilise les données fournies
  // (numéro de téléphone et message)
  const job = queue.create('push_notification_code_2', {
    phoneNumber,
    message
  }).save((err) => {
    // Si aucune erreur n'est survenue lors de la création
    // du job, affiche un message de confirmation
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      // Affiche un message d'erreur si la création du job échoue
      console.error(`Error creating job: ${err.message}`);
    }
  });

  // Écoute l'événement 'complete', qui est déclenché
  // lorsque le job est terminé avec succès
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  // Écoute l'événement 'failed', qui est déclenché si le job échoue
  job.on('failed', (err) => {
    console.log(`Notification job ${job.id} failed: ${err}`);
  });

  // Écoute l'événement 'progress', qui est
  // déclenché pour indiquer la progression du job
  // Affiche la progression en pourcentage dans la console
  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
}

// Boucle pour créer des jobs
// Pour chaque élément du tableau 'jobs', appelle
// la fonction 'createJob' avec les données du job
jobs.forEach(jobData => {
  createJob(jobData.phoneNumber, jobData.message);
});
