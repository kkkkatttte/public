from flask import Flask,request,redirect
import requests
app = Flask(__name__)
score=50
states1=[]
states = ['alabama', 'alaska','arizona','arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts','michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode island', 'south carolina' 'south dakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'west virginia', 'wisconsin', 'wyoming']
@app.route('/')
def index():
    return (
        '<h1> hello <a href="/start"> world </a> </h1> '
        )
@app.route('/start', methods=['GET','POST'])
def start():
    global score
    global states
    global states1
    if request.method=='POST':
        state=request.form.get('state')
        if state.lower() in states and state.lower() not in states1:
            states1.append(state)
            score-=1
        redirect('/start')
    return ('<h1 align="center"> Name 50 States </h1><br>'
            f'<h2>{score} states left</h2><br>'
            '<form method="POST" action="">'
            '<input type="text" name="state">'
            '<input type="submit">'
            '</form>')

#@app.route('/correct')

#@app.route('/incorrect')
#def incorrect():
print(__name__)

if __name__=='__main__':
    app.run(debug=True,port=5001,host='0.0.0.0')