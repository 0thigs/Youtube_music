from pathlib import Path
from random import randint
from uuid import uuid4

from flask import Flask, request, render_template
import mysql.connector

config = {
    'host': 'database',
    'port': 3306,
    'user': 'thigs',
    'password': 'root',
    'database': 'youtube',
}

database = mysql.connector.connect(**config)
cursor = database.cursor(dictionary=True)

template_dir = "./src/templates"
static_dir = "./src/static"

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/', methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        print(request.form, flush=True)

        img_music = request.files.get("img_music")
        print(img_music, flush=True)

        image_name = f"{uuid4()}.jpg"
        image_path = Path().absolute() / "src" / "static" / "uploads" / image_name

        img_music.save(image_path)

        title = request.form.get("title")
        description = request.form.get("description")
        url_music = request.form.get("url_music")

        query = f"INSERT INTO post(titulo, description ,musicurl, musicimage) VALUES ('{title}', '{description}' ,'{url_music}', '{image_name}')"
        cursor.execute(query)
        database.commit()

    get_query = f"SELECT * FROM post"
    cursor.execute(get_query)
    musics = cursor.fetchall()

    print(musics)

    return render_template('homepage.html', musics=musics)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
        