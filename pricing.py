import boto3
import json
import aws_config as config
import os
import time


AWS_ACCESS_KEY_ID = config.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = config.AWS_SECRET_ACCESS_KEY
REGION_NAME = config.REGION_NAME

# create the boto3 client
pricing = boto3.client(
    'pricing',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME
)

services_required = ["AmazonRDS", "AmazonS3", "AmazonVPC",
                     "AmazonSNS", "AWSELB", "AmazonEC2", "AmazonEKS"]


def save_data(json_data, service_name):
    filename = './AWS_DATA/{}.json'.format(service_name)
    with open(filename, 'a+') as json_file:
        if os.path.getsize(filename) > 0:
            json_file.seek(0)
            # load the existing data
            json_file_data = json.load(json_file)
            # join new data with existing
            for data in json_data:
                json_file_data.append(data)
            # set file position to offset
            json_file.seek(0)
            # convert back to json
            json.dump(json_file_data, json_file, indent=2)

        else:

            json.dump(json_data, json_file)


def get_data(service, NextToken=''):
    service_data_collection = pricing.get_products(
        ServiceCode=service,
        FormatVersion='aws_v1',
        NextToken=NextToken
    )
    print(json.loads(json.dumps(service_data_collection)), "\n--------\n")

    price_data = []
    for price in service_data_collection['PriceList']:
        print(type(price))
        print()
        print(json.dumps(price), "\n3\n")
        print(type(json.loads(price)))
        time.sleep(3)
        price_data.append(json.loads(price))

    save_data(price_data, service)

    if service_data_collection['NextToken']:
        print(service_data_collection['NextToken'])
        time.sleep(2)
        get_data(service, service_data_collection['NextToken'])


for service in services_required:
    print("Selected  Service {}".format(service))

    get_data(service)