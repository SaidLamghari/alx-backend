// Auteur SAID LAMGHARI
import redis from 'redis';

// Crée un nouveau client Redis pour se connecter au serveur Redis
const client = redis.createClient();

// Écoute l'événement 'connect', qui est
// déclenché lorsque la connexion au serveur Redis est établie
client.on('connect', () => {
  // Affiche un message confirmant que le
  // client est connecté au serveur Redis
  console.log('Redis client connected to the server');
  
  // Abonne le client au canal nommé 'holberton school channel'
  // Les messages publiés sur ce canal seront reçus par ce client
  client.subscribe('holberton school channel');
});

// Écoute l'événement 'error', qui est déclenché en cas
// de problème avec la connexion ou les opérations Redis
client.on('error', (err) => {
  // Affiche un message d'erreur si une erreur survient lors
  // de la connexion ou de l'exécution des commandes
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Écoute l'événement 'message', qui est déclenché lorsqu'un
// message est reçu sur un canal auquel le client est abonné
client.on('message', (channel, message) => {
  // Affiche le message reçu dans la console
  console.log(message);
  
  // Vérifie si le message est 'KILL_SERVER'
  // Si c'est le cas, désabonne le client du
  // canal et ferme la connexion Redis
  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.quit(); // Termine la connexion avec le serveur Redis
  }
});

