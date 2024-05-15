from flask import Flask, render_template
import mysql.connector

config = {
    'host': 'database',
    'port': 3306,
    'user': 'thigs',
    'password': 'root',
    'database': 'youtube',
}

database = mysql.connector.connect(**config)

template_dir = "./src/templates"
static_dir = "./src/static"

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def homepage():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
        