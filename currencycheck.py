from random import sample

def currencycodes():
    file = open("currencycode.txt")
    ccodes = []
    for line in file:
        line = line.strip()
        if line:
            ccodes.append(line)
        file.close
    return ccodes


def currencysymbols():
    file = open("currencysymbol.txt")
    csymbols = []
    for line in file:
        line = line.strip()
        if line:
            csymbols.append(line)
        file.close
    return csymbols

currency = {  code: symbol for code, symbol in zip(currencycodes(), currencysymbols() )}

currency


def checkcurrency(currency_code):
    if currency_code in currency:
        return True
    else:
        return False

def get_symbol(currency_code):
    if checkcurrency(currency_code) == True:
        return currency[currency_code]
    else:
        return "not a valid currency!"


def randomcurrency():
     return " , ".join([code for code in sample(currencycodes(), 4)])

