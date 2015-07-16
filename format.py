import csv
import json
def main():


    # with open('data.txt', 'w') as outfile:
    #   json.dump(data, outfile)
    # fl = open('meteoritessize.csv', 'r')
    # output = open('output.csv', 'w')

    # PARSED HEADER:
    # location,mass,year,lat,long

    fl = open('meteoritessize.csv', 'r')
    # output = open('parsed_sample.json', 'w')
    reader = csv.reader(fl)
    # writer = csv.writer(output)
    lns = []

    inum = 0

    d = {}
    for ln in reader:
      if (inum != 0):
        if (ln[3]=='Fell'):
          #writer.writerow( [ln[0], int(ln[2].replace(',','')), ln[3], ln[4], ln[6], ln[7]] )
          new_ln = [ln[0], ln[2].replace(',',''), ln[4], ln[6], ln[7] ]
          if float(new_ln[1]) > 0:
              print new_ln
              node = { 'location': new_ln[0], 'mass': new_ln[1], 'year': new_ln[2], 'lat': new_ln[3], 'long': new_ln[4]}
              if d.has_key(new_ln[2]):
                  d[new_ln[2]].append(node) #new_ln)
              else:
                  d[new_ln[2]] = [node] #[new_ln]
          #TODO: keep below line, move
          #writer.writerow( [ln[0], ln[2].replace(',',''), ln[4], ln[6], ln[7]] )
      inum +=1



    with open('parsed_sample.json', 'w') as outfile:
      json.dump(d, outfile)

    # lns.sort(key=lambda x:x[2])









main()
