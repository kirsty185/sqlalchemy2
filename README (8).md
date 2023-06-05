# sqlalchemy-challenge

Part 1: Analyse and Explore the Climate Data
I used Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. 
4. Link Python to the database by creating a SQLAlchemy session.
5. Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

Precipitation Analysis
1. Find the most recent date in the dataset.
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Select only the "date" and "prcp" values.
4.Load the query results into a Pandas DataFrame. Explicitly set the column names.
5.Sort the DataFrame values by "date".
6.Plot the results by using the DataFrame plot method, as the following image shows a bar graph
7. Use Pandas to print the summary statistics for the precipitation data.

Station Analysis
1. Design a query to calculate the total number of stations in the dataset.
2. Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:
a.  List the stations and observation counts in descending order.
b. Answer the following question: which station id has the greatest number of observations?
c. Using the most-active station id, calculate the lowest, highest, and average temperatures.

3. Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
a. Filter by the station that has the greatest number of observations.
b. Query the previous 12 months of TOBS data for that station.
c. Plot the results as a histogram with bins=12, as the following image shows a histogram

Part 2: Design Your Climate App
I struggled with this part and required assistance via tutors and research. 
