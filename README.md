**Sentiment Analysis of Twitter Tweet Data using ETL Process and Elastic Search**

* CONNECT TO THE CLUSTER USING "http://18.188.160.132:9200/" *

**CODE FRAGMENT DESCRIPTION**

**extracvs.py** - This code fragment was used to extract 100 tweets with hastage exam.

**Sentimental.py** - This was used to run senntimental analysis on the tweets extract.

**datainsert.py** - This fragment was used to insert the sentimental result into elastic search.

**load.sh**- This batch file was used to load the 3 scripts(extracvs.py,Sentimental.py,datainsert.py) to make it a background process.
to run **load.sh**

first run- **chmod +x load.sh**

and the run- **./load.sh**





