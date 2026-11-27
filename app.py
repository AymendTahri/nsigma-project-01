import os
from flask import Flask, render_template , request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
import crud

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")
@app.route("/annonces/nouvelle", methods=["GET", "POST"])
def creer_annonce():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        title = request.form.get("title")
        city = request.form.get("city")
        price = request.form.get("price")
        description = request.form.get("description")

        image_filename = "default.jpg"
        file = request.files.get("image")
        if file and file.filename:
            image_filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], image_filename))

        try:
            crud.create_annonce(
                user_id=session["user_id"],
                title=title,
                city=city,
                price=price,
                description=description,
                image_filename=image_filename
            )
            return redirect(url_for("index"))
        except ValueError as e:
            flash(str(e))

    return render_template("form.html")


@app.route("/annonces/<int:annonce_id>/supprimer", methods=["POST"])
def supprimer_annonce(annonce_id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    crud.delete_annonce(annonce_id=annonce_id, user_id=session["user_id"])
    return redirect(url_for("index"))



if __name__ == "__main__":
  app.run(debug=True)
