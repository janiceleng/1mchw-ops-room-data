# coding: utf-8

#### DATA FRAMES ####

# Import packages
import pandas as pd

# Load original Qualtrics data
df = pd.read_csv('Community_Health_Worker_Dashboard_Lem 3.csv')

# Drop descriptive row
df=df.drop(df.index[[0]])

# Re-index the dataset because of deleted row
df=df.reset_index()

# Unstack df so that each service location can be exploited
df2 = df.unstack()

#### HEADERS ####

# Upload header renaming index
headers = pd.read_csv('qual-to-agol-pairing.csv')

# Define new column headers 
col_agol = list(headers['agol-header'])

# Define COMMON headers from original headers
col_qual = list(headers['qual-header'].dropna())

#### NEW DATAFRAME ####

# Create new dataframe
df3=pd.DataFrame(index=range(df.shape[0]), columns=col_agol)
df3

#### SERVICE LOCATIONS ####

# Upload array of service location headers
df_services = pd.read_csv('service-locations.csv')

# Define list of service headers 
services = df_services.values.T.tolist()
print services[1]

##### RESHAPING QUALTRICS OUTPUT ########

#Get number of rows in original df (aka number of total entries)
rg = range(df.shape[0])

# For each row
for r in rg:
    # For each potential service location in the data
    for s in services:
        # If service location in a row...
        if type(df2[s[0],r]) == str: #didn't know why is not None wasn't working 
            
            # Set values for service location (5)
            values = [df2[s[0],r], df2[s[1],r],df2[s[2],r], df2[s[3],r],df2[s[4],r]]
            
            # Now add common records for that row (40+ in total)
            for x in col_qual:
                values.append(df2[x,r])

            df3.loc[r] = pd.Series(values, index=col_agol)

#### FINAL OUTPUT ####

#Final output for ArcGIS online
df3
