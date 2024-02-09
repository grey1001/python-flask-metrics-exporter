import logging
from flask import Flask, Response
from prometheus_client import Gauge, generate_latest
import requests
import os

logging.basicConfig(level=logging.ERROR)  

app = Flask(__name__)


DOCKERHUB_ORGANIZATION = os.getenv('DOCKERHUB_ORGANIZATION', 'camunda')
PULLS_ENDPOINT = f'https://hub.docker.com/v2/repositories/{DOCKERHUB_ORGANIZATION}/?page_size=25&page=1'

docker_image_pulls = Gauge('docker_image_pulls', 'The total number of Docker image pulls', ['image', 'organization'])

def fetch_docker_image_pulls():
    try:
        response = requests.get(PULLS_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        if not data.get('results'):
            logging.error(f"The specified organization '{DOCKERHUB_ORGANIZATION}' cannot be found")
            return
        for result in data.get('results', []):
            docker_image_pulls.labels(image=result.get('name', ''), organization=DOCKERHUB_ORGANIZATION).set(result.get('pull_count', 0))
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching Docker image pulls: {e}")

@app.route('/metrics', methods=['GET'])
def metrics():
    fetch_docker_image_pulls()
    return Response(generate_latest(), mimetype='text/plain')

def main():
    try:
        app.run(host='0.0.0.0', port=2113)
    except Exception as e:
        logging.error(f"Error starting server: {e}")

if __name__ == '__main__':
    main()