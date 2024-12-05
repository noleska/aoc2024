import pandas as pd

df = pd.read_fwf(r'./input.txt', widths=[1 for x in range(0,140)], header = None)
search_key = "XMAS"
rlsk   = range(len(search_key)
margin = len(search_key) - 1
nbound = 0
ebound = len(df.columns)
sbound = len(df)
wbound = 0

pts_for_dir = {'n' : [{'x' : -i, 'y' :  0} for i in rlsk],
               'ne': [{'x' : -i, 'y' :  i} for i in rlsk],
               'e' : [{'x' :  0, 'y' :  i} for i in rlsk],
               'se': [{'x' :  i, 'y' :  i} for i in rlsk],
               's' : [{'x' :  i, 'y' :  0} for i in rlsk],
               'sw': [{'x' :  i, 'y' : -i} for i in rlsk],
               'w' : [{'x' :  0, 'y' : -i} for i in rlsk],
               'nw': [{'x' : -i, 'y' : -i} for i in rlsk]}


class search_point:
  def __init__(self, x, y):
    self.xorigin = x
    self.yorigin = y
    self.clear = {'n' : self.xorigin >= nbound + margin,
                  'e' : self.yorigin <  ebound - margin,
                  's' : self.xorigin <  sbound - margin,
                  'w' : self.yorigin >= wbound + margin,}
    self.clear.update({'ne' : self.clear['n'] and self.clear['e'],
                       'se' : self.clear['s'] and self.clear['e'], 
                       'sw' : self.clear['s'] and self.clear['w'],
                       'nw' : self.clear['n'] and self.clear['w']})
    self.num_matches = 0

    for dir in self.clear.keys():
      if self.clear[dir]:
        search_txt = ""
        for offset in pts_for_dir[dir]:
          search_txt += df.iloc[self.xorigin+offset['x'],self.yorigin+offset['y']]
          if search_txt == search_key:
            self.num_matches += 1


tot_matches = 0
for row in range(0,len(df)):
  for col in range(0,len(df.columns)):
    tot_matches += search_point(row, col).num_matches
print(tot_matches)
