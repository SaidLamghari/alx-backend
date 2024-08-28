// Auteur SAID LAMGHARI
const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

// Créez une instance de l'application Express
const app = express();
const port = 1245;

// Définissez la liste des produits disponibles
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

// Fonction pour obtenir un produit par son ID
function getItemById(id) {
  return listProducts.find(product => product.id === id);
}

// Créez un client Redis et promisify ses
// méthodes pour les utiliser avec des promesses
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Fonction pour réserver
// du stock en utilisant Redis
function reserveStockById(itemId, stock) {
  // Stocke le nombre de
  // produits réservés dans Redis
  return setAsync(`item.${itemId}`, stock);
}

// Fonction pour obtenir le stock
// réservé actuel depuis Redis
async function getCurrentReservedStockById(itemId) {
  // Récupère la quantité réservée
  // pour un produit spécifique
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock, 10) : 0;
}

// Route pour lister tous les produits
app.get('/list_products', (req, res) => {
  // Transforme la liste des produits en un format JSON
  const products = listProducts.map(({ id, name, price, stock }) => ({
    itemId: id,
    itemName: name,
    price,
    initialAvailableQuantity: stock
  }));
  // Répond avec la liste des produits
  res.json(products);
});

// Route pour obtenir les détails
// d'un produit spécifique par ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);
  
  // Vérifie si le produit existe
  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  // Obtient la quantité réservée pour le produit
  const reservedStock = await getCurrentReservedStockById(itemId);
  // Calcule la quantité disponible actuelle
  const currentQuantity = product.stock - reservedStock;

  // Répond avec les détails du produit
  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity
  });
});

// Route pour réserver un produit
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);
  
  // Vérifie si le produit existe
  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  // Obtient la quantité réservée pour le produit
  const reservedStock = await getCurrentReservedStockById(itemId);
  // Calcule la quantité disponible actuelle
  const currentQuantity = product.stock - reservedStock;

  // Vérifie s'il y a suffisamment de stock disponible
  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  // Réserve un produit supplémentaire
  await reserveStockById(itemId, reservedStock + 1);
  // Répond avec la confirmation de la réservation
  res.json({ status: 'Reservation confirmed', itemId });
});

// Démarre le serveur sur le port défini
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
