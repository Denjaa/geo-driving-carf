# Georaphical car driving

The idea of this project is to show that you can use Kafka to store live data. Once live data is being stored it was be consumed applications. I have used Flask to develop website that works as consumer to get the live streaming data. Once data was available I used JavaScript to capture this data and plot marker on the map.

Instructions to run application:
1. Install all required packages
2. Switch on zookeeper (zookeeper-server-start.bat C:\kafka\config\zookeeper.properties)
3. Switch on kafka (kafka-server-start.bat C:\kafka\config\server.properties)
4. Create topic (kafka-server-start.bat C:\kafka\config\server.properties)
5. Switch on car_producer (to stream live data into kafka)
6. Run application
