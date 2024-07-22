#!/usr/bin/env python3
"""
Pagination hypermédia résiliente à la suppression
Auteur Said LAMGHARI
"""

import csv
from typing import List, Dict, Any


class Server:
    """Classe Server pour paginer une base
    de données de prénoms populaires de bébé."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None  # Dataset brut non indexé
        self.__indexed_dataset = None  # Dataset indexé par position de tri

    def dataset(self) -> List[List]:
        """
        Retourne le dataset brut en lisant
        le fichier CSV, excluant l'en-tête.

        Returns:
        - List[List]: Liste des lignes de données du fichier CSV.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclure l'en-tête
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Retourne le dataset indexé par position
        de tri, en commençant à l'indice 0.

        Returns:
        - Dict[int, List]: Dictionnaire avec
        les données indexées par leur position.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retourne un dictionnaire avec les
        informations de pagination à partir d'un index donné.

        Parameters:
        - index (int): L'indice de départ actuel de la page à retourner.
        - page_size (int): Le nombre d'éléments par page.

        Returns:
        - Dict[str, Any]: Un dictionnaire contenant
        les métadonnées de pagination.
        """
        # Vérifie que l'index est valide
        assert isinstance(index, int) and index >= 0 and index < len(
            self.__indexed_dataset)

        indexed_data = self.indexed_dataset()
        data = []
        next_index = index
        # Collecte les données pour la page actuelle
        while len(data) < page_size and next_index < len(indexed_data):
            if next_index in indexed_data:
                data.append(indexed_data[next_index])
            next_index += 1

        next_index = next_index if next_index < len(indexed_data) else None

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
