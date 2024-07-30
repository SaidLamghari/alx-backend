#!/usr/bin/env python3

"""
Application web Flask avec intégration de Babel pour
l'internationalisation.
Cette application permet de servir une page d'accueil et
de gérer la sélection de la langue en fonction des préférences du client.
Auteur SAID LAMGHARI
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """
    Classe de configuration pour l'application Flask.

    Attributs:
    LANGUAGES (list): Liste des langues supportées par l'application.
                      Ici, l'application supporte l'anglais
                      ('en') et le français ('fr').
    BABEL_DEFAULT_LOCALE (str): Langue par défaut utilisée
                                par Babel pour l'application.
                                Ici, l'anglais ('en') est défini
                                comme langue par défaut.
    BABEL_DEFAULT_TIMEZONE (str): Fuseau horaire par défaut
utilisé par Babel.Ici, le fuseau horaire UTC est défini
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


@babel.localeselector
def get_locale() -> str:
    """
    def get_locale():

    Détermine la meilleure langue à utiliser
    en fonction des préférences du client.

    Retourne:
    str: Le code de langue qui correspond le
    mieux aux préférences du client.
    """
    # Sélectionne la langue préférée du client en
    # fonction des langues supportées par l'application
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    @app.route('/')
    def index():

    Rend la page d'accueil.

    Retourne:
    str: La page HTML rendue avec le modèle '3-index.html'.
    """
    # Utilisation de la fonction render_template
    # pour afficher le modèle HTML
    # Le modèle '3-index.html' doit être localisé
    # en fonction de la langue sélectionnée
    return render_template('3-index.html')


if __name__ == "__main__":
    # Exécution de l'application Flask sur
    # l'adresse IP 0.0.0.0 et le port 5000
    # L'application sera accessible depuis
    # toutes les interfaces réseau de la machine
    app.run()
