from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index_ninja.html")

@app.route('/ninja')
def all_ninjas():
    return render_template("all_ninjas.html")

@app.route('/ninja/<color>')
def display(color):
    if color.lower() == "red":
        ninja = "Raphael"
        temp = "raphael.jpg"

    elif color.lower() == "blue":
        ninja = "Leonardo"
        temp = "leonardo.jpg"

    elif color.lower() == "purple":
        ninja = "Donatello"
        temp = "donatello.jpg"
    
    elif color.lower() == "orange":
        ninja = "Michelangelo"
        temp = "michelangelo.jpg"

    else:
        ninja = "Not a ninja!"
        temp = "notapril.jpg"
        
    return render_template('one_ninja.html', name=ninja, spec=temp)

app.run(debug=True)
    
