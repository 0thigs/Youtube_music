from flask import Flask, render_template

template_dir = "./src/templates"
static_dir = "./src/static"

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def homepage():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True)
        