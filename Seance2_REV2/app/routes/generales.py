from ..app import app

@app.route("/division/<nb1>/<nb2>")
def division (nb1, nb2):
    resultat = int(nb1)/int(nb2)
    return "Le résultat de la division de " + str(nb1) + " et " + str(nb2) + " est " + str(resultat) + "."





