import os
import csv

progs=open('brain/knowledge/programs_x86.csv','r')
reader=csv.reader(progs)
rows=[]
for row in reader:
    if(row!=[]):
        rows.append(row[0])
progs.close()
progs=open('brain/knowledge/programs.csv','r')
reader=csv.reader(progs)
for row in reader:
    if(row!=[]):
        rows.append(row[0])
progs.close()
def open_it(input):
    if 'explorer' in input:
        os.popen('explorer')
        return 1
    open_add=input+'.exe'
    for i in rows:
        try:
            if input in i.lower():
                open_ad=i+'\\'+open_add
                #print('opening '+open_ad)
                os.startfile(open_ad)
                return 1
            
        except:
            continue
    return 0
    
    
