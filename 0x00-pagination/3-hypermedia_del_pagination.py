#!/usr/bin/env python3
"""
Pagination hypermédia résiliente à la suppression
Auteur SAID LAMGHARI
"""

import csv
from typing import List, Dict, Any


class Server:
    """Classe Server pour paginer une base de
    données de prénoms de bébés populaires."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None  # Dataset non traité
        self.__indexed_dataset = None  # Dataset indexé

    def dataset(self) -> List[List]:
        """Dataset mis en cache."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Ignorer l'en-tête
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexé par position de tri, en commençant à 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, 
                        page_size: int = 10) -> Dict[str, Any]:
        """
        Retourne un dictionnaire avec des
        informations de pagination à partir d'un index donné.
        
        Paramètres :
        - index (int) : L'indice de départ actuel de la page retournée.
        - page_size (int) : Le nombre d'éléments par page.
        
        Retourne :
        - Dict[str, Any] : Un dictionnaire
        contenant les métadonnées de pagination.
        """
        assert isinstance(index, int) and 0 <= index < len(
            self.__indexed_dataset), "Index hors de portée"

        indexed_data = self.indexed_dataset()
        data = []
        next_index = index
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
