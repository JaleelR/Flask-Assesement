from flask import Flask, redirect, render_template,url_for, request, flash
from flask_debugtoolbar import DebugToolbarExtension
import requests 
from currencycheck import get_symbol, currencycodes, randomcurrency, checkcurrency



app = Flask(__name__)
app.config['SECRET_KEY'] = 'Naruto7'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def home():
 
    return render_template("mainpage.html")


@app.route("/convert", methods=["POST"])
def converter():
    cfrom = request.form.get("from") 
    if len(cfrom) != 3:
        flash("converting from: currency Codes must be 3 letters", "error")
        return redirect(url_for("home"))
    elif checkcurrency(cfrom) == False:
        flash(f"{cfrom} is not a valid currency, some examples of currency codes would be {randomcurrency()} " )
        return redirect('/')

    cto= request.form.get("to")
    if len(cto) != 3:
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
    
    url = 'https://api.exchangerate.host/convert?'
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
        flash(f"Converting {cfrom} to {cto} in the amount of {amt}, would be {symbol}{result}", "success")
        return redirect("/")
    else: 
        print("error response code " + responsejson.status_code)
        redirect('/')