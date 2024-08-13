from flask import Flask,request,redirect
import requests
app = Flask(__name__)
score=50
states1 = []
states = 'alabama_alaska_arizona_arkansas_california_colorado_connecticut_delaware_florida_georgia_hawaii_idaho_illinois_indiana_iowa_kansas_kentucky_louisiana_maine_maryland_massachusetts_michigan_minnesota_mississippi_missouri_montana_nebraska_nevada_new hampshire_new jersey_new mexico_new york_north carolina_north dakota_ohio_oklahoma_oregon_pennsylvania_rhode island_south carolina_south dakota_tennessee_texas_utah_vermont_virginia_washington_west virginia_wisconsin_wyoming'.split('_')
@app.route('/', methods=['GET','POST'])
def index():
    global score
    global states
    global states1
    if request.method=='POST':
        if score>1:
            state=request.form.get('state')
            if state.lower() in states and state.lower() not in states1:
                states1.append(state)
                score-=1
            return redirect('/')
        else:
            return redirect('/finish')
    return ('<h1 align = "center"> Name 50 States </h1><br>'
            f'<h2 align = "center">{score} states left</h2><br>'
            '<form align = "center" method = "POST" action = "">'
            '<input type = "text" name = "state">'
            '<input type = "submit">'
            '</form>'
            '<form align= "center" action="/start_over">'
            '<button> START OVER </button>'
            '</form><br><br><br><br><br><br><br><br><br><br><br>'
            '<div align= "center">'
            '<img src="https://t4.ftcdn.net/jpg/03/45/72/27/360_F_345722778_Iw2PEnOrYSidL3U3mSEMHrxHY0PO7U2G.jpg">'
            '</div>'
            )

@app.route('/start_over')
def start_over():
    global score
    score = 50
    global states1
    states1 = []
    return redirect('/')
@app.route('/finish')
def finish():
    return (
        '<h1 align= "center" > Thanks for playing! </h1><br><br>'
        #'<image align = "center" href='
        '<form align= "center" action="/start_over">'
        '<button> START OVER </button>'
        '</form><br><br>'
        '<div align= "center">'
        '<img src="https://static1.srcdn.com/wordpress/wp-content/uploads/2022/03/Ross-Geller.jpg" width=800>'
        '</div>'
    )


if __name__=='__main__':
    app.run(debug=True,port=5001,host='0.0.0.0')

