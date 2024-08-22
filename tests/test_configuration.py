from harlow_bindicator.app.configuration import Configuration


def test_configuration_broker_address():
    config = Configuration()
    assert config.mqtt_addresss == "broker"


def test_configuration_mqtt_topic():
    config = Configuration()
    assert config.mqtt_topic == "bindicator"


def test_configuration_mqtt_client_id():
    config = Configuration()
    assert config.mqtt_client_id == "bindicator_client"


def test_configuration_logging_level():
    config = Configuration()
    assert config.logging_level == "INFO"


def test_configuration_time_between_runs():
    config = Configuration()
    assert config.pause_minutes == 60
