#!/usr/bin/env python3
""" Module LRUCache

Ce module définit la classe LRUCache, qui implémente
un système de cache LRU (Least Recently Used).
Auteur SAID LAMGHARI
"""
# Importe la classe BaseCaching depuis base_caching.py
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Classe LRUCache

    Hérite de BaseCaching et implémente un
    système de cache LRU (Least Recently Used).
    """

    def __init__(self):
        """ Initialise le cache """
        # Appelle le constructeur __init__ de la classe parent BaseCaching
        super().__init__()
        # Initialise une liste pour suivre l'ordre des clés utilisées
        self.order = []

    def put(self, key, item):
        """ Ajoute un élément dans le cache

        Si le cache dépasse la limite de MAX_ITEMS,
        l'élément le moins récemment utilisé est supprimé.

        Args:
            key (str): La clé sous laquelle l'élément doit être stocké.
            item (any): L'élément à stocker dans le cache.
        """
        if key is None or item is None:
            return  # Si key ou item est None, la méthode ne fait rien

        if key in self.cache_data:
            self.order.remove(key)  # Retire la clé de l'ordre actuel
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Retire la clé la moins récemment utilisée (LRU)
            lru_ky = self.order.pop(0)
            # Supprime l'élément associé à la clé LRU du cache
            del self.cache_data[lru_ky]
            # Affiche la clé LRU supprimée avec un message DISCARD
            print("DISCARD: {}".format(lru_ky))

        self.cache_data[key] = item  # Ajoute le nouvel élément au cache
        self.order.append(key)  # Ajoute la clé à la fin de l'ordre

    def get(self, key):
        """ Récupère un élément du cache par sa clé

        Args:
            key (str): La clé à rechercher dans le cache.

        Returns:
            any: La valeur associée à la clé, ou None si la clé n'existe pas.
        """
        if key in self.cache_data:
            self.order.remove(key)  # Retire la clé de l'ordre actuel
            # Ajoute la clé à la fin de l'ordre pour
            # indiquer qu'elle a été utilisée récemment
            self.order.append(key)
            return self.cache_data[key]  # Retourne l'élément associé à la clé

        return None  # Retourne None si la clé n'est pas trouvée dans le cache
