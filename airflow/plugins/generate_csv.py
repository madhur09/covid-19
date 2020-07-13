import os
from pyspark import Row
from pyspark.sql import SparkSession
import datetime

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL Hive integration ") \
    .enableHiveSupport().getOrCreate()


def generate_csv(**kwargs):
    dict_data = kwargs['ti'].xcom_pull(dag_id='covid_stats', key='api_response')
    spark_df = spark.createDataFrame(Row(**x) for x in dict_data)
    spark_df.write\
        .mode("overwrite")\
        .csv("hdfs://localhost:9000/tmp/covid_state_data_"+str(datetime.datetime.now())+".csv")

    print('CSV generated successfully!!')
