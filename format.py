import csv

def main():
    fl = open('meteoritessize.csv', 'r')
    output = open('output.csv', 'w')
    reader = csv.reader(fl)
    writer = csv.writer(output)
    newln = []

    inum = 0
    for ln in reader:
      if (inum != 0):
        if (ln[3]=='Fell'):
          #writer.writerow( [ln[0], int(ln[2].replace(',','')), ln[3], ln[4], ln[6], ln[7]] )
          writer.writerow( [ln[0], ln[2].replace(',',''), ln[4], ln[6], ln[7]] )
      inum +=1






main()
