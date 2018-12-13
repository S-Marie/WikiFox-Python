from flask import Flask,request,render_template

app = Flask(__name__)


@app.route('/', methods=["POST","GET"])
def validate():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":

        nom = request.form['terme']
    #couleur = flask.request.form['couleur']
    #Age = flask.request.form['Age']

        data = nom#, couleur, Age

        print (data)

        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)