import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify

#query_date = dt.date(2017, 8, 23) - dt.timedelta(days=364)


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
#Passenger = Base.classes.passenger

Measurement = Base.classes.measurement
Station = Base.classes.station
# Measurement2 = Base.classes.measurement
# Measurement3 = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)
session1 = Session(engine)
session2 = Session(engine)
session3 = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>"
    )

"/api/v1.0/('2012-02-28', '2012-03-05')"

@app.route("/api/v1.0/precipitation")

def dates():
    #session = Session(engine)
    """Return the average precip readings for dates ('2017-08-23') through ('2010-01-01')"""
    # Query all passengers
    #results = session.query(Passenger.name).all()
    results = session.query(Measurement.date, func.avg(Measurement.prcp)).\
    group_by(Measurement.date).all()


    # Convert list of tuples into normal list
    #all_dates = list(np.ravel(results))

    return jsonify(results)


@app.route("/api/v1.0/stations")
def stations():
   # session1 = Session(engine)
    """Return a list of weather stations"""
    # Query all passengers
    #results_station = session.query(Measurement.station).group_by(Measurement.station).all()
    results = session1.query(Station.station).distinct().all()
    
    return jsonify(results)
    

    # Create a dictionary from the row data and append to a list of all_passengers
#     all_stations = []
#     for station in results_station:
#         station_dict = {}
#         station_dict["station"] = station.station
#         all_stations.append(station_dict)
#     return jsonify(all_stations)



@app.route("/api/v1.0/tobs")
def tobs():
 #   session2 = Session(engine)
    """Return a list of temperature observations for the last year"""    
    tobs_results = session2.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= 2016-8-23).all()   
    return jsonify(tobs_results)

@app.route("/api/v1.0/<start>")
def start_time(start):
   # session3 = Session(engine)
    
    date_results = session3.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).\
    group_by(Measurement.date).all()
    
    return jsonify(date_results)

#func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)


#session.query(*sel).filter(func.strftime("%m-%d", Measurement.date) == date).all()


# @app.route("/api/v1.0/<start>")
# def start_date(start):
#     dates = session.query(Measurement.date, Measurement.tobs).all()
#     for date in dates:
#         if session.query(Measurement.date) > "start"
#     return jsonify(date)
   


# @app.route("/api/v1.0/passengers")
# def passengers():
#     results = session.query(Passenger).all()

#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_passengers = []
#     for passenger in results:
#         passenger_dict = {}
#         passenger_dict["name"] = passenger.name
#         passenger_dict["age"] = passenger.age
#         passenger_dict["sex"] = passenger.sex
#         all_passengers.append(passenger_dict)

#     return jsonify(all_passengers)
    
    
    
#     start_results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= ["start"]).all()   
#     return jsonify(start_results)
    
    
#     canonicalized = superhero.replace(" ", "").lower()
#     for character in justice_league_members:
#         search_term = character["superhero"].replace(" ", "").lower()

#         if search_term == canonicalized:
#             return jsonify(character)
    





# def calc_temps(start_date, end_date):
#     for time in session.query(Measurement.date):
#         search_term = character["superhero"].replace(" ", "").lower()

#         if search_term == canonicalized:
#             return jsonify(character)
        
        
        
#     for time in session.query(Measurement.date):
        
    
#     return jsonify(session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
#         filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all())



# function usage example
#print(calc_temps('2012-02-28', '2012-03-05'))
   
    
#         for character in justice_league_members:
#         if character[key] == value:
#             return jsonify(character)


if __name__ == '__main__':
    app.run(debug=True)
