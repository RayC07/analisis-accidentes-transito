# analisis-accidentes-transito
"Proyecto en PySpark para analizar accidentes de tránsito desde HDFS"
# Análisis de Accidentes de Tránsito con PySpark

Este proyecto realiza un análisis de datos de accidentes de tránsito utilizando PySpark. Los datos provienen del portal de datos abiertos de Colombia y se procesan desde un archivo CSV almacenado en HDFS.

## 📂 Estructura del Proyecto
- `accidentes.py`: Script principal que lee el archivo CSV desde HDFS, realiza análisis por año, día de la semana y gravedad, y muestra estadísticas.
- `wacd-xkg8.csv`: Archivo de datos de accidentes (subido a HDFS).
- `README.md`: Este archivo con la descripción del proyecto.
- `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.

## 📊 Análisis Realizado
- Conteo de accidentes por año (`a_o`)
- Conteo de accidentes por día de la semana (`dia`)
- Conteo de accidentes por nivel de gravedad (`gravedad`)
- Estadísticas descriptivas del conjunto de datos

## 🚀 Instrucciones de Ejecución

### 1. Subir el archivo CSV a HDFS

Crea un entorno virtual e instala dependencias:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 2. Subir el archivo CSV a HDFS
hdfs dfs -put /ruta/local/wacd-xkg8.csv /Tarea3

### 3. Ejecutar el script
python3 accidentes.py

### Requisitos

Python 3
PySpark 3.5.6
Hadoop configurado con HDFS

### Fuente de datos
Datos Abiertos Colombia

### Ejemplo de salida
Accidentes por año:
+----+-----+
|a_o |count|
+----+-----+
|2017|  500|
|2018|  300|
|2019|  200|
|2020|   50|
+----+-----+

Accidentes por gravedad:
+-----------+-----+
|gravedad   |count|
+-----------+-----+
|SOLO DAÑOS |  700|
|CON HERIDOS|  300|
|CON MUERTOS|   50|
+-----------+-----+

