# MQTT-Based-IOT-SGNS

This project including 3 parts: Server scripts(Python), Gateway scripts(Python) and Node code(Arduino based).

### Server
- Front-end(Python-Flask) for visualising the date of Nodes.
- Database processing code(SQLite3).
- Scheduler(for calculating the average data once per day/hours).

### Gateway
- Receiving the date from serial-port(USB device) which is sent by nodes via LoRa.
- Processing the raw date and publishing to the MQTT broker.

### Node
- Collecting sensors's date once per hour
- Sending those date to Gateway though LoRa module.


> This project is base on MQTT which is suitable for the scenario of IOT communication. SGNS stands for Server & Gateway & Node System


version.0.3


