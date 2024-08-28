// Auteur SAID LAMGHARI
import kue from 'kue';
import chai from 'chai';
import spies from 'chai-spies';
import createPushNotificationsJobs from './8-job.js';

// Configure Chai pour utiliser les spies (espions)
// pour surveiller les appels de fonction
chai.use(spies);
const { expect } = chai;

describe('createPushNotificationsJobs', function() {
  let queue;

  beforeEach(function() {
    // Avant chaque test, crée une nouvelle instance de queue Kue
    queue = kue.createQueue();
    // Active le mode test de Kue pour permettre la simulation de jobs
    kue.testMode.enter();
  });

  afterEach(function() {
    // Après chaque test, vide la queue et désactive le mode test
    return queue.removeAsync().then(() => kue.testMode.exit());
  });

  it('should display an error message if jobs is not an array', function() {
    // Vérifie que la fonction lève une erreur
    // si le paramètre 'jobs' n'est pas un tableau
    expect(() => createPushNotificationsJobs({}, queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should create jobs in the queue and validate them', function(done) {
    // Définit un tableau d'objets représentant des jobs à créer
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    // Appelle la fonction pour créer les jobs dans la queue
    createPushNotificationsJobs(jobs, queue);

    // Utilise setTimeout pour attendre un court
    // moment avant de vérifier les résultats
    setTimeout(() => {
      // Vérifie le nombre de jobs dans le mode test de Kue
      const jobCount = kue.testMode.jobs.length;
      expect(jobCount).to.equal(2);

      // Vérifie les détails du premier job
      const job1 = kue.testMode.jobs[0];
      expect(job1.data.phoneNumber).to.equal('4153518780');
      expect(job1.data.message).to.equal('This is the code 1234 to verify your account');

      // Vérifie les détails du deuxième job
      const job2 = kue.testMode.jobs[1];
      expect(job2.data.phoneNumber).to.equal('4153518781');
      expect(job2.data.message).to.equal('This is the code 4562 to verify your account');

      // Indique que le test est terminé
      done();
    }, 100); // Délai de 100 ms pour s'assurer que les jobs sont correctement ajoutés à la queue
  });
});
