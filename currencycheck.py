from random import sample, choice

def currencycodes():
   
    ccodes = []
    with open("currencycode.txt") as file:
        for line in file:
            line = line.strip()
            if line:
                ccodes.append(line)
        return ccodes


def currencysymbols():
   
    csymbols = []
    with open("currencysymbol.txt") as file:
        for line in file:
            line = line.strip()
            if line:
                csymbols.append(line)
        
        return csymbols



currency = {  code: symbol for code, symbol in zip(currencycodes(), currencysymbols() )}




def checkcurrency(currency_code):
    currency_code = currency_code.upper()
    if currency_code in currency:
        return True
    else:
        return False


def get_symbol(currency_code):
    currency_code = currency_code.upper()
    if checkcurrency(currency_code) == True:
        return currency[currency_code]
    else:
        return "not a valid currency!"


def randomcurrency():
    if len(currencycodes()) >= 4:
     return " , ".join([code for code in sample(currencycodes(), 4)])
    else: 
        return " ".join(choice(currencycodes()))

