from random import sample, choice

def currencycodes():
    ''' 
    Opens file currency codes that has all exsisting currency codes 
    puts all currency codes into an array 
    
     '''
    ccodes = []
    with open("currencycode.txt") as file:
        for line in file:
            line = line.strip()
            if line:
                ccodes.append(line)
        return ccodes


def currencysymbols():
    '''
    Opens file currencysymbol that has all exsisting currency symbols
    puts all currency symbols into an array 
    '''
    csymbols = []
    with open("currencysymbol.txt") as file:
        for line in file:
            line = line.strip()
            if line:
                csymbols.append(line)
        
        return csymbols


''' Makes csymbols and ccodes array into a dictionary with the key being currency code & symbols being the value'''
currency = {  code: symbol for code, symbol in zip(currencycodes(), currencysymbols() )}




def checkcurrency(currency_code):
    '''checks if entered currency code is an actual currency code'''
    currency_code = currency_code.upper()
    if currency_code in currency:
        return True
    else:
        return False


def get_symbol(currency_code):
    currency_code = currency_code.upper()
    ''' Check if currency code is valid, if so find the corresponding symbol for it in the currency dictionary'''
    if checkcurrency(currency_code) == True:
        return currency[currency_code]
    else:
        return "not a valid currency!"


def randomcurrency():
    ''' return a string of 4 diffrent random currency codes '''
    if len(currencycodes()) >= 4:
     return " , ".join([code for code in sample(currencycodes(), 4)])
    else: 
        return " ".join(choice(currencycodes()))

