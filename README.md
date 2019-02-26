## Data Journalism Project

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


#### Data Extract and Load
- CSV formatted Data downloaded from the data.world
- Using python/SQLAchemy/psycopg2 to Extract out[(GitHub)]()/Load into[(GitHub)](https://nbviewer.jupyter.org/github/Pyligent/Inc5000_Data_Viz_Project/blob/master/Data_Load.ipynb) the PostgreSQL database
- Flask Webserver will provide the JSON format API data
  
#### Data Visualization 
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

  
  
