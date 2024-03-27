from flask import Flask, session, render_template, redirect, url_for, request, flash
app = Flask('app')
app.secret_key = "portfoliowebsite"
import sqlite3

@app.route('/', methods=['GET', 'POST'])
def website():
  #sends to login template 
  if request.method == 'GET':
    return render_template("index.html")

app.run(host='0.0.0.0', port=8080)