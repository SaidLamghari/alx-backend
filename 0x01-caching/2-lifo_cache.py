#!/usr/bin/env python3
""" Module LIFOCache

Ce module définit la classe LIFOCache, qui représente un
système de cache utilisant l'algorithme LIFO (Last-In-First-Out).
"""
# Importe la classe BaseCaching depuis base_caching.py
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Classe LIFOCache

    Hérite de BaseCaching et implémente
    un système de cache utilisant l'algorithme LIFO.
    """

    def __init__(self):
        """ Initialise le cache en appelant
        le constructeur de la classe parent BaseCaching
        """
        # Appelle le constructeur __init__ de la classe parent BaseCaching
        super().__init__()
        # Initialise last_key à None pour suivre la dernière clé insérée
        self.last_key = None

    def put(self, key, item):
        """ Ajoute un élément dans le cache avec
        la stratégie d'éviction LIFO (Last-In-First-Out)

        Args:
            key (any): Clé pour accéder à l'élément dans le cache.
            item (any): Élément à ajouter dans le cache.

        Notes:
            Si key ou item est None, la méthode ne fait rien.
            Si le nombre d'éléments dans self.cache_data atteint
            BaseCaching.MAX_ITEMS et que key n'est pas déjà dans le cache,
            l'algorithme supprime le dernier élément
            ajouté au cache (LIFO) avec un message DISCARD.
        """
        if key is None or item is None:
            return  # Si key ou item est None, la méthode ne fait rien

        # Vérifie si le cache est plein et
        # si key n'est pas déjà présent dans le cache
        var = len(self.cache_data)
        if var >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            if self.last_key:
                print(f"DISCARD: {self.last_key}")
                # Supprime le dernier élément du cache
                del self.cache_data[self.last_key]

        self.cache_data[key] = item  # Ajoute le nouvel élément au cache
        self.last_key = key  # Metà jour last_key avec la nouvelle clé insérée

    def get(self, key):
        """ Récupère un élément du cache par sa clé

        Args:
            key (any): Clé de l'élément à récupérer dans le cache.

        Returns:
            any: Élément associé à la clé key si présent, sinon None.
        """
        # Retourne l'élément associé à key dans
        # self.cache_data ou None si non trouvé
        return self.cache_data.get(key, None)
