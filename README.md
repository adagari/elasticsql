# sqlastic
A SQL Client for Elasticsearch which aims to simply the use of sql statments against an Elasticsearch database. 

You will need Python with the Requests module installed.

Sample SQL examples:
```
SHOW tables;
```
```
DESCRIBE kibana_sample_data_logs;
```
```
SELECT ip FROM kibana_sample_data_logs;
```
```
SELECT agent,COUNT(agent) as count 
FROM kibana_sample_data_logs 
GROUP BY agent 
ORDER BY count DESC 
LIMIT 5;
```
