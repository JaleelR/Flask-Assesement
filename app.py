from flask import Flask, redirect, render_template,url_for, request, flash
from flask_debugtoolbar import DebugToolbarExtension
import requests 
from currencycheck import get_symbol, currencycodes, randomcurrency, checkcurrency



app = Flask(__name__)
app.config['SECRET_KEY'] = 'Naruto7'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


@app.route('/')
def home():
    """ home page """
    return render_template("mainpage.html")


@app.route("/convert", methods=["POST"])
def converter():
    """
    -Gets form data from "converting from" "converting to" & "amount"
    -Checks if there is no form data entered, if the letters amount of letters is 3 and if its a valid currency
    -checks and turns amount value into a float, if it can't turn into a float provide a response to make value a number
    """
    cfrom = request.form.get("from") 
    if cfrom is None:
        flash(f"Please provide us with a currency code such as {randomcurrency()}", "error" ) 
        return redirect('/')
    elif len(cfrom) != 3:
        flash("converting from: currency Codes must be 3 letters", "error")
        return redirect(url_for("home"))
    elif checkcurrency(cfrom) == False:
        flash(f"{cfrom} is not a valid currency, some examples of currency codes would be {randomcurrency()} " )
        return redirect('/')
   

    cto= request.form.get("to")
    if cto is None:
        flash(f"Please provide us with a currency code such as {randomcurrency()}", "error" )
        return redirect('/')
    elif len(cto) != 3:
        flash("converting to: currency Code must be 3 letters", "error")
        return redirect('/')
    elif checkcurrency(cto) == False:
        flash(f"{cto} is not a valid currency, some examples of currency codes would be {randomcurrency()} " )
        return redirect('/')
   
    amt = request.form.get("amount")
    try:
        amt = float(amt)
    except ValueError:
        flash("Amount must be a number", "error")
        return redirect(url_for("home"))
    

    '''
    - Sends data from inputs to api to convert
    - checks if the status code is 200 if so...
        cont. - turn response into json so it is readable 
        cont. - Get the result of the conversion from: cfrom and cto varibles
        cont. - Get symbol for currespoding currency code (cto)
    - if status code isn't 200 print a response with the current status code 
    '''
    url = 'https://api.exchangerate.host/convert'
    params = { 
        "from": cfrom,
        "to": cto,
        "amount": amt,
        "places": 2,
        "symbols": currencycodes()
    }


    response = requests.get(url, params=params)
    if response.status_code == 200:
        responsejson = response.json()
        result = responsejson["result"]
        symbol  =  get_symbol(cto)
        flash(f"Converting {cfrom.upper()} to {cto.upper()} in the amount of {amt}, would be {symbol}{result}", "success")
        return redirect("/")
    else: 
        print("error response code " + responsejson.status_code)
        redirect('/')