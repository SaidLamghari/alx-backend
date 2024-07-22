#!/usr/bin/env python3
"""
Classe Server qui pagine une base de données de noms de bébés populaires.
Auteur SAID LAMGHARI
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Prend_indx deux arguments entiers et retourne un tuple de taille deux
    contenant l'indice de début et l'indice de fin correspondant à la plage
    d'indices à retourner dans une liste pour ces paramètres de pagination.

    Args:
        page (int): Numéro de page à retourner (les pages commencent à 1).
        page_size (int): Nombre d'éléments par page.

    Returns:
        Tuple[int, int]: Un tuple contenant
        l'indice de début et l'indice de fin.
    """
    strt_indx = (page - 1) * page_size
    end_indx = page * page_size
    return (strt_indx, end_indx)


class Server:
    """Classe Server pour paginer une base de
    données de noms de bébés populaires."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Jeu de données en cache.

        Returns:
            List[List]: Le jeu de données sous forme de liste de listes.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                # Sauvegarde du jeu de données excluant l'en-tête
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Prend_indx deux arguments entiers et retourne
        la page demandée du jeu de données.

        Args:
            page (int): Numéro de la page demandée (par défaut: 1).
            page_size (int): Nombre d'enregistrements
                par page (par défaut: 10).

        Returns:
            List[List]: Liste de listes contenant
            les données requises du jeu de données.
        """
        "Le numéro de page doit être un entier positif."
        assert isinstance(page, int) and page > 0, "Le numéro positif."
        "La taille de page doit être un entier positif."
        assert isinstance(page_size, int) and page_size > 0, "taille positif"

        dataset = self.dataset()
        try:
            strt_indx, end_indx = index_range(page, page_size)
            return dataset[strt_indx:end_indx]
        except IndexError:
            return []
