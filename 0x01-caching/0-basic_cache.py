#!/usr/bin/python3
""" Module BasicCache

Ce module définit la classe BasicCache,
qui représente un système de cache basique.
Auteur SAID LAMGHARI
"""

# Importe la classe BaseCaching depuis base_caching.py
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Classe BasicCache

    Hérite de BaseCaching et implémente un
    système de cache basique sans limite de taille.
    """

    def put(self, key, item):
        """ Ajoute un élément dans le cache

        Args:
            key (any): Clé pour accéder à l'élément dans le cache.
            item (any): Élément à ajouter dans le cache.

        Note:
            Si key ou item est None, la méthode ne fait rien.
        """
        if key is None or item is None:
            return  # Si key ou item est None, on ne fait rien
        # Ajoute l'item associé à la clé key dans self.cache_data
        self.cache_data[key] = item

    def get(self, key):
        """ Récupère un élément depuis le cache

        Args:
            key (any): Clé de l'élément à récupérer dans le cache.

        Returns:
            any: Élément associé à la clé key si présent, sinon None.

        Note:
            Si key est None ou si la clé n'existe pas
            dans self.cache_data, retourne None.
        """
        if key is None or key not in self.cache_data:
            # Si key est None ou n'existe pas dans le cache, retourne None
            return None
        # Retourne l'élément associé à la clé key dans self.cache_data
        return self.cache_data[key]
