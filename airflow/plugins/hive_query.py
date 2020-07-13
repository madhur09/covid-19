from pyspark.sql import SparkSession
import datetime


spark = SparkSession \
    .builder \
    .appName("Python Spark SQL Hive integration ") \
    .enableHiveSupport().getOrCreate()


def hive_query():
    spark.sql("create table if not exists covid_state (state string, case_count int, status string)    PARTITIONED BY \
                (date_str string)    ROW FORMAT DELIMITED    FIELDS TERMINATED BY ','    LINES TERMINATED BY '\n'    \
                stored as textfile")

    spark.sql("LOAD DATA INPATH '/tmp/covid_state_dataa.csv' overwrite INTO TABLE \
                covid_state PARTITION(date_str='"+str(datetime.datetime(2020,7,1).strftime('%Y-%m-%d'))+"')")
