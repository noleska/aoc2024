import pandas as pd


df = pd.read_fwf(r'./input.txt', widths=[1 for x in range(0,140)], header = None)

search_key = "XMAS"
margin = len(search_key) - 1
nbound = 0
ebound = len(df.columns)
sbound = len(df)
wbound = 0

pts_for_dir = {'n' : [],
               'ne': [],
               'e' : [],
               'se': [],
               's' : [],
               'sw': [],
               'w' : [],
               'nw': []}

for i in range(len(search_key)):
  pts_for_dir['n' ].append({'x' : -i, 'y' : 0 })
  pts_for_dir['ne'].append({'x' : -i, 'y' : i })
  pts_for_dir['e' ].append({'x' : 0 , 'y' : i })
  pts_for_dir['se'].append({'x' : i , 'y' : i })
  pts_for_dir['s' ].append({'x' : i , 'y' : 0 })
  pts_for_dir['sw'].append({'x' : i , 'y' : -i})
  pts_for_dir['w' ].append({'x' : 0 , 'y' : -i})
  pts_for_dir['nw'].append({'x' : -i, 'y' : -i})


class search_point:
  def __init__(self, x, y):
    self.xorigin = x
    self.yorigin = y
    self.clear = {'n' : self.xorigin >= nbound + margin,
                  'e' : self.yorigin <  ebound - margin,
                  's' : self.xorigin <  sbound - margin,
                  'w' : self.yorigin >= wbound + margin,
                  'ne': self.xorigin >= nbound + margin and self.yorigin <  ebound - margin,
                  'se': self.xorigin <  sbound - margin and self.yorigin <  ebound - margin,
                  'sw': self.xorigin <  sbound - margin and self.yorigin >= wbound + margin,
                  'nw': self.xorigin >= nbound + margin and self.yorigin >= wbound + margin}
    self.num_matches = 0

    for dir in self.clear.keys():
      if self.clear[dir]:
        search_txt = ""
        for offset in pts_for_dir[dir]:
          search_txt += df.iloc[self.xorigin + offset['x'], self.yorigin + offset['y']]
        if search_txt == search_key:
          self.num_matches += 1

tot_matches = 0
for row in range(0,len(df)):
  for col in range(0,len(df.columns)):
    if df.iloc[row, col] == search_key[0]:
      tot_matches += search_point(row, col).num_matches
print("Part 1:", tot_matches)
