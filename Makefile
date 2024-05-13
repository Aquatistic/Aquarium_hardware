black_refactor:
	@black .

test_temperature_sensor:
	python3 -m sensors.HardwareSensors.TemperatureSensor

test_water_level_sensor:
	python3 -m sensors.HardwareSensors.WaterLevelSensor

test_food_level_sensor:
	python3 -m sensors.HardwareSensors.FoodLevelSensor
