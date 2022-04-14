!pip install pyspark
from pyspark.sql import SparkSession
import pyspark.sql.functions as f
import pyspark.sql.types as t

spark = SparkSession.builder.getOrCreate()
df = spark.read.format("csv").option("header", "true").load("transactions_map.csv")
df.show(1, vertical=True)


df.groupBy("number_transactions").count().orderBy(F.col("number_transactions").desc()).show(5)


df.select("number_transactions", "amount_transactions", "icij_sar_id").describe().show()


def main():
    spark = SparkSession.builder.getOrCreate()
    df = spark.read.format('csv').option('header', 'true').load("transactions_map.csv")
    df.show(3)
    output = (
        df
        .groupby('icij_sar_id')
        .agg(
            F.count('icij_sar_id').alias('id'),
            F.round(F.avg('number_transactions')).cast(type.IntegerType()).alias('avg_num'),
            F.min('amount_transactions').alias('min_price'),
            F.max('amount_transactions').alias('max_price')
        )
        .filter("id > 10")
    )
    output.coalesce(3).write.mode('overwrite').format('json').save('result.json')
    
main()
