Apache Airflow Project (COVID-19 Analysis Service)
===============

Introduction
----
This is the apache airflow project with HDFS, Grafana, Kibana and Datadog compatibility.


### Project Doc

Project documentation link : [Documentation file](https://docs.google.com/document/d/1emYYIOu9f7Vru9Z0EurjiF3brb9SMe8yAzpxLmNDKuo/edit)


Pre-requisite for Running the Project
---
```   
1. Install spark
    pip install spark
2. Install hadoop and to do that follow below link
    [https://phoenixnap.com/kb/install-hadoop-ubuntu]
3. Install apache airflow
    pip install apache-airflow
    and foe further steps follow this link [https://airflow.apache.org/docs/stable/installation.html]
    airflow will run on port 8080 by deafult
4. Install elastic search and to do that follow below link
    [https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html]
    elastic search will run on port 9200 by deafult
5. Install kibana and to do that follow below link
    [https://www.elastic.co/guide/en/kibana/current/targz.html]
    kibana will run on port 5601 by deafult
6. Install Grafana and to do that follow below link
    [https://grafana.com/grafana/download]
    grafana will run on port 3000 by deafult
7. For datadog goto below link and follow all the steps
    [https://www.datadoghq.com/]
```


Steps for Running the Project
---
```   
1. Open Project folder airflow
2. Then set Airflow path:
    - go to the folder where you created airflow_home folder.
    - open terminal there and set airflow_path using this command export AIRFLOW_HOME=$(pwd)/airflow_home
3. Then write airflow initdb. It will create airflow database, logs and unittest file.
4. Then create a dags folder inside airflow_home folder to store our dags.
5. Now to start server run the commands below:
    - airflow webserver
    - airflow scheduler
6. Now to go to localhost:8080 in your browser you will see some example dags there.
```


Key Entities in Code
----
```   
+-- airflow
|  +--dags
|       +--main_dag.py
|  +--logs
|       +--covid_stats.log
|  +--plugins
|       +--extract.py
|       +--validate_and_clean_data.py
|       +--generate_csv.py
|       +--hive_query.py
|       +--move_data_to_sql.sh
|       +--sql_config.sh
```


Dependencies
----
1. **Hadoop**: database connection and queries execution of sqlite3.    

2. **Spark**: software test framework for running test cases.

3. **Apache-airflow**: framework for measuring coverage for test cases.

4. **Grafana**: mocking framework is a tool that will help to generate stubs and mocks.

5. **Kibana**: framework for measuring coverage for test cases.

6. **Datadog**: framework for measuring coverage for test cases.
