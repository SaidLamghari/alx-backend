// Auteur SAID LAMGHARI
import redis from 'redis';

// Crée une instance de client Redis pour se connecter au serveur Redis
const client = redis.createClient();

// Fonction pour publier des messages sur
// un canal Redis après un certain délai
function publishMessage(message, time) {
  // Utilise 'setTimeout' pour attendre un certain délai
  // (en millisecondes) avant d'exécuter la fonction de publication
  setTimeout(() => {
    // Affiche un message dans la console indiquant que le message va être envoyé
    console.log(`About to send ${message}`);
    
    // Utilise la méthode 'publish' du client Redis pour
    // envoyer le message au canal 'holberton school channel'
    client.publish('holberton school channel', message);
  }, time);
}

// Écoute l'événement 'connect', qui est déclenché
// lorsque la connexion au serveur Redis est établie
client.on('connect', () => {
  // Affiche un message confirmant que le client est connecté au serveur Redis
  console.log('Redis client connected to the server');
  
  // Appelle la fonction 'publishMessage' pour
  // publier différents messages sur le canal
  // Les messages seront publiés avec un délai défini par le paramètre 'time'
  publishMessage('Holberton Student #1 starts course', 100);
  publishMessage('Holberton Student #2 starts course', 200);
  publishMessage('KILL_SERVER', 300);
  publishMessage('Holberton Student #3 starts course', 400);
});

// Écoute l'événement 'error', qui est déclenché en cas de
// problème avec la connexion ou les opérations Redis
client.on('error', (err) => {
  // Affiche un message d'erreur si une erreur survient
  // lors de la connexion ou de l'exécution des commandes
  console.error(`Redis client not connected to the server: ${err.message}`);
});
