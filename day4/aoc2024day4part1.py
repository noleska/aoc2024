import pandas as pd

df = pd.read_fwf(r'./input.txt', widths=[1 for x in range(0,140)], header = None)
search_key = "XMAS"
margin = len(search_key) - 1
nbound = 0
ebound = len(df.columns)
sbound = len(df)
wbound = 0

pts_for_dir = {'n' : [{'x' : -i, 'y' :  0} for i in range(len(search_key))],
               'ne': [{'x' : -i, 'y' :  i} for i in range(len(search_key))],
               'e' : [{'x' : 0 , 'y' :  i} for i in range(len(search_key))],
               'se': [{'x' : i , 'y' :  i} for i in range(len(search_key))],
               's' : [{'x' : i , 'y' :  0} for i in range(len(search_key))],
               'sw': [{'x' : i , 'y' : -i} for i in range(len(search_key))],
               'w' : [{'x' : 0 , 'y' : -i} for i in range(len(search_key))],
               'nw': [{'x' : -i, 'y' : -i} for i in range(len(search_key))]}


def search_on_point(x, y):
    xorigin = x
    yorigin = y
    clear = {'n' : xorigin >= nbound + margin,
             'e' : yorigin < ebound - margin,
             's' : xorigin < sbound - margin,
             'w' : yorigin >= wbound + margin,}
    clear.update({'ne' : clear['n'] and clear['e'],
                       'se' : clear['s'] and clear['e'], 
                       'sw' : clear['s'] and clear['w'],
                       'nw' : clear['n'] and clear['w']})
    num_matches = 0

    for dir in clear.keys():
      if clear[dir]:
        search_txt = ""
        for offset in pts_for_dir[dir]:
          search_txt += df.iloc[xorigin+offset['x'], yorigin+offset['y']]
          if search_txt == search_key:
            num_matches += 1
    
    return num_matches


tot_matches = 0
for row in range(0,len(df)):
  for col in range(0,len(df.columns)):
    tot_matches += search_on_point(row, col)
print(tot_matches)

