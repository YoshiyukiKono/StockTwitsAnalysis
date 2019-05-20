import subprocess
args = ['curl', '-X', 'GET', 'https://api.stocktwits.com/api/2/streams/symbol/AAPL.json']
try:
    res = subprocess.check_call(args)
except:
    print "Error."
