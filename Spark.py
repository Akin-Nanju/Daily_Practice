# -*- coding: utf-8 -*-
"""Spark.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TSFAYLUJFA_jjXPVncS9f_DGLaRvr_0Y
"""

from pyspark.sql import *
spark = SparkSession.builder.appName('Practice').getOrCreate()
Students = [
    Row(first_name='Akin', last_name='Nanju', age=20),
    Row(first_name='Prajwal', last_name='Shrestha', age=20),
    Row(first_name='Bagish', last_name='Gautam', age=20)
]
df = spark.createDataFrame(Students)
df.show()
spark.stop()

