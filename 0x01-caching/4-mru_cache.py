#!/usr/bin/env python3
""" Module MRUCache

Ce module définit la classe MRUCache, qui implémente un système de cache MRU (Most Recently Used).
"""

from base_caching import BaseCaching  # Importe la classe BaseCaching depuis base_caching.py


class MRUCache(BaseCaching):
    """ Classe MRUCache

    Hérite de BaseCaching et implémente un système de cache MRU (Most Recently Used).
    """

    def __init__(self):
        """ Initialise le cache """
        super().__init__()  # Appelle le constructeur __init__ de la classe parent BaseCaching
        self.order = []  # Initialise une liste pour suivre l'ordre des clés utilisées

    def put(self, key, item):
        """ Ajoute un élément dans le cache

        Si le cache dépasse la limite de MAX_ITEMS,
        l'élément le plus récemment utilisé est supprimé.

        Args:
            key (str): La clé sous laquelle l'élément doit être stocké.
            item (any): L'élément à stocker dans le cache.
        """
        if key is None or item is None:
            return  # Si key ou item est None, la méthode ne fait rien
        
        if key in self.cache_data:
            self.order.remove(key)  # Retire la clé de l'ordre actuel
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.order.pop()  # Retire la clé la plus récemment utilisée (MRU)
            del self.cache_data[mru_key]  # Supprime l'élément associé à la clé MRU du cache
            print("DISCARD: {}".format(mru_key))  # Affiche la clé MRU supprimée avec un message DISCARD
        
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
            self.order.append(key)  # Ajoute la clé à la fin de l'ordre pour indiquer qu'elle a été utilisée récemment
            return self.cache_data[key]  # Retourne l'élément associé à la clé
        
        return None  # Retourne None si la clé n'est pas trouvée dans le cache
