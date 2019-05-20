from __future__ import print_function
import sys
from random import random
from operator import add
from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .appName("JsonGen")\
    .getOrCreate()
    
spark.sparkContext.setLogLevel("ERROR")

#json_list = spark.read.table("json_message")
json_list = spark.sql("select * from json_message")

#json_list.show(5)

path = "./output.json"
with open(path, mode='w') as f:
  f.write('{"data":[')
  bool_first_line = True
  for row in json_list.rdd.collect():
    if bool_first_line:
      f.write(",\n")
      bool_first_line = False
    print(row.message)
    #f.write(row.message.encode("utf-8"))
    f.write(row.message)
    
  f.write("]}")
