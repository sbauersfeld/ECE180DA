import paho.mqtt.publish as publish
MQTT_SERVER = "2607:f010:2e9:14:c85:73d:3432:f2ff"
MQTT_PATH = "ece180d_Best_Group"
publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER)