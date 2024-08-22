import configparser


class Configuration:

    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.mqtt_addresss = config['MQTT']['address']
        self.mqtt_topic = config['MQTT']['topic']
        self.mqtt_client_id = config['MQTT']['client_id']
        self.uprn = config['Property']['uprn']
        self.logging_level = config['Logging']['level']
        self.pause_minutes = int(config['Runner']['minutes_between_runs'])
