#!/usr/bin/env python3
"""
Implémentation de la pagination hypermédia
"""

import csv
import math
from typing import List, Dict
from 1-simple_pagination import index_range, Server as SimpleServer


class Server(SimpleServer):
    """
    Classe Server pour paginer une base de données de
    noms populaires de bébés avec des métadonnées hypermédia.
    """

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Récupère une page du jeu de données avec des métadonnées hypermédia.

        Args:
        - page (int): Numéro de la page à récupérer (par défaut: 1).
        - page_size (int): Nombre d'éléments par page (par défaut: 10).

        Returns:
        - Dict: Un dictionnaire contenant les métadonnées
            hypermédia pour la page demandée.
          - "page_size": Nombre d'éléments dans la page actuelle.
          - "page": Numéro de la page actuelle.
          - "data": Les données de la page actuelle.
          - "next_page": Numéro de la page suivante,
            ou None si c'est la dernière page.
          - "prev_page": Numéro de la page précédente,
          ou None si c'est la première page.
          - "total_pages": Nombre total de pages dans le jeu de données.
        """
        # Récupère les données de la page
        # demandée à l'aide de la méthode héritée
        data = self.get_page(page, page_size)

        # Récupère l'ensemble des données
        # pour calculer le nombre total de pages
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        # Construit et retourne le dictionnaire
        # de métadonnées hypermédia
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
