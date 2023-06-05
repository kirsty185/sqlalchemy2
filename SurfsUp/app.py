# Part 2: Design the Climate App using Flask API


#Import dependencies and reflect database
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect Database into ORM classes

Base = automap_base()
Base.prepare(autoload_with=engine)

# View all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# 1. / 

#     Start at the homepage.
# Flask Setup

app = Flask(__name__)

#  List all the available routes.

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/2017-08-18<br/>"
        f"/api/v1.0/2010-01-01/2010-01-27<br/>"
    )
# 2. /api/v1.0/precipitation ##

#Convert the query results to a dictionary by using datae as the key and prcp as the valuefrom your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    """Return a list of all precipitation queries"""
    # Query
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    session.close()
#create dictionary
    percipitation_data = []
    for date,prcp in results:
        percipitation_data_dict = {}
        percipitation_data_dict["date"] = date
        percipitation_data_dict["prcp"] = prcp
        percipitation_data.append(percipitation_data_dict)

    return jsonify(percipitation_data)

 
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all stations"""
    # Query all stations
    results = session.query(Station.station).all()
    #Close session
    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def temperature():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Returns the temperature data of most active station for the last year in the database """

    # Perform a query to retrieve the data and temperature scores
   
    #retrieve the most active station
    sel = [Measurement.station,func.count(Measurement.station)]
    active_station = session.query(*sel).\
    group_by(Measurement.station).\
    order_by(func.count(Measurement.station).desc()).all()
    
    (most_active,totalcount) = active_station[0]
    
    #Retrieve the last date
    last_date = session.query(Measurement.date).filter(Measurement.station == most_active).order_by(Measurement.date.desc()).first()
    # Calculate the date one year from the last date in data set.
    query_date1 = dt.date(2017, 8, 18) - dt.timedelta(days=365)

    results = session.query(Measurement.date,Measurement.tobs).filter(Measurement.station == most_active , Measurement.date >= query_date1).all()

    #Close Session
    session.close()

    # Create a dictionary from the row data and append to a list of date and temperature data
    temperature_data = []
    for date,tobs in results:
        temperature_data_dict = {}
        temperature_data_dict["date"] = date
        temperature_data_dict["tobs"] = tobs
        temperature_data.append(temperature_data_dict)

    return jsonify(temperature_data)

@app.route("/api/v1.0/<start>")
def temp_startdate(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of the minimum temperature, the average temperature, 
       and the maximum temperature for a specified start date"""
    
    results = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()

    session.close()
    
    # Create a dictionary from the row data and append to min,amx and avg temp for the specified start date
    summary_data = []
    for tmin,tmax,tavg in results:
        summary_data_dict = {}
        summary_data_dict["Min"] = tmin
        summary_data_dict["Max"] = tmax
        summary_data_dict["Avg"] = tavg
        summary_data.append(summary_data_dict)

    return jsonify(summary_data)

@app.route("/api/v1.0/<start>/<end>")
def temp_startenddate(start,end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of the minimum temperature, the average temperature, 
       and the maximum temperature for a specified start date and end date."""
    
    results = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date >= start,Measurement.date <= end).all()
    session.close()
    
    # Create a dictionary from the row data and append to min,amx and avg temp for the specified start/end  date
    summary_data = []
    for tmin,tmax,tavg in results:
        summary_data_dict = {}
        summary_data_dict["Min"] = tmin
        summary_data_dict["Max"] = tmax
        summary_data_dict["Avg"] = tavg
        summary_data.append(summary_data_dict)

    return jsonify(summary_data)

if __name__ == "__main__":
    app.run(debug=True)