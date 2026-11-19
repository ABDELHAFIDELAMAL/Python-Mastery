from pyspark.sql import SparkSession

df = SparkSession.builder.getOrCreate()
df.show()