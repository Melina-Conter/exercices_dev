from ..app import app
from flask import render_template

@app.route("/")
def accueil():
    return render_template("pages/accueil.html")

import requests
@app.route("/retrieve_wikidata/<id>")
def retrieve_wikidata (id):
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{id}.json"

    # Envoi de la requête GET
    response = requests.get(url)

    # Récupérer le code HTTP
    http_code = response.status_code

    # Récupérer le type de média 
    media_type = response.headers.get('Content-Type', 'Type non spécifié')

    #Récupérer l'encodage
    encoding = response.encoding
    
    #Par défaut, data est vide ainf d'éviter les erreurs
    data = None

    # Si la requête a réussi (code HTTP 200), afficher les données JSON
    if http_code == 200:
      data = response.json()
    else:
        data = {"error": f"Aucune donnée valide n'a été retournée pour l'ID \"{id}\"."}

    return render_template("pages/retrieve_wikidata.html", http_code = http_code, media_type=media_type, encoding = encoding, data=data)