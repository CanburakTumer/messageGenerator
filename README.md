# Message Generator for Pub/Sub

This is a personal project to have some hands-on practice for sending messages to Pub/Sub.

## How to run?
Best way to run this code is on Google Cloud.

Below steps can be followed to run on own Google Cloud environment. 
1. Clone this repository `git clone <REPO_URL>`  
2. Navigate into project folder `cd messageGenerator`
3. Build docker image `gcloud builds submit -t <IMAGE_TAG> .`
4. Create a GCE VM instance using the container image `gcloud compute instances create-with-container <INSTANCE_NAME> --zone=us-central1-a --machine-type=e2-micro --scopes=https://www.googleapis.com/auth/pubsub,https://www.googleapis.com/auth/devstorage.read_only --container-image=<MY_IMAGE> --container-restart-policy=always --container-env=PROJECT_ID=c<MY_PROJECT>,TOPIC_ID=<MY_TOPIC>`