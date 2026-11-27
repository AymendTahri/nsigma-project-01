from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/connexion", methods=["GET", "POST"])
def connexion():
  return render_template("connexion.html")

@app.route("/inscription", methods=["GET", "POST"])
def inscription():
  return render_template("inscription.html")

@app.route("/ajouter", methods=["GET", "POST"])
def ajouter():
  return render_template("ajouter.html")

@app.route("/profil")
def profil():
  return render_template("profil.html")

@app.route("/annonce/<int:annonce_id>/modifier", methods=["GET", "POST"])
def modifier_annonce(annonce_id):
    return render_template("modifier.html")

@app.route("/annonce/<int:annonce_id>")
def detail_annonce(annonce_id):
    return render_template("detail.html")

if __name__ == "__main__":
  app.run(debug=True)