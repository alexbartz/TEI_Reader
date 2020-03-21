from flask import render_template
from .app import app
from .fonctions import *

# lxml est la librairie permettant de traiter du XML en python
from lxml import etree


@app.route("/Accueil")
def accueil():
    return render_template("pages/Accueil.html", liste=corpus())


@app.route("/<document>/Table_des_matieres")
def table_matieres(document):
    doc = ouvrir_doc(document)
    return render_template("pages/Table_matieres.html", table=table_des_matieres(doc))


@app.route("/<document>/Index_lieux")
def index_des_lieux(document):
    doc = ouvrir_doc(document)
    return render_template("pages/Index_lieux.html", index=index_lieux(doc))


@app.route("/<document>/Index_personnages")
def index_des_personnages(document):
    doc = ouvrir_doc(document)
    return render_template("pages/Index_personnages.html", index=index_personnages(doc))


@app.route("/<document>/Presentation")
def presentation(document):
    doc = ouvrir_doc(document)
    return render_template("pages/Presentation.html", infos=presenter(doc))


@app.route("/<document>/Texte")
def Texte(document):
    xslt = etree.parse('TEI_Reader/XSLT_Appli.xsl')
    transform = etree.XSLT(xslt)
    doc = ouvrir_doc(document)
    return str(transform(doc))