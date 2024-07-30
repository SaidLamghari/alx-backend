#!/usr/bin/env python3

"""
Application web Flask avec intégration de Babel pour
l'internationalisation et connexion utilisateur fictive,
incluant un support pour les fuseaux horaires.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError


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
    BABEL_DEFAULT_TIMEZONE (str): Fuseau horaire par
    défaut utilisé par Babel.
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

# Base de données fictive des utilisateurs
# Utilisée pour simuler des connexions utilisateurs
# avec des paramètres de langue et de fuseau horaire
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Récupère un dictionnaire d'utilisateur basé sur le paramètre URL login_as.

    Retourne:
    dict ou None: Le dictionnaire de l'utilisateur
    si l'ID utilisateur est valide, sinon None.
    """
    # Obtient l'ID utilisateur à partir du paramètre URL 'login_as'
    user_id = request.args.get('login_as')
    # Vérifie si l'ID utilisateur est un nombre entier
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        # Retourne le dictionnaire de l'utilisateur si l'ID est valide
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """
    Fonction exécutée avant chaque requête. Définit l'utilisateur
    dans flask.g si le paramètre URL login_as est fourni.
    """
    # Définit l'utilisateur dans flask.g pour rendre accessible
    # les informations de l'utilisateur dans d'autres parties de l'application
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Détermine la meilleure langue à utiliser en fonction
    des paramètres URL, des préférences utilisateur,
    de l'en-tête Accept-Language de la requête, ou de la langue par défaut.

    Retourne:
    str: Le code de langue déterminé en fonction de l'ordre de priorité.
    """
    # Vérifie si une langue est fournie dans la chaîne de requête de l'URL
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        # Utilise la langue fournie dans l'URL si elle est supportée
        return locale

    # Vérifie si l'utilisateur est connecté
    # et possède une langue préférée
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        # Utilise la langue préférée de l'utilisateur si elle est supportée
        return g.user['locale']

    # Sinon, utilise le meilleur match basé sur
    # l'en-tête Accept-Language de la requête
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    Détermine le meilleur fuseau horaire à utiliser en fonction
    des paramètres URL, des préférences utilisateur,
    ou du fuseau horaire par défaut.

    Retourne:
    str: La chaîne de caractère du fuseau horaire déterminée
    en fonction de l'ordre de priorité.
    """
    # Vérifie si un fuseau horaire est fourni
    # dans la chaîne de requête de l'URL
    timezone = request.args.get('timezone')
    if timezone:
        try:
            # Valide le fuseau horaire
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            # Ignore si le fuseau horaire est invalide
            pass

    # Vérifie si l'utilisateur est connecté et
    # possède un fuseau horaire préféré
    if g.user and g.user['timezone']:
        try:
            # Valide le fuseau horaire
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except UnknownTimeZoneError:
            # Ignore si le fuseau horaire est invalide
            pass

    # Par défaut, utilise le fuseau horaire UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """
    Rend la page d'accueil.

    Retourne:
    str: La page HTML rendue avec le modèle '7-index.html',
    affichant le titre, l'en-tête et le message du fuseau horaire.
    """
    return render_template('7-index.html')


if __name__ == "__main__":
    # Exécution de l'application Flask sur
    # l'adresse IP 0.0.0.0 et le port 5000
    # L'application sera accessible depuis toutes
    # les interfaces réseau de la machine
    app.run(host='0.0.0.0', port=5000)
