// Auteur SAID LAMGHARI
import redis from 'redis';

// Crée un nouveau client Redis pour se connecter au serveur Redis
const client = redis.createClient();

// Définition d'une clé pour le hash
// et des données à stocker dans ce hash
const hashKey = 'HolbertonSchools';
const hashData = {
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2'
};

// Fonction pour créer un hash dans Redis avec les données fournies
function createHash() {
  // Parcourt chaque paire clé-valeur dans l'objet 'hashData'
  for (const [field, value] of Object.entries(hashData)) {
    // Utilise la méthode 'hset' pour ajouter
    // chaque paire clé-valeur au hash Redis
    // 'redis.print' est une fonction de rappel qui
    // affiche le résultat de l'opération 'hset' dans la console
    client.hset(hashKey, field, value, redis.print);
  }
}

// Fonction pour afficher le contenu du hash stocké dans Redis
function displayHash() {
  // Utilise la méthode 'hgetall' pour récupérer toutes
  // les paires clé-valeur du hash spécifié par 'hashKey'
  client.hgetall(hashKey, (err, obj) => {
    if (err) {
      // En cas d'erreur lors de la récupération
      // du hash, affiche un message d'erreur
      console.error(`Error fetching hash: ${err.message}`);
    } else {
      // Affiche l'objet récupéré du hash dans la console
      console.log(obj);
    }
  });
}

// Écoute l'événement 'connect', qui est déclenché
// lorsque la connexion au serveur Redis est établie
client.on('connect', () => {
  // Affiche un message confirmant que le
  // client est connecté au serveur Redis
  console.log('Redis client connected to the server');
  
  // Appelle la fonction pour créer le
  // hash avec les données définies
  createHash();
  
  // Appelle la fonction pour afficher
  // le contenu du hash après l'avoir créé
  displayHash();
});

// Écoute l'événement 'error', qui est déclenché en cas
// de problème avec la connexion ou les opérations Redis
client.on('error', (err) => {
  // Affiche un message d'erreur si une erreur survient
  // lors de la connexion ou de l'exécution des commandes
  console.error(`Redis client not connected to the server: ${err.message}`);
});
