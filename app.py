import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import MetaData,Table,inspect

import psycopg2

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:postgres@@127.0.0.1/inc5000"
db = SQLAlchemy(app)


metadata = MetaData(bind=db.engine) 
inc2018_data = Table('inc2018_data', metadata, autoload_with=db.engine) 


#session = Session(db.engine)
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
Inc2018_data = Base.classes.inc2018_data

# Select All
sel_all = [ 
        Inc2018_data.rank,
        Inc2018_data.url,
        Inc2018_data.growth,
        Inc2018_data.industry,
        Inc2018_data.revenue,
        Inc2018_data.state_l,
        Inc2018_data.state_s,
        Inc2018_data.city,
        Inc2018_data.founded,
        Inc2018_data.latitude,
        Inc2018_data.longitude,
        Inc2018_data.yrs_on_list,
        Inc2018_data.company,
        Inc2018_data.website,
        Inc2018_data.workers,
        ]

def build_metadata_list(inc_jsondata_list,results):
    
    inc_jsondata={}
    for result in results:
        inc_jsondata['rank'] = result[0]
        inc_jsondata['url'] = result[1]
        inc_jsondata['growth'] = result[2]
        inc_jsondata['industry'] = result[3]
        inc_jsondata['revenue'] = result[4]
        inc_jsondata['state_l'] = result[5]
        inc_jsondata['state_s'] = result[6]
        inc_jsondata['city'] = result[7]
        inc_jsondata['founded'] = result[8]
        inc_jsondata['latitude'] = result[9]
        inc_jsondata['longtitude'] = result[10]
        inc_jsondata['yrs_on_list'] = result[11]
        inc_jsondata['company'] = result[12]
        inc_jsondata['website'] = result[13]
        inc_jsondata['workers'] = result[14]
        inc_jsondata_list.append([inc_jsondata])
        inc_jsondata={}
    return inc_jsondata_list

@app.route("/")
def index():
    return render_template("index.html")




@app.route("/2018metadata")
def metadata():
 #   """Return the homepage."""
 #   return render_template("index.html")
    

# Use Pandas to perform the sql query
    results = db.session.query(*sel_all).all()
    inc_jsondata_list = []
    results_list = build_metadata_list(inc_jsondata_list,results)
    # Return a list of the column names (sample names)
    return jsonify(results_list)


@app.route("/rank/<ranking_number>")
def ranking(ranking_number):
    """Return a list of Ranking # Company Information."""
    num = int(ranking_number)
    results = db.session.query(*sel_all).filter(Inc2018_data.rank == num).all() 
    inc_jsondata_list = []

    results_list = build_metadata_list(inc_jsondata_list,results)
    
    return jsonify(results_list)


@app.route("/state_s/<state_s>")
def state_s_query(state_s):
    """Return a list of Ranking # Company Information."""
    state_s = state_s.upper()
    results = db.session.query(*sel_all).filter(Inc2018_data.state_s == state_s).all() 
    inc_jsondata_list = []

    results_list = build_metadata_list(inc_jsondata_list,results)
    
    return jsonify(results_list)

@app.route("/years_on/<yrs_on_list>")
def yrs_on_list_query(yrs_on_list):
    """Return a list of Ranking # Company Information."""
    yrs_on_list = int(yrs_on_list)
    results = db.session.query(*sel_all).filter(Inc2018_data.yrs_on_list == yrs_on_list).all() 
    inc_jsondata_list = []

    results_list = build_metadata_list(inc_jsondata_list,results)
    
    return jsonify(results_list)

@app.route("/founded_year/<founded>")
def founded_query(founded):
    """Return a list of Ranking # Company Information."""
    founded = int(founded)
    results = db.session.query(*sel_all).filter(Inc2018_data.founded == founded).all() 
    inc_jsondata_list = []

    results_list = build_metadata_list(inc_jsondata_list,results)
    
    return jsonify(results_list)

###############################################################
    
if __name__ == "__main__":
    app.run(debug=True)
