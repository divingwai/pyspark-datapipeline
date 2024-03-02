import pyspark
from delta import *

builder = pyspark.sql.SparkSession.builder.appName("MyApp") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()


def test_spark(spark):

  from pyspark.sql.types import StructType,StructField, StringType, IntegerType
  data2 = [("James","","Smith","36636","M",3000),
      ("Michael","Rose","","40288","M",4000),
      ("Robert","","Williams","42114","M",4000),
      ("Maria","Anne","Jones","39192","F",4000),
      ("Jen","Mary","Brown","","F",-1)
    ]

  schema = StructType([ \
      StructField("firstname",StringType(),True), \
      StructField("middlename",StringType(),True), \
      StructField("lastname",StringType(),True), \
      StructField("id", StringType(), True), \
      StructField("gender", StringType(), True), \
      StructField("salary", IntegerType(), True) \
    ])
  
  df = spark.createDataFrame(data=data2,schema=schema)
  df.printSchema()
  df.show(truncate=False)
