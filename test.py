#### DATA FRAMES ####

# Import packages
import pandas as pd

# Load original Qualtrics data
df = pd.read_csv('test.csv')

# Unstack df so that each service location can be exploited
df2 = df.unstack()


#### HEADERS ####

# Define new column headers 
columns = ['A','B','C','D']

df3=pd.DataFrame(index=range(df.shape[0]), columns=columns)


##### RESHAPING QUALTRICS OUTPUT ########

# List of COMMON columns from original 
columns = ('a','b')

# List of SERVICE-SPECIFIC columns
services = (['c','d'],['e','f'])

# Get number of rows in uploaded csv
rg = range(df.shape[0])

# For each row
for r in rg:

    # For each potential service location
    for s in services:
        
        print df2[s[0],r]
        # If service location in a row...
        if type(df2[s[0],r]) == str: #didn't know why is not None wasn't working
                        
            # Set values for service location 
            values = [df2[s[0],r], df2[s[1],r]]
            
            # Now add common records for that row 
            for x in columns:
                values.append(df2[x,r])
            df3.loc[r] = pd.Series(values, index=['A','B','C','D'])


#### FINAL OUTPUT ####

#Final output for ArcGIS Online
df3
