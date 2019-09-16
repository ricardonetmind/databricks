# Databricks notebook source
spark.conf.set("fs.azure.account.key.databrickssadl.dfs.core.windows.net", "<key>")
spark.conf.set("fs.azure.createRemoteFileSystemDuringInitialization", "true")
dbutils.fs.ls("abfss://databricks@databrickssadl.dfs.core.windows.net/")
spark.conf.set("fs.azure.createRemoteFileSystemDuringInitialization", "false")

# COMMAND ----------

dbutils.fs.ls("abfss://databricks@databrickssadl.dfs.core.windows.net/data")

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
"fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
"fs.azure.account.oauth2.client.id": "<client_id>",
"fs.azure.account.oauth2.client.secret": "<secret>",
"fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/9452b23e-fd00-40c5-98f7-d9a67ab13a7e/oauth2/token"}

dbutils.fs.mount(
source = "abfss://databricks@databrickssadl.dfs.core.windows.net/data",
mount_point = "/mnt/mymount",
extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls("/mnt/mymount")

# COMMAND ----------

dbutils.fs.unmount("/mnt/mymount") 
