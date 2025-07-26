Twitter Sentiment Analysis is a big data project that analyzes the sentiment of tweets in both real-time (streaming) and batch processing modes. 
The architecture utilizes Apache Kafka for real-time data ingestion, Apache Spark for data processing, TextBlob for sentiment analysis, and MySQL for data storage. 
The project allows for performance comparison between streaming and batch modes, showcasing the strengths and trade-offs of each approach.
Features
Real-time sentiment analysis of simulated Twitter data streams.

Batch sentiment analysis for historical data.

Multi-topic Kafka ingestion simulating real-world Twitter firehose.

Apache Spark Streaming for scalable real-time processing.

MySQL database storage for raw, filtered, and scored tweets.

Comparison scripts to analyze performance differences between streaming and batch modes.
