# coding: utf-8

"""Spark SQL DataType

ByteType: int
ShortType: int
IntegerType: int
LongType: long
FloatType: float
DoubleType: float
Decimal: Decimal
StringType: ""
BinaryType: ignore
BooleanType: bool
TimestampType: datetime
DateType: date
ArrayType: list
MapType: dict
StructType: tuple
"""

from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext
import decimal
from datetime import datetime, date
from pyspark.sql import StructType, StructField, LongType

conf = SparkConf().setAppName("spark_sql_datatype_extend3")

sc = SparkContext(conf=conf)

hc = HiveContext(sc)

source = sc.parallelize(
    ["85070591730234615847396907784232501249", "85070591730234615847396907784232501249"])

rows = source.map(lambda value: int(value)).collect()

sc.stop()

for row in rows:
    print row, type(row)
