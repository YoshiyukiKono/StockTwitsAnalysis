add jar hdfs:/tmp/brickhouse-0.7.1-SNAPSHOT.jar;
CREATE TEMPORARY FUNCTION to_json AS 'brickhouse.udf.json.ToJsonUDF';

create table json_message (message STRING) STORED AS TEXTFILE;

insert overwrite table json_message
select to_json(named_struct('message_body', body, 'sentiment', sentiment)) from sentiment_data;
