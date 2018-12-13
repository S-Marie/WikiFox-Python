# coding: utf-8
from pymongo import MongoClient
from pymongo import ReturnDocument
from pprint import pprint
from bson.objectid import ObjectId
from flask import Flask, request, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
import re


### Instructions :
# 1) Installer pymongo : pip install pymongo
# 2) Lancer le serveur mongod avec le CMD : mongod --dbpath [chemin de la base en URI] --port 27017
# 3) Lancer mongo dans le cmd : mongo --host localhost --port 27017
# 4) Dans mongo, creer la db MaBaseWiki : use MaBaseWiki
# 5) Lancer ce programme via le CMD en précisant bien : python TestPyMongo.py
###
env = Environment(
    loader=PackageLoader('Projet_Fil_Rouge', 'templates'),
    autoescape=select_autoescape(['html'])
)

app = Flask(__name__)
class MongoDBManagement :
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['MaBaseWiki']
        self.test = self.db['Articles']
    def RecupNom(self,r):
        r = '^'+r
        lnom = []        
        varAffiche = self.test.find({"nom":{'$regex':r}})
        for entry in varAffiche :
            lnom.append(entry.get('nom'))
        return lnom
    def RecupUrl(self,r):
        r = '^'+r
        lurl = []
        varAffiche = self.test.find({"nom":{'$regex':r}})
        for entry in varAffiche :
            lurl.append(entry.get('url'))
        return lurl

@app.route('/', methods=["POST","GET"])
def validate():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        nom = request.form['terme']
        rNom= mongoDB.RecupNom(nom)
        rUrl= mongoDB.RecupUrl(nom)
        template = env.get_template('index.html')
        return (template.render(lurl = rUrl, lnom = rNom))
    


if __name__ == '__main__' :
    mongoDB = MongoDBManagement()
    app.run(debug=True)

