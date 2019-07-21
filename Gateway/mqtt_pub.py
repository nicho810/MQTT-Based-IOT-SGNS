import paho.mqtt.publish as publish
import time

def pub_data(data):
    publish.single("yourTopic", data,
                   hostname="yourMQTTserver",
                   auth={'username': "yourUsername", 'password': "yourPassword"})


if __name__ == '__main__':
    while (True):
        pub_data("{25,100,80,0,304,0}")
        time.sleep(1)
        print("pub finished..")

