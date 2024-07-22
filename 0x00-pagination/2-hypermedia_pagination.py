#!/usr/bin/env python3
"""
Ce module contient la classe Server et la
fonction index_range pour la pagination.
Auteur SAID LAMGHARI
"""

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Retourne un tuple contenant l'indice
    de début et l'indice de fin pour une page donnée.

    Paramètres :
    - page (int) : Le numéro de page actuel (indexé à partir de 1).
    - page_size (int) : Le nombre d'éléments par page.

    Retourne :
    - Tuple[int, int] : Un tuple contenant l'indice
        de début et l'indice de fin.
    """
    # Calcul de l'indice de début de la page
    strt_ind = (page - 1) * page_size
    # Calcul de l'indice de fin de la page
    end_ind = page * page_size
    return strt_ind, end_ind


class Server:
    """Classe Server pour paginer une base de
    données de prénoms populaires de bébés.
    """
    # Chemin vers le fichier CSV des prénoms populaires
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        # Initialisation du dataset
        # en tant qu'attribut privé
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Retourne le dataset en cache.

        Charge le fichier CSV en mémoire s'il n'est pas encore chargé.
        """
        # Vérifie si le dataset n'a pas été chargé
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                # Lit toutes les lignes du fichier CSV
                dataset = [row for row in reader]
            # Ignore l'en-tête et stocke le dataset sans l'en-tête
            self.__dataset = dataset[1:]

        # Retourne le dataset en cache
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retourne une page du dataset.

        Paramètres :
        - page (int) : Le numéro de page actuel (indexé à partir de 1).
        - page_size (int) : Le nombre d'éléments par page.

        Retourne :
        - List[List] : Une liste de lignes
            correspondant à la page et page_size donnés.
        """
        "La page doit être un entier supérieur à 0"
        assert isinstance(page, int) and page > 0, "La page sup à 0"
        "La taille de la page doit être un entier supérieur à 0"
        assert isinstance(page_size, int) and page_size > 0, "La taille sup 0"

        # Calcul des indices de début et fin de la page
        strt_ind, end_ind = index_range(page, page_size)
        # Récupère le dataset
        dataset = self.dataset()

        if strt_ind >= len(dataset):
            # Retourne une liste vide si l'indice de
            # début dépasse la taille du dataset
            return []

        # Retourne les lignes correspondant à la page demandée
        return dataset[strt_ind:end_ind]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Retourne un dictionnaire contenant les métadonnées de pagination.

        Paramètres :
        - page (int) : Le numéro de page actuel (indexé à partir de 1).
        - page_size (int) : Le nombre d'éléments par page.

        Retourne :
        - Dict[str, Any] : Un dictionnaire
            contenant les métadonnées de pagination.
        """
        data = self.get_page(page, page_size)  # Récupère la page de données
        # Calcule le nombre total d'éléments dans le dataset
        total_items = len(self.dataset())
        # Calcule le nombre total de pages nécessaires
        total_pages = math.ceil(total_items / page_size)

        # Calcule la page suivante, ou None si c'est la dernière page
        next_page = page + 1 if page < total_pages else None
        # Calcule la page précédente, ou None si c'est la première page
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),  # Nombre d'éléments sur la page courante
            "page": page,  # Numéro de la page courante
            "data": data,  # Les données de la page courante
            "next_page": next_page,  # Numéro de la page suivante
            "prev_page": prev_page,  # Numéro de la page précédente
            "total_pages": total_pages  # Nombre total de pages
        }
