import paho.mqtt.subscribe as subscribe


def on_message_run(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))


subscribe.callback(on_message_run, "yourTopic",
                   hostname="yourMQTTserver",
                   auth={'username': "yourUsername", 'password': "yourPassword"})


