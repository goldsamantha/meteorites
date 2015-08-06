"""
Takes init data and parses to JSON with only relevant information including
location, mass, year, longitude, and latitude of fallen meteorites.

    Samantha Goldstein, 2015
"""

import csv
import json
def main():



    fl = open('data/meteoritessize.csv', 'r')
    # You can use this sample csv if you would like to edit!
    # fl = open('data/sample.csv', 'r')
    reader = csv.reader(fl)
    lns = []

    inum = 0

    d = {}
    for ln in reader:
      if (inum != 0):
        if (ln[3]=='Fell'):
          new_ln = [ln[0], ln[2].replace(',',''), ln[4], ln[6], ln[7] ]
          if float(new_ln[1]) > 0 and new_ln[2].isdigit():
              #Set first date
              if (int(new_ln[2])< 1200):
                  continue
              node = { 'location': new_ln[0], 'mass': new_ln[1], 'year': new_ln[2], 'lat': new_ln[3], 'long': new_ln[4]}
              if d.has_key(new_ln[2]):
                  d[new_ln[2]].append(node)
              else:
                  d[new_ln[2]] = [node]
      inum +=1



    init_kys = d.keys()

    kys = []
    [kys.append(int(init_kys[i])) for i in range(len(init_kys))]
    kys.sort()


    start = int(kys[0])
    end = int(kys[-1])
    diff = end - start
    print "Start:", start, "End: ", end, "Diff: ", (end-start)

    for i in range(diff):
        date = str(start+i)
        print date
        if d.has_key(date) == False:
            # Fill in with 'false positives', essentially we need to make sure there is at least one node of each date
            # in our data.
            #Sikhote-Alin,23000000,1947,46.16,134.65333
            node = { 'location': 'Sikhote-Alin' , 'mass': '0', 'year': date, 'lat': '46.16', 'long': '134.65333' }
            d[date] = [node]
            print d[date]



    with open('data/parsed.json', 'w') as outfile:
      json.dump(d, outfile)










main()
