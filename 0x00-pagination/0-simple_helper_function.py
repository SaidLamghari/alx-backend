#!/usr/bin/env python3
"""
Fonction utilitaire simple pour la pagination
Auteur: SAID LAMGHARI
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Retourne un tuple de taille deux contenant
    un indice de début et un indice de fin
    correspondant à la plage d'indices à retourner
    dans une liste pour les paramètres
    de pagination donnés.

    Args:
    - page (int): Le numéro de la page pour laquelle
        on veut calculer l'indice de début et de fin.
    - page_size (int): Le nombre d'éléments par page.

    Returns:
    - Tuple[int, int]: Un tuple contenant l'indice
        de début et l'indice de fin pour la page donnée.
    """
    # Calcul de l'indice de début
    strt_ind = (page - 1) * page_size

    # Calcul de l'indice de fin
    end_ind = page * page_size

    # Retourne un tuple contenant l'indice de début et l'indice de fin
    return (strt_ind, end_ind)
