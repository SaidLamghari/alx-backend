// Auteur SAID LAMGHARI
import redis from 'redis';

// Crée un nouveau client Redis.
// Ce client est utilisé pour établir une connexion avec
// le serveur Redis et pour envoyer des commandes Redis.
const client = redis.createClient();

// Ajoute un écouteur pour l'événement 'connect'.
// Cet événement est déclenché lorsque la connexion au
// serveur Redis est établie avec succès.
client.on('connect', () => {
  // Affiche un message dans la console pour confirmer
  // que la connexion au serveur Redis est établie.
  console.log('Redis client connected to the server');
});

// Ajoute un écouteur pour l'événement 'error'.
// Cet événement est déclenché lorsqu'il y a un problème avec
// la connexion ou avec l'exécution des commandes Redis.
client.on('error', (err) => {
  // Affiche un message d'erreur dans la console
  // avec les détails du problème rencontré.
  console.error(`Redis client not connected to the server: ${err.message}`);
});
