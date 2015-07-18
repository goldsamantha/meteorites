"""
Takes init data and parses to JSON with only relevant information including
location, mass, year, longitude, and latitude of fallen meteorites. 

    Samantha Goldstein, 2015
"""

import csv
import json
def main():



    fl = open('data/meteoritessize.csv', 'r')
    reader = csv.reader(fl)
    lns = []

    inum = 0

    d = {}
    for ln in reader:
      if (inum != 0):
        if (ln[3]=='Fell'):
          new_ln = [ln[0], ln[2].replace(',',''), ln[4], ln[6], ln[7] ]
          if float(new_ln[1]) > 0:
              print new_ln
              node = { 'location': new_ln[0], 'mass': new_ln[1], 'year': new_ln[2], 'lat': new_ln[3], 'long': new_ln[4]}
              if d.has_key(new_ln[2]):
                  d[new_ln[2]].append(node)
              else:
                  d[new_ln[2]] = [node]
      inum +=1



    with open('data/parsed_sample.json', 'w') as outfile:
      json.dump(d, outfile)










main()
