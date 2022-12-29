import random
import time
import json


def read_conditions():
    with open('./fakeData/conditions.txt') as conditions:
        list_of_conditions = conditions.read().split(', ')
    return list_of_conditions


def generate_conditions():
    condition_list = read_conditions()
    return condition_list[random.randint(0, len(condition_list)-1)]


def generate_heat():
    heat = random.randint(-24, 56)
    return heat


def generate_humidity():
    humid = random.randint(0, 100)
    return humid


def generate_a_message():
    timestamp = int(time.time())
    condition = generate_conditions()
    heat = generate_heat()
    humidity = generate_humidity()

    message = {
        "timestamp": timestamp,
         "condition": condition,
         "temp": heat,
         "humidity": humidity
         }

    return json.dumps(message).encode('utf-8')

