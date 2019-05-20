add jar hdfs:/tmp/json-1.3.7.3.jar;
add jar hdfs:/tmp/json-serde-1.3.7.3.jar;
add jar hdfs:/tmp/json-serde-cdh5-shim-1.3.7.3.jar;

DROP TABLE IF EXISTS twits;
CREATE EXTERNAL TABLE twits (
	messages 
	ARRAY<
	    STRUCT<body: STRING,
	        symbols:ARRAY<STRUCT<symbol:STRING>>,
	        entities:STRUCT<sentiment:STRUCT<basic:STRING>>
	    >
	>
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe' 
STORED AS TEXTFILE
LOCATION '/tmp/twits';

create table message_extracted (symbols array<struct<symbol:string>>, sentiment STRING, body STRING) STORED AS TEXTFILE;
create table message_filtered (symbols array<struct<symbol:string>>, sentiment STRING, body STRING) STORED AS TEXTFILE;
create table sentiment_data (symbol string, sentiment STRING, body STRING) STORED AS TEXTFILE;

insert overwrite table message_extracted 
select message.symbols, message.entities.sentiment, message.body from twits 
lateral view explode(messages) messages as message where message.entities.sentiment is not null;

insert overwrite table message_filtered 
select symbols, sentiment, body from twits_message where sentiment is not null;

insert overwrite table sentiment_data 
select symbol.symbol, sentiment, body from messages lateral view explode(symbols) symbols as symbol;
