// Auteur SAID LAMGHARI
import redis from 'redis';
import { promisify } from 'util';

// Crée un nouveau client Redis pour se connecter au serveur Redis
const client = redis.createClient();

// Convertit les méthodes basées sur les
// callbacks de Redis en méthodes basées sur les promesses
// 'promisify' permet d'utiliser les méthodes Redis avec async/await
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Fonction asynchrone pour afficher la valeur d'une clé dans Redis
async function displaySchoolValue(schoolName) {
  try {
    // Utilise 'getAsync' pour récupérer
    // la valeur associée à la clé 'schoolName'
    const value = await getAsync(schoolName);
    // Affiche la valeur récupérée dans la console
    console.log(value);
  } catch (err) {
    // En cas d'erreur, affiche un message
    // d'erreur avec les détails du problème
    console.error(`Error fetching value for ${schoolName}: ${err.message}`);
  }
}

// Fonction asynchrone pour définir une
// nouvelle valeur pour une clé dans Redis
async function setNewSchool(schoolName, value) {
  try {
    // Utilise 'setAsync' pour définir la valeur associée à la clé 'schoolName'
    // La réponse de l'opération 'set' est affichée dans la console
    const reply = await setAsync(schoolName, value);
    console.log(`Reply: ${reply}`);
  } catch (err) {
    // En cas d'erreur, affiche un message
    // d'erreur avec les détails du problème
    console.error(`Error setting value for ${schoolName}: ${err.message}`);
  }
}

// Écoute l'événement 'connect', qui est déclenché
// lorsque la connexion au serveur Redis est établie
client.on('connect', async () => {
  // Affiche un message confirmant que le client est connecté au serveur Redis
  console.log('Redis client connected to the server');
  
  // Appelle les fonctions asynchrones pour démontrer le fonctionnement
  // Affiche la valeur actuelle associée à la clé 'Holberton'
  await displaySchoolValue('Holberton');
  
  // Définit une nouvelle valeur pour la clé 'HolbertonSanFrancisco'
  await setNewSchool('HolbertonSanFrancisco', '100');
  
  // Affiche la nouvelle valeur associée à la clé 'HolbertonSanFrancisco'
  await displaySchoolValue('HolbertonSanFrancisco');
});

// Écoute l'événement 'error', qui est déclenché en cas
// de problème avec la connexion ou les opérations Redis
client.on('error', (err) => {
  // Affiche un message d'erreur si une erreur survient lors
  // de la connexion ou de l'exécution des commandes
  console.error(`Redis client not connected to the server: ${err.message}`);
});
