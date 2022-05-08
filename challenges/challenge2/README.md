


In **GCP** it is again similar to the AWS the first request will return a directory and the users have to make further calls to the api to get the values.

>curl "http://metadata.google.internal/computeMetadata/v1/instance/" -H "Metadata-Flavor: Google"

  

# Assumptions

- The machine that is running this service is configured with right access keys and permissions in IAM.


# Installation:

sudo pip3 install pipenv
pipenv install


# Execution:


python3 querymetadata.py

  

  

Examples for the key : image or machine-type