from flask import Flask, render_template,request

app = Flask(__name__)

@app.get("/")
def showPage():
    return render_template('index.html')


@app.post('/analyze')
def analyze():
    text = request.form["text"]
    action = request.form["action"]
    answer = ""
    if(action=="cntchr"):
        #count the number of character
        answer = f"the number of characters are:-{len(text)}"
    if(action == "cntws"):
        #count the number of whitespaces
        answer = f"the number of white spaces are:-{text.count(' ')}"
    if(action =="ctuc"):
        #convert to upper case
        answer = f"the converted string is:-{text.upper()}"
    if(action == "ctlc"):
        #convert to lower case
        answer = f"the converted string is:-{text.lower()}"
    if(action =="csil"):
        #ckeck wether in lower case or not
        answer = f"the checked string is:-{text.islower()}"
    if(action =="csiu"):
        #check wether is in upper case or not
        answer = f"thw checked string is:-{text.isupper()}"
    if(action =="ctstc"):
        #capitalize
        answer = f"the capitalized string is:-{text.capitalize()}"
    return render_template('index.html', output = answer)



app.run(debug=True)