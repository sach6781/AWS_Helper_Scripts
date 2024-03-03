import logging
from pyspark.sql import SparkSession

LOGGER = logging.getLogger(__name__)

SPARK = SparkSession.builder.getOrCreate()

left_datasets = ['dataset1', 'dataset2']


def upload_dataset():
    for data_set in left_datasets:
        data_set_name = data_set
        try:
            # Prefix = This should be added to upload data set to some existing dataset (i.e. india_datasets)
            data_set = 'Prefix.' + data_set
            print('proceeding for the dataset - {}'.format(data_set_name))
            sdf = SPARK.sql("select * from {}".format(data_set))
            # below command saves file on s3 bucket where databricks storage is configured
            sdf.coalesce(1).write.format("csv").mode("overwrite").option("header", "true").save(
                "/datasets/india_datasets/{}".format(data_set_name))
            print('Uploading completed for the dataset - {}'.format(data_set_name))
        except Exception as error:
            LOGGER.error("Error while fetching the data, the actual error is - {}".format(error))

upload_dataset()
