// Auteur SAID LAMGHARI
import redis from 'redis';

// Crée un nouveau client Redis pour se connecter au serveur Redis
const client = redis.createClient();

// Fonction pour afficher la valeur d'une clé dans Redis
function displaySchoolValue(schoolName) {
  // Utilise la méthode 'get' du client Redis pour
  // récupérer la valeur associée à la clé 'schoolName'
  client.get(schoolName, (err, reply) => {
    if (err) {
      // En cas d'erreur, affiche un message
      // d'erreur avec les détails du problème
      console.error(`Error fetching value for ${schoolName}: ${err.message}`);
    } else {
      // Affiche la valeur récupérée
      // depuis Redis (réponse) dans la console
      console.log(reply);
    }
  });
}

// Fonction pour définir une nouvelle valeur pour une clé dans Redis
function setNewSchool(schoolName, value) {
  // Utilise la méthode 'set' du client Redis pour
  // définir la valeur associée à la clé 'schoolName'
  // 'redis.print' est une fonction de rappel qui
  // affiche le résultat de l'opération 'set' dans la console
  client.set(schoolName, value, redis.print);
}

// Écoute l'événement 'connect', qui est déclenché
// lorsque la connexion au serveur Redis est établie
client.on('connect', () => {
  // Affiche un message confirmant que le client est connecté au serveur Redis
  console.log('Redis client connected to the server');
  
  // Appel des fonctions pour démontrer le fonctionnement
  // Affiche la valeur actuelle associée à la clé 'Holberton'
  displaySchoolValue('Holberton');
  
  // Définit une nouvelle valeur pour la clé 'HolbertonSanFrancisco'
  setNewSchool('HolbertonSanFrancisco', '100');
  
  // Affiche la nouvelle valeur associée à la clé 'HolbertonSanFrancisco'
  displaySchoolValue('HolbertonSanFrancisco');
});

// Écoute l'événement 'error', qui est déclenché en cas de
// problème avec la connexion ou les opérations Redis
client.on('error', (err) => {
  // Affiche un message d'erreur si une erreur survient
  // lors de la connexion ou de l'exécution des commandes
  console.error(`Redis client not connected to the server: ${err.message}`);
});
