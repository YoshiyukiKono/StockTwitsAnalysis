select sentiment, count(sentiment) as count from sentiment_data group by sentiment;
select symbol, count(symbol) as count from sentiment_data group by symbol;
select symbol, sentiment, count(*) as count from sentiment_data group by symbol, sentiment;
