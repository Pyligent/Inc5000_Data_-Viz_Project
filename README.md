##   Data Journalism Project   
#### INC Magazine's 5000 fastest growing private companies
![incpic](img/inc.png)

### Exploring INC Magazine's fastest growing private companies

#### Data Source

- [Inc. Magazine](https://www.inc.com) has published the fastest growing private companies ranking list every year. The full data sets are hosted in the data.world.     
  - [2018 Data](https://data.world/aurielle/inc-5000-2018) (Geo Data added in 2018 List)
  - [2007 - 2017 Data](https://data.world/aurielle/inc-5000-10-years)   
  
#### Project Overview
- Data Storage : PostgreSQL   
- Workflow Engine (WFE): Flask Web Server/SQLAchemy/Python   
- Web Application/GUI : HTML/CSS, JavaScript,D3,Leaflet.js   
- Production Deployment: Heroku  
- Product : Web Data Journalism Visualization, JSON format API data for INC 5000 data      

<hr>


#### 1. Data Extract and Load
- CSV formatted Data downloaded from the data.world
- Using python/SQLAchemy/psycopg2 to Extract out[(GitHub)](https://nbviewer.jupyter.org/github/Pyligent/Inc5000_Data_Viz_Project/blob/master/Data_Extract.ipynb)/Load into[(GitHub)](https://nbviewer.jupyter.org/github/Pyligent/Inc5000_Data_Viz_Project/blob/master/Data_Load.ipynb) the PostgreSQL database
- Flask Webserver will provide the JSON format API data

#### 2. Workflow Engine (WFE)
- Using the Flask Web server/SQLAchemy/Python  to create the API route and JSON data for data visualization
- Flask API JSON Data Route:
  - **@app.route("/2018metadata")**   
    Return Full Inc2018 5000 JSON Metadata   
    
  - **@app.route("/rank/<ranking_number>")**   
    Return ranking query JSON data   
    
  - **@app.route("/state_s/<state_s>")**   
    Return State query JSON data   
    
  - **@app.route("/years_on/<yrs_on_list>")**   
    Return years on the list query JSON data   
    
  - **@app.route("/founded_year/<founded>")**   
    Return founded year query JSON data
  
 - API JSON Data Format   
   ![json_format](img/api_json_format.png)
  
    
  
#### 3. Data Visualization 
 - Explore the Geo-location relation with the fastest growing private companies.
   - States views of the companies
   - City views of companies
   - Industry-related views of companies
   - Revenues-related views of companies
   - Distribution companies by different filters
 
 - Explore the individual company information
   - Visualization the company basic information
   - Headcount/Revenue/Years on the list/CEO
   - Website information
   
 #### Option (if time is available)
 - Explore the 10 years data to discover the more interesting fact of the fastest growing private companies

  
  
