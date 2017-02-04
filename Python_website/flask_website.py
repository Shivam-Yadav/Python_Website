__author__ = 'Shivam'
from flask import Flask, render_template #Flask is a class in flask module,
                                         # render_template accesses html file, stores in python files and displays on requested url

app=Flask(__name__)                        #__name__ is a special variable that will get name of the script
                                           #instantiating the object Flask

@app.route('/about/')   #url for localhost localhost:5000/about/in this case

def about():      #defines what ur website will do
    return render_template("about.html")

@app.route('/home/')
def home():      #defines what ur website will do
    return "dragon_emperor"

if __name__=="__main__":       #when python executes the scrpit, it changes  "__name__" to string "__main__",thus __name__=="__main__"
    app.run(debug=True)        #however, if we import the same script to another script, its name turns to name assigned,i.e "flask_webite.py" in this case
