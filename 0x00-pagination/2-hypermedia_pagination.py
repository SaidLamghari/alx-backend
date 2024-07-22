#!/usr/bin/env python3
"""
Fonction utilitaire simple pour la pagination
Auteur: SAID LAMGHARI
"""
import csv
import math
from typing import List, Dict, Union, Optional
from functools import lru_cache


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Retourne un tuple de taille deux
    contenant l'indice de début et l'indice de fin
    correspondant à la plage d'indices à
    retourner dans une liste pour les
    paramètres de pagination spécifiés.

    Args:
        page (int): Numéro de la page à retourner (1-indexé).
        page_size (int): Nombre d'éléments par page.

    Returns:
        tuple[int, int]: Un tuple contenant l'indice de début (inclusif)
        et l'indice de fin (exclusif) pour
        la page spécifiée et la taille de page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Classe Server pour paginer une base de
    données de noms de bébés populaires."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    @lru_cache(maxsize=None)
    def dataset(self) -> List[List[str]]:
        """Renvoie le jeu de données en cache."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                # Ignorer l'en-tête
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Récupère la page spécifiée du jeu de données.

        Args:
            page (int): Numéro de la page à récupérer (par défaut: 1).
            page_size (int): Nombre
                d'enregistrements par page (par défaut: 10).

        Returns:
            List[List[str]]: Liste de listes
            contenant les lignes de données demandées.
        """
        # Vérifier que les arguments sont des entiers positifs
        "Le numéro de page doit être un entier positif."
        assert isinstance(page, int) and page > 0, "Le numéro positif."
        "La taille de page doit être un entier positif."
        assert isinstance(page_size, int) and page_size > 0, "Taill positif."

        # Charger le jeu de données à partir du fichier CSV
        dataset = self.dataset()
        total_rows = len(dataset)

        # Calculer les indices de début et de fin pour la pagination
        start_index, end_index = index_range(page, page_size)

        # Vérifier si l'indice de début est hors
        # des limites du jeu de données
        if start_index >= total_rows:
            return []
        # Ajuster l'indice de fin si nécessaire pour
        # éviter une IndexError
        if end_index > total_rows:
            end_index = total_rows

        # Retourner la partie du jeu de données
        # correspondant à la page demandée
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str,
                                               Union[int,
                                                     List[List[str]],
                                                     Optional[int]]]:
        """
        Récupère les informations hypermédia avec
        la page spécifiée du jeu de données.

        Args:
            page (int): Numéro de la page à récupérer (par défaut: 1).
            page_size (int): Nombre d'enregistrements
            par page (par défaut: 10).

        Returns:
            Dict[str, Union[int, List[List[str]], Optional[int]]]:
                    Dictionnaire contenant :
                - 'page_size': Taille de la page de données retournée.
                - 'page': Numéro de la page actuelle.
                - 'data': Page du jeu de données
                    (équivalent au retour de get_page).
                - 'next_page': Numéro de la prochaine page,
                    None s'il n'y a pas de prochaine page.
                - 'prev_page': Numéro de la page précédente,
                    None s'il n'y a pas de page précédente.
                - 'total_pages': Nombre total de pages dans
                    le jeu de données en tant qu'entier.
        """
        # Récupérer les données de la page demandée en utilisant get_page
        data = self.get_page(page, page_size)
        # Calculer le nombre total de lignes dans le jeu de données
        total_rows = len(self.dataset())
        # Calculer le nombre total de pages
        # en utilisant math.ceil pour arrondir vers le haut
        total_pages = math.ceil(total_rows / page_size)

        # Calculer le numéro de la page suivante et précédente
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Retourner un dictionnaire contenant
        # les informations hypermédia
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
