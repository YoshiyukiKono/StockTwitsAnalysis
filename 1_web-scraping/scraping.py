import subprocess

symbols = ['BBRY', 'AAPL', 'AMZN', 'BABA', 'YHOO', 'LQMT', 'FB', 'GOOG', 'BBBY', 'JNUG', 'SBUX', 'MU']

args = ['curl', '-X', 'GET', '']
URL = "https://api.stocktwits.com/api/2/streams/symbol/"

FILE_PATH = "./data/"

for symbol in symbols:
  try:
    args[3] = URL + symbol + ".json"
    print(args[3])
    proc = subprocess.run(args,stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    
    path = FILE_PATH + symbol + ".json"
    
    with open(path, mode='w') as f:
      f.write(proc.stdout.decode("utf8"))
  
  except:
    print("Error.")
