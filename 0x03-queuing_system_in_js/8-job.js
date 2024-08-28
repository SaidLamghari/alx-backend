// Auteur SAID LAMGHARI
import kue from 'kue';

/**
 * Fonction pour créer des jobs de notification push dans une queue
 * @param {Array} jobs - Tableau d'objets représentant les données des jobs
 * @param {Object} queue - Objet de la queue Kue utilisé pour créer les jobs
 */
function createPushNotificationsJobs(jobs, queue) {
  // Vérifie si 'jobs' est bien un tableau
  if (!Array.isArray(jobs)) {
    // Lève une erreur si 'jobs' n'est pas un tableau
    throw new Error('Jobs is not an array');
  }

  // Parcourt chaque élément du tableau 'jobs'
  jobs.forEach(jobData => {
    // Crée un job dans la queue avec le type 'push_notification_code_3'
    // 'jobData' contient les données du job
    // (par exemple, numéro de téléphone et message)
    const job = queue.create('push_notification_code_3', jobData)
      // Écoute l'événement 'enqueue', déclenché
      // lorsque le job est ajouté à la queue
      .on('enqueue', () => {
        console.log(`Notification job created: ${job.id}`);
      })
      // Écoute l'événement 'complete', déclenché
      // lorsque le job est terminé avec succès
      .on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      })
      // Écoute l'événement 'failed', déclenché si le job échoue
      .on('failed', (errorMessage) => {
        console.log(`Notification job ${job.id} failed: ${errorMessage}`);
      })
      // Écoute l'événement 'progress',
      // déclenché pour indiquer la progression du job
      .on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      })
      // Sauvegarde le job dans la queue
      .save();
  });
}

// Exporte la fonction pour l'utiliser dans d'autres modules
export default createPushNotificationsJobs;
