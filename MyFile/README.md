# DATA-ENGNEERING-CODES
-All about data engineering zoomcamp

# Postgres(Image) Commandline for Docker
winpty docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:13

# Other Window Users
```
winpty docker run -it \
  -e POSTGRES_USER="root" \ 
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v c:/Users/Mujeeb-PC.DESKTOP-GS5FVCL/Desktop/DatEng-Course/docker-example/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5431:5431 
  postgres:13
```
```
 docker run -it 
 -e POSTGRES_USER="root" 
 -e POSTGRES_PASSWORD=admin
 -e POSTGRES_DB="ny_taxi" 
 -v "/c/users/abhis/git/zoomcamp/week_1/ny_taxi_postgres_data://var/lib/postgresql/data"
 -p 5431:5432 postgres:13
``` 
leave it running... and open another bash terminal

# Installation of Pgcli

python -m pip install --upgrade pip
pip install postgres
pip install pgcli 

# To check pgcli
pgcli
pgcli --help
pip list -v
which pgcli
pip show pgcli
pip install pgcli
# Error Encounter: An enrror was encountered when running the pgcli where I had to change the path location using:
# You can either add it to path via bash,or gui(Computer=Properties=Advance Setting=Envrironment variables=Path creation)
export PATH=<pip path>/bin:$PATH
no space before and after =.
after that run echo $PATH to confirm, if its added to the path

# Run server...
It was run on -Powershell when bash freeze
# Client Server 
-Error encountered when i executed the commands and the port was change to 5431: 5432
```
pgcli -h localhost -p 5431 -u root -d ny_taxi 
```
passport prompt....then connected
# syntax
\dt, \dT, SELECT 1
# Installation of Jupyter
```
  pip install jupyter
```
```
  jupyter notebook
``` 
Leave it running and open another bash terminal....Jupyter page open through browser, Click on New to click python3

# Write python script
```
  --- pip install pandas
  --- import pandas as pd
  --- pd.__version__

```
Go to file to rename: upload-data and press ok

# Downloading of Data in Jupyter using Url:
Data Url:- https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
Data Dict:- https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf
Data Look-up:- https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv
Shortcut keys Jupyter:- https://towardsdatascience.com/jypyter-notebook-shortcuts-bf0101a98330
# syntax
``` wget url
  ```
Download wget if ure using window then copy the file from the downloading folder,(check the (path) on your cmd, open local disk, click on window, click on system32 then past it there.Then go to environment variable to add the path.

close cmd and re-open cmd to check wget.
Then run the above commands
# Not necessary
 ```
 cp ~/tmp/pg-test/yellow_tripdata_2021-01.csv . 
 ``` 
 if the file is found after running (ls) on bash.
# To view the data
``` less yellow_tripdata_2021-01.csv 
```
# To check first 100 row and To save it in different name
```
head -n 100 yellow_tripdata_2021-01.csv
```
# To save it in different name
```
head -n 100 yellow_tripdata_2021-01.csv >yellow_head.csv
```
# To check how many lines in a data (Length of Data)
```wc -l yellow_tripdata_2021-01.csv
```
# Jupyter Notebook was used to load the data using sqlalchemy. and the data was break into chunk which was loaded in batches. 

# CONNECTING PGADMIN AND POSTGRES#
docker pull dpage/pgadmin4

```
docker run -it -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" -e PGADMIN_DEFAULT_PASSWORD="root" -p 8080:80 dpage/pgadmin4
```
After running it on cmd,shell,bash, then go to a new browser and type (localhost:8080)
Create a new server inputting the username,password,port that was initially executed when loading database.
NOTE: And error occur due to the fact that we need to link the the two image in the container(postgres and pgadmin) with the database.

# CREATE DOCKER NETWORK
url: https://docs.docker.com/engine/reference/commandline/network_create/

First Stopped both Postgres image and pgAdmin Server.Then run the below commands:
```
(docker network create [OPTIONS] NETWORK)
docker network create pg-network
```
run it on postgres Server that was stopped

# NETWORK_postgres
```
winpty docker run -it 
-e POSTGRES_USER="root" 
-e POSTGRES_PASSWORD="root" 
-e POSTGRES_DB="ny_taxi" 
-v /c/Users/Mujeeb-PC.DESKTOP-GS5FVCL/Desktop/DatEng-Course/docker-example/ny_taxi_postgres_data:/var/lib/postgresql/data
-p 5431:5432 
--network=pg-network 
--name pg-database  
postgres:13

```
winpty docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v c:/Users/Mujeeb-PC.DESKTOP-GS5FVCL/Desktop/DatEng-Course/docker-example/ny_taxi_postgres_data:/var/lib/postgresql/data -p 5431:5432 --network=pg-network --name pg-database  postgres:13

``` 
leave it running..... then reconnect notebook jupyter
run pgcli -h localhost -p 5431 -u root -d ny_taxi
then execute:
SELECT COUNT(1) FROM yellow_taxi_data

# syntax: docker ps, docker ps -a
(Linux cmd: docker exec -it pg-database /bin/sh, psql -h localhost -p 5432 -d ny_taxi -U root)
```
# NETWORK_pgAdmin
This should be run on another terminal

```
docker run -it -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" -e PGADMIN_DEFAULT_PASSWORD="root" -p 8080:80 --network=pg-network --name pg-admin dpage/pgadmin4

```
```
docker run -it 
-e PGADMIN_DEFAULT_EMAIL="admin@admin.com" 
-e PGADMIN_DEFAULT_PASSWORD="root" 
-p 8080:80 
--network=pg-network 
--name pg-admin 
dpage/pgadmin4
```
# Open Pgadmin on browser
After connection, leave the two server running and open your browser to run localhost:8080
connect using the username and password.

# DE Zoomcamp 1.2.4 - Dockerizing the Ingestion Script
convert the jupyter commands to pythong script:
```jupyter nbconvert --to=script upload-data_pandas.ipynb
```
url: https://docs.python.org/3/library/argparse.html
url: https://docs.python.org/3/library/__main__.html

URL="https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv"

python ingest_data.py  --user=root  --password=root  --host=localhost  --port=5431  --db=ny_taxi  --table_name=yellow_taxi_trips  --url=${URL}

echo $?