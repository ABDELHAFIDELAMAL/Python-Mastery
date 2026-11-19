
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min, count

# 1. Create Spark Session
spark = SparkSession.builder \
    .appName("PySparkTest") \
    .master("local[*]") \
    .getOrCreate()

# 2. Create Dataset
data = [
    (1, "Ali", 22, 15.5),
    (2, "Sara", 23, 18.0),
    (3, "Youssef", 21, 12.0),
    (4, "Amine", 24, 16.5),
    (5, "Fatima", 22, 19.0),
    (6, "Omar", 25, 9.0)
]

columns = ["id", "name", "age", "note"]

# 3. Create DataFrame
df = spark.createDataFrame(data, columns)

print("===== ALL STUDENTS =====")
df.show()

# 4. Filter successful students
print("===== SUCCESSFUL STUDENTS =====")
df.filter(df.note >= 10).show()

# 5. Calculate average note
print("===== AVERAGE NOTE =====")
df.select(avg("note").alias("average")).show()

# 6. Maximum note
print("===== MAXIMUM NOTE =====")
df.select(max("note").alias("max_note")).show()

# 7. Sort students by note
print("===== SORTED STUDENTS =====")
df.orderBy(df.note.desc()).show()

# 8. Count students
print("===== TOTAL STUDENTS =====")
df.select(count("*").alias("total")).show()

# 9. Stop Spark
spark.stop()
