import paho.mqtt.subscribe as subscribe
import db

def on_message_run(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
    # print(type(str(message.payload)))
    # print(str(message.payload)[2:-1])
    db.insert_value(str(message.payload)[2:-1])


subscribe.callback(on_message_run, "yourTopic",
                   hostname="yourMQTTserver",
                   auth={'username': "yourUsername", 'password': "yourPassword"})

