# packages to import
import json
from datetime import datetime
import uuid
import time
from pykafka import KafkaClient

class CarProducer:

    def __init__(self):
        self.fInput = json.load(open('./data/car.json'))
        self.coordinates = self.fInput['features'][0]['geometry']['coordinates']
        self.client = KafkaClient(hosts = 'localhost:9092')
        self.topic = self.client.topics['London']
        self.producer = self.topic.get_sync_producer()
        self.data = {'brand' : 'audi'}
        self.trigger = True

    def generate_random_id(self):
        return uuid.uuid4()

    def generate_coordinates_data(self, coordinates):
        counter = 0
        while self.trigger:
            self.data['key'] = self.data['brand'] + '_' + str(self.generate_random_id())
            self.data['timestamp'] = str(datetime.utcnow())
            self.data['longitude'] = coordinates[counter][0]
            self.data['latitude'] = coordinates[counter][1]
            self.producer.produce((json.dumps(self.data)).encode('ascii'))
            time.sleep(1)
            if counter == len(coordinates) - 1:
                counter = 0
            else: counter = counter + 1

            print (self.data)

    def activate(self):
        self.generate_coordinates_data(self.coordinates)

CarProducer().activate()
