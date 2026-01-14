# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "a8926498-46df-4bad-8156-7f6e7b466504",
# META       "default_lakehouse_name": "demolh",
# META       "default_lakehouse_workspace_id": "61345cca-e3c7-4e28-9462-85a31c79ed39",
# META       "known_lakehouses": [
# META         {
# META           "id": "a8926498-46df-4bad-8156-7f6e7b466504"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# # Data Exploration

# CELL ********************

df = spark.sql("SELECT * FROM sales LIMIT 10")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
