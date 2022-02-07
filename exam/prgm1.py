import csv
import pandas

mydict=[{'name':'hamna','mfc':'50','dc':'20','ds':'50','ase':'68'},
        {'name':'nihal','mfc':'45','dc':'60','ds':'45','ase':'89'},
        {'name':'henna','mfc':'89','dc':'20','ds':'89','ase':'68'},
        {'name':'rahana','mfc':'54','dc':'65','ds':'40','ase':'86'},
        {'name':'roshan','mfc':'80','dc':'20','ds':'40','ase':'96'},
        {'name':'safa','mfc':'50','dc':'24','ds':'56','ase':'96'},
        {'name':'rayees','mfc':'50','dc':'24','ds':'50','ase':'97'},
        {'name':'ehan','mfc':'50','dc':'24','ds':'50','ase':'97'},
        {'name':'jil','mfc':'50','dc':'24','ds':'50','ase':'97'},
        {'name':'fath','mfc':'50','dc':'24','ds':'50','ase':'97'}]
        
       
        

fields=['name','mfc','dc','ds','ase']

with open('details.csv','r+') as new_csvfile:

    writer = csv.DictWriter(new_csvfile,fieldnames=fields)

    writer.writeheader()

    writer.writerows(mydict)

    new_csvfile.close()

mfc=0
dc=0
ase=0
ds=0
with open('details.csv','r') as csfiles:
     reader = csv.DictReader(csfiles)
     for row in reader:
         print(row['name'],":",(int(int(row['mfc'])+int(row['dc'])+int(row['ds'])+int(row['ase']))/400)*100)
         mfc=mfc+int(row['mfc'])
         dc=dc+int(row['dc'])
         ase=ase+int(row['ase'])
         ds=ds+int(row['ds'])
print("\n\nAverage")
print("mfc",mfc/10)
print("dc",dc/10)
print("ds",ds/10)
print("ase",ase/10)
