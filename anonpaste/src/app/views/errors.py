from django.shortcuts import render
from app import app
from flask import render_template

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.errorhandler(429)
def too_many_req(e):
    return render_template("429.html")


@app.errorhandler(500)
def internal_issue(e):
    return render_template("500.html")