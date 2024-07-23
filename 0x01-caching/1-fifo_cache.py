#!/usr/bin/python3
""" Module FIFOCache

Ce module définit la classe FIFOCache, qui représente un système
de cache utilisant l'algorithme FIFO (Premier Entré, Premier Sorti).
Auteur SAID LAMGHARI
"""
# Importe la classe BaseCaching depuis base_caching.py
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Classe FIFOCache

    Hérite de BaseCaching et implémente un
    système de cache utilisant l'algorithme FIFO.
    """

    def __init__(self):
        """ Initialise le cache en appelant le
        constructeur de la classe parent BaseCaching
        """
        # Appelle le constructeur __init__ de la classe parent BaseCaching
        super().__init__()

    def put(self, key, item):
        """ Ajoute un élément dans le cache avec la stratégie d'éviction FIFO

        Args:
            key (any): Clé pour accéder à l'élément dans le cache.
            item (any): Élément à ajouter dans le cache.

        Notes:
            Si key ou item est None, la méthode ne fait rien.
            Si le nombre d'éléments dans
            self.cache_data atteint self.MAX_ITEMS,
            le premier élément ajouté au cache est
            supprimé (algorithme FIFO) avec un message DISCARD.
        """
        if key is None or item is None:
            return  # Si key ou item est None, la méthode ne fait rien

        # Vérifie si le cache est plein
        if len(self.cache_data) >= self.MAX_ITEMS:
            # Trouve la première clé ajoutée au cache (éviction FIFO)
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            # Supprime le premier élément du cache
            del self.cache_data[first_key]

        self.cache_data[key] = item  # Ajoute le nouvel élément au cache

    def get(self, key):
        """ Récupère un élément du cache

        Args:
            key (any): Clé de l'élément à récupérer dans le cache.

        Returns:
            any: Élément associé à la clé key si présent, sinon None.

        Notes:
            Si key est None ou si la clé n'existe
            pas dans self.cache_data, retourne None.
        """
        if key is None or key not in self.cache_data:
            # Si key est None ou n'existe pas dans le cache, retourne None
            return None

        # Retourne l'élément associé à key dans self.cache_data
        return self.cache_data[key]
