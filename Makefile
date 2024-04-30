black_refactor:
	@black .

test_temperature_sensor:
	python3 -m sensors.TemperatureSensor

test_water_level_sensor:
	python3 -m sensors.WaterLevelSensor

test_food_level_sensor:
	python3 -m sensors.FoodLevelSensor
