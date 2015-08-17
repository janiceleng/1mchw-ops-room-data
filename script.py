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

# Get number of rows in uploaded csv
rg = range(df.shape[0])

# Keep track of new rows
i = 0

# For each row
for r in rg:
    
    #For each potential service location
    for s in services:

        if type(df[s[0]][r]) == str:

            #set values for service location (5 total in final)
            values = [df[s[0]][r], df[s[1]][r], df[s[2]][r], df[s[3]][r], df[s[4]][r]]

            #Now add common records for that row (40+ in total)
            for x in col_qual:

                #Manually correct the Mobile Health Usage column (MH_Usage)
                if x == "Q20":
                    #Change the 2 to 0 ("No")
                    if df[x][r] == 2:
                        values.append(df[x][r] - 2)
                    #1 will remain as 1 ("Yes")
                    else:
                        values.append(df[x][r])
                else:
                    values.append(df[x][r])
            
            #Populate the new dataframe
            df3.loc[i] = pd.Series(values, index=col_agol)
            i+=1
            
#### FINAL OUTPUT ####

#Final output for ArcGIS online
df3.to_csv('final.csv')
df3
