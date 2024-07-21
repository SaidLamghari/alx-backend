#!/usr/bin/env python3
"""
Simple pagination implementation
Auteur SAID LAMGHARI
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Retourne un tuple de taille deux contenant
    l'indice de début et l'indice de fin
    correspondant à la plage d'indices à retourner
    dans une liste pour les paramètres
    de pagination donnés.

    Args:
        page (int): Numéro de page indexé à partir de 1.
        page_size (int): Nombre d'éléments par page.

    Returns:
        Tuple[int, int]: Un tuple contenant l'indice de début (inclusif) et
        l'indice de fin (exclusif) pour la
        page et la taille de page spécifiées.
    """

    strt_indx = (page - 1) * page_size
    end_ind = strt_indx + page_size
    return (strt_indx, end_ind)


class Server:
    """Classe Server pour paginer une base de
    données de prénoms populaires de bébé.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Dataset mis en cache
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Omettre l'en-tête

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Récupère la page spécifiée à partir du dataset paginé.

        Args:
            page (int): Numéro de page à récupérer (par défaut: 1).
            page_size (int): Nombre d'éléments par page (par défaut: 10).

        Returns:
            List[List]: Liste des lignes correspondant à la page demandée.
        """
        "La page doit être un entier positif."
        assert isinstance(page, int) and page > 0,
        "La taille de la page doit être un entier positif."
        assert isinstance(page_size, int) and page_size > 0,

        dataset = self.dataset()
        total_rows = len(dataset)

        # Calcul des indices de début et de fin pour la pagination
        strt_indx, end_ind = index_range(page, page_size)

        # Vérification si les indices sont hors limites
        if strt_indx >= total_rows:
            return []
        if end_ind > total_rows:
            end_ind = total_rows

        return dataset[strt_indx:end_ind]
