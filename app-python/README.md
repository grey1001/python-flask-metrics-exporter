# Dockerized Flask App with Prometheus Metrics
This is a Dockerized Flask web application that exposes Prometheus metrics for Docker image pulls from Docker Hub.

## Configuration

The application is configured to fetch Docker image pull counts from Docker Hub. It uses the `DOCKERHUB_ORGANIZATION` environment variable to specify the Docker Hub organization from which to fetch pull counts.

## Deployment

### Prerequisites

- Docker
- Kubernetes (optional)

### Local Deployment

To deploy the application locally, follow these steps:

1. Clone the repository:
git clone <repository-url>

Navigate to the project directory:

cd <project-directory>

Build the Docker image:
docker build -t <image-name>:<tag> .

Run the Docker container:
docker run -d -p <host-port>:2113 <image-name>:<tag>
Replace <repository-url>, <project-directory>, <image-name>, <tag>, and <host-port> with appropriate values.

###Kubernetes Deployment
To deploy the application on Kubernetes, follow these steps:
Ensure you have a Kubernetes cluster set up and configured (kubectl installed and configured to point to your cluster).
Write your manifest files for your deployment and service. 
A simple nodePort service is sufficient to run the application
Be sure to specify the correct image name and tags
Apply the Kubernetes manifest file:
kubectl apply -f <manifest-file>
Replace <manifest-file> with the path to your Kubernetes manifest file.

Accessing Metrics
Once the application is deployed, you can access the Prometheus metrics endpoint at <hostname>:<port>/metrics, where <hostname> is the hostname or IP address of the machine running the application, and <port> is the port configured for the application (default is 2113).

Troubleshooting
If you encounter any issues during deployment or while accessing the metrics, check the application logs for error messages. 
Make sure Docker and Kubernetes are properly configured and have access to the necessary resources.