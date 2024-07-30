#!/usr/bin/env python3

"""
Une application web simple avec Flask,
contenant une seule route.
Auteur SAID LAMGHARI
"""

from flask import Flask, render_template

# Création de l'application Flask
app = Flask(__name__)


@app.route('/')
def index():
    """
    Rend la page d'accueil.

    Retourne:
    str: La page HTML rendue avec le modèle '0-index.html'.
    """
    # Utilisation de la fonction render_template
    # pour afficher le modèle HTML
    return render_template('0-index.html')


if __name__ == "__main__":
    # Exécution de l'application Flask sur
    # l'adresse IP 0.0.0.0 et le port 5000
    app.run(host='0.0.0.0', port=5000)
