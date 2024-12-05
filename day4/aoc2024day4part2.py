import pandas as pd

df = pd.read_fwf(r'./input.txt', widths=[1 for x in range(0,140)], header = None)

exmas_count = 0
for row in range(1,len(df)-1):
  for c in range(1,len(df.iloc[row])-1):
    if df.iloc[row,c] == "A":
      subdf = pd.DataFrame(df.iloc[row-1:row+2, c-1:c+2])
      subdf = subdf.reset_index(drop=True)
      x1 = ""
      x1 += str(subdf.iloc[0,0]) + str(subdf.iloc[2,2])
      x2 = ""
      x2 += str(subdf.iloc[2,0]) + str(subdf.iloc[0,2])
      if (x1 == "MS" or x1 == "SM") and (x2 == "MS" or x2 == "SM"):
        exmas_count += 1

print(exmas_count)
