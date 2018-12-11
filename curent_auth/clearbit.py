import clearbit

clearbit.key = '212c6193c089b2ce94e194efe19d36e9'
try:
    from starnavi.settings import CLEARBIT_CHECK
except:
    CLEARBIT_CHECK = False

def clearbitCheck(username):
    if CLEARBIT_CHECK:
        try:
            response = clearbit.Enrichment.find(email=username, stream=True)
        except:
            return False
        if response is None:
            raise ValueError('Invalid response from clerbit')
        if response['person'] is None:
            return False
    return True
