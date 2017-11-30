
# coding: utf-8

# This is an attempt at using Python to create a source file for MongoDB.

# The csv file used in this example was downloaded from https://github.com/datasets/airport-codes.  The program does the following:
#         
#         It loads the csv file into the dataframe df.
#         It extracts the Country, City, Timezone and DST attributes from the full dataset into a dataframe called City; these attributes will
#		  repeat and are the same fo each city in the set, so it drops duplicates and then sorths them in ascending order by Country, City, Timezone 
#		  and DST.
#         Then it defines a function writeafile that first writes 'use aviation' to the json file.  This tells the file which database to use.
#         It then iterates through a set of City rows, converts them to json format and embeds an array of airports for the city into the json record.
#         It renames the array from the standard '0' to 'Airports'.  It embeds the json into a mongoDB insert statement and writes it to the file.
#         
#         The program splits the dataset into 1,000 row chunks, and writes each chunk to a file.  This is to prevent memory errors.
#         
import pandas as pd
df = pd.read_csv('data/sightings.csv', sep = ',', 
                 delimiter = None,encoding='latin-1')
ufo = df[['City','State']]\
.drop_duplicates()\
.sort_values(['City','State'], ascending = [True,True])

def writeafile(filename):
    file = open(filename,'w') 
    print('Opening ', filename)
    rec = 'use sightings\n\n'
    file.write(rec)
    for r, s,  in thisfile[['City','State']].itertuples(index=False):
        tc = (df[(df['City']==r) & (df['State']==s)])
        j = (tc.groupby(['City','State'], as_index=False)
        .apply(lambda x: x[['Date / Time','Shape','Duration','Summary','Posted']]
               .to_dict('r'))
             .reset_index()
             .rename(columns={0:'Ufo'})
             .to_json(orient='records'))
        rec = 'db.ufos.insert(' + j + ')\n'
        file.write(rec)
    file.close()
    print('Closing ', filename)
    return()

count = 1
countmax = round(len(ufo)+.5)/1000

filename = 'data/ufos.js'

thisfile = ufo[:len(ufo)-1]
print(thisfile.head())
print ('The count is:', count)
b = writeafile(filename)
   

print ("Finished - GoodBye!")


