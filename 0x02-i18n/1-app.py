#!/usr/bin/env python3

"""
Application web Flask avec intégration
de Babel pour l'internationalisation.
Auteur SAID LAMGHARI
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Classe de configuration pour l'application Flask.

    Attributs:
    LANGUAGES (list): Liste des langues
    supportées par l'application.
    BABEL_DEFAULT_LOCALE (str): Langue par
    défaut utilisée par Babel pour l'application.
    BABEL_DEFAULT_TIMEZONE (str): Fuseau
    horaire par défaut utilisé par Babel.
    """
    LANGUAGES = ["en", "fr"]  # Langues supportées : anglais et français
    BABEL_DEFAULT_LOCALE = 'en'  # Langue par défaut : anglais
    BABEL_DEFAULT_TIMEZONE = 'UTC'  # Fuseau horaire par défaut : UTC


# Création de l'application Flask
app = Flask(__name__)


# Chargement de la configuration depuis la classe Config
app.config.from_object(Config)


# Initialisation de Babel pour la gestion de l'internationalisation
babel = Babel(app)


@app.route('/')
def index():
    """
    Rend la page d'accueil.

    Retourne:
    str: La page HTML rendue avec le modèle '1-index.html'.
    """
    # Utilisation de la fonction
    # render_template pour afficher le modèle HTML
    return render_template('1-index.html')


if __name__ == "__main__":
    # Exécution de l'application Flask sur
    # l'adresse IP 0.0.0.0 et le port 5000
    # L'application sera accessible depuis
    # toutes les interfaces réseau de la machine
    app.run(host='0.0.0.0', port=5000)
