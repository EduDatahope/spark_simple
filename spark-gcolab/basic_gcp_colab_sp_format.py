# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

# %% id="t32wpceMzoXX"
from google.colab import auth
auth.authenticate_user()

# %% id="Me5lq5B10zwd"
# !curl https://sdk.cloud.google.com | bash

# %% id="syl3LVMoz32f"
# !gcloud init

# %% id="8Wueokw80NuL"
# !mkdir gcc_temp

# %% id="dlrmLLY-0THy"
# !gsutil cp gs://dhope-input-data/spark/sales.csv.txt ./gcc_temp/.

# %% id="sdKGCTta0rcL"
# !pip install --upgrade google-cloud-bigquery-storage pyarrow

# %% id="XyxtSjLE08xV"
# !sudo apt update
# !apt-get install openjdk-8-jdk-headless -qq > /dev/null
#Check this site for the latest download link https://www.apache.org/dyn/closer.lua/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz
# !wget -q https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz
# !tar xf spark-3.2.1-bin-hadoop3.2.tgz
# !pip install -q findspark
# !pip install pyspark
# !pip install py4j

import os
import sys
# os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
# os.environ["SPARK_HOME"] = "/content/spark-3.2.1-bin-hadoop3.2"


import findspark
findspark.init()
findspark.find()

import pyspark

from pyspark.sql import DataFrame, SparkSession
from typing import List
import pyspark.sql.types as T
import pyspark.sql.functions as F

spark= SparkSession \
       .builder \
       .appName("Our First Spark Example") \
       .getOrCreate()

spark

# %% id="lcN5F9q21zYF"
from pyspark.sql.types import StructType,StructField,IntegerType,StringType,DateType

d_schema = StructType([
    StructField("product_id" ,StringType(),True),
    StructField("customer_id" ,StringType(),True),
    StructField("order_date" ,StringType(),True),
    StructField("location" ,StringType(),True),
    StructField("source_order" ,StringType(),True)
]
)

df = spark.read\
    .option("header", "false")\
    .format("csv")\
    .schema(d_schema)\
    .load("./gcc_temp/sales.csv.txt")

df.show()



# %% id="0S9M9iSv-UM5"
import pandas as pd
import pandas_gbq

project_id = "dwhp-437913"
table_id = 'db1.tb_colab_test2'

dfp = df.toPandas()

##if_existsstr replace / fail

pandas_gbq.to_gbq(dfp , table_id, project_id=project_id ,if_exists='append')

# %% id="KhRh8LIKxWSB"
configuration = {
   'query': {
     "useQueryCache": True,
     "use_bqstorage_api": True
   }
}

sql = "select * from db1.tb_colab_test2"

##df2 = pandas_gbq.read_gbq(sql, project_id=project_id)
##
df2 = pandas_gbq.read_gbq(sql, project_id=project_id,configuration=configuration)

df2

# %% id="z05FcVaDyF4S"
from google.cloud import bigquery

pid = "dwhp-437913"

client = bigquery.Client(pid)

query_str = '''
CALL `dwhp-437913.db1.sp_truncate_test2`();
'''

print (client )

query_job = client.query(query_str)
rows = list(query_job.result())
print(rows)

