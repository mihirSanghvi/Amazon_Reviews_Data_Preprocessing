import pandas as pd
import gzip

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    print d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

fullMetaElectronics = getDF("C:\\Users\\USER\\Downloads\\meta_Electronics.json.gz")

metaElectronics = fullMetaElectronics['asin','price','salesRank','title','imUrl']

metaElectronics.to_csv("C:\\Users\USER\\Downloads\\meta_Electronics.csv",index = False)
