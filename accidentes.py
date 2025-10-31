# Importamos librerías necesarias
from pyspark.sql import SparkSession, functions as F
import time

# Inicializa la sesión de Spark
spark = SparkSession.builder.appName("AccidentesTransito").getOrCreate()

# Ruta del archivo en HDFS
file_path = 'hdfs://localhost:9000/Tarea3/wacd-xkg8.csv'

# Leer el archivo CSV
df = spark.read.format('csv') \
    .option('header', 'true') \
    .option('inferSchema', 'true') \
    .load(file_path)

# Mostrar esquema
df.printSchema()

# Mostrar primeras filas
df.show(5)

# Estadísticas básicas
df.summary().show()

# Conteo por año
print("Accidentes por año:")
df.groupBy("a_o").count().orderBy(F.col("count").desc()).show()

# Conteo por día
print("Accidentes por día:")
df.groupBy("dia").count().orderBy(F.col("count").desc()).show()

# Conteo por gravedad
print("Accidentes por gravedad:")
df.groupBy("gravedad").count().orderBy(F.col("count").desc()).show()

# Mantener sesión abierta 5 minutos
print("La sesión permanecerá abierta durante 5 minutos...")
time.sleep(300)

spark.stop()
