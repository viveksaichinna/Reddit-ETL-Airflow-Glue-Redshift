import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Amazon S3
AmazonS3_node1753379470016 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://vivek-reddit-bucket/raw/reddit_20250723.csv"], "recurse": True}, transformation_ctx="AmazonS3_node1753379470016")

# Script generated for node Drop Fields
DropFields_node1753379508416 = DropFields.apply(frame=AmazonS3_node1753379470016, paths=["edited", "spoiler", "stickied"], transformation_ctx="DropFields_node1753379508416")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=DropFields_node1753379508416, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1753378748229", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1753379512450 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1753379508416, connection_type="s3", format="csv", connection_options={"path": "s3://vivek-reddit-bucket/clean_files/", "partitionKeys": []}, transformation_ctx="AmazonS3_node1753379512450")

job.commit()
