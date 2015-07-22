# 1mchw-ops-room-data
Transforming qualtrics survey data for ArcGIS. The survey consists of a large side-by-side form to collect as much information about CHW service locations. However, all of this data gets stored in one row. This script unstacks each survey entry, then re-stacks the dataframe according to service location.

You can explore the code using our test dummy data set (test.csv and test.py)
