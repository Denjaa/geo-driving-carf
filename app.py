from flask import Flask
from flask import render_template
from flask import Response
from pykafka import KafkaClient
import time

app = Flask(__name__)

def kafkaClient():
    return KafkaClient(hosts = 'localhost:9092')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/topic/<topicname>', methods=['GET'])
def get_message(topicname):
    client = kafkaClient()
    def events():
        for i in client.topics[topicname].get_simple_consumer():
            yield "event: {0}\ndata: {1}\n\n".format("listen", i.value.decode())
    return Response(events(), mimetype= 'text/event-stream')

if __name__ == '__main__':
    app.run(debug = True, port = 5001)
