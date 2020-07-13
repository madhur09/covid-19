# geting directory where this script file stored.
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
source "$DIR/../config/sql_config.sh"
# create database
mysql -u maddy  'maddy' -e "CREATE DATABASE if not exists ${database} ;"
# create mysql table
mysql -u maddy  'maddy' -e "use ${database};
CREATE TABLE if not exists ${table} (
${column1} ${column1_dtype} NOT NULL,
${column2} ${column2_dtype} NOT NULL,
${column3} ${column3_dtype} NOT NULL,
${column4} ${column4_dtype} NOT NULL,
${column5} ${column5_dtype} NOT NULL,
${column6} ${column6_dtype} NOT NULL,
${column7} ${column7_dtype} NOT NULL) ;
truncate table ${table};
"
# because sqoop always append data(we can not perform overwrite operation). so we need to tuncate our table first .
# sqoop job to export hive data into sql table
# note: before running elow command start hive metastore service ( by using this command `hive --service metastore`)
# because hcatalog use metastore service to fetch hive table details
HADOOP_USER_NAME=${hadoop_user_name} sqoop export --connect jdbc:mysql://localhost/${database} -username maddy  --columns "${column1}, ${column2}, ${column3}, ${column4}, ${column5}, ${column6}, ${column7}," --table ${table}  --hcatalog-table covid_state  --input-fields-terminated-by ',' -m 1
# Sqoop is a tool designed to transfer data between Hadoop and relational databases or mainframes.
# You can use Sqoop to import data from a relational database management system (RDBMS)
# such as MySQL or Oracle or a mainframe into the Hadoop Distributed File System (HDFS),
# transform the data in Hadoop MapReduce, and then export the data back into an RDBMS.
# The import tool imports an individual table from an RDBMS to HDFS. Each row
# from a table is represented as a separate record in HDFS
# The export tool exports a set of files from HDFS back to an RDBMS.
# The target table must already exist in the database.
