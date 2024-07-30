#!/usr/bin/env python3

"""
Application web Flask avec intégration
de Babel pour l'internationalisation.
Cette application gère la langue de l'interface
utilisateur en fonction des préférences du client
et des paramètres fournis dans l'URL.
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
                                Ici, l'anglais ('en') est
                                défini comme langue par défaut.
    BABEL_DEFAULT_TIMEZONE (str): Fuseau horaire par défaut utilisé par Babel.
                                   Ici, le fuseau horaire UTC
                                   est défini comme valeur par défaut.
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
def get_locale():
    """
    Détermine la meilleure langue à utiliser en fonction des
    préférences du client ou des paramètres de l'URL.

    Retourne:
    str: Le code de langue qui correspond le mieux aux
    préférences du client ou au paramètre URL.
    """
    # Vérifie si un paramètre de langue est
    # fourni dans la chaîne de requête de l'URL
    if request.args.get('locale') in app.config['LANGUAGES']:
        # Utilise le paramètre de langue fourni dans l'URL
        return request.args.get('locale')

    # Sinon, utilise le meilleur match basé
    # sur l'en-tête Accept-Language de la requête
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Rend la page d'accueil.

    Retourne:
    str: La page HTML rendue avec le modèle '4-index.html'.
    """
    # Utilisation de la fonction render_template pour afficher le modèle HTML
    # Le modèle '4-index.html' doit être
    # localisé en fonction de la langue sélectionnée
    return render_template('4-index.html')


if __name__ == "__main__":
    # Exécution de l'application Flask sur
    # l'adresse IP 0.0.0.0 et le port 5000
    # L'application sera accessible depuis
    # toutes les interfaces réseau de la machine
    app.run(host='0.0.0.0', port=5000)
