#!/usr/bin/env python3
""" Module LFUCache

Ce module définit la classe LFUCache, qui implémente
un système de cache LFU (Least Frequently Used).
Auteur SAID LAMGHARI
"""
# Importe la classe BaseCaching depuis base_caching.py
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Classe LFUCache

    Hérite de BaseCaching et implémente
    un système de cache LFU (Least Frequently Used).
    """

    def __init__(self):
        """ Initialise le cache """
        # Appelle le constructeur __init__ de la classe parent BaseCaching
        super().__init__()
        # Initialise un dictionnaire pour suivre
        # le nombre d'utilisations de chaque clé
        self.usage_count = {}
        # Initialise une liste pour suivre l'ordre des clés utilisées
        self.order = []

    def put(self, key, item):
        """ Ajoute un élément dans le cache

        Si le cache dépasse la limite de MAX_ITEMS,
        l'élément le moins fréquemment utilisé est supprimé.
        En cas d'égalité, l'élément le moins récemment utilisé est supprimé.

        Args:
            key (str): La clé sous laquelle l'élément doit être stocké.
            item (Any): L'élément à stocker dans le cache.
        """
        if key is None or item is None:
            return  # Si key ou item est None, la méthode ne fait rien
        
        if key in self.cache_data:
            # Met à jour l'élément associé à key dans le cache
            self.cache_data[key] = item
            # Incrémente le compteur d'utilisation pour key
            self.usage_count[key] += 1
            self.order.remove(key)  # Retire key de l'ordre actuel
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Trouve la clé LFU (Least Frequently Used)
                lfu_key = min(self.usage_count, key=self.usage_count.get)
                # Récupère toutes les clés ayant le nombre minimal d'utilisations
                keysmin_usge = [k for k, v in self.usage_count.items() if v == self.usage_count[lfu_key]]
                if len(keysmin_usge) > 1:
                    # S'il y a une égalité, choisit la clé qui est la moins récemment utilisée
                    lfu_key = next(k for k in self.order if k in keysmin_usge)
                self.order.remove(lfu_key)  # Retire la clé LFU de l'ordre actuel
                del self.cache_data[lfu_key]  # Supprime l'élément associé à la clé LFU du cache
                del self.usage_count[lfu_key]  # Supprime le compteur d'utilisation de la clé LFU
                print("DISCARD: {}".format(lfu_key))  # Affiche la clé LFU supprimée avec un message DISCARD

            self.cache_data[key] = item  # Ajoute le nouvel élément au cache
            self.usage_count[key] = 1  # Initialise le compteur d'utilisation pour la nouvelle clé à 1

        self.order.append(key)  # Ajoute la clé à la fin de l'ordre pour indiquer qu'elle a été utilisée récemment

    def get(self, key):
        """ Récupère un élément du cache par sa clé

        Args:
            key (str): La clé à rechercher dans le cache.

        Returns:
            Any: La valeur associée à la clé, ou None si la clé n'existe pas.
        """
        if key in self.cache_data:
            self.usage_count[key] += 1  # Incrémente le compteur d'utilisation pour key
            self.order.remove(key)  # Retire key de l'ordre actuel
            self.order.append(key)  # Ajoute key à la fin de l'ordre pour indiquer qu'elle a été utilisée récemment
            return self.cache_data[key]  # Retourne l'élément associé à key dans le cache
        
        return None  # Retourne None si la clé n'est pas trouvée dans le cache
