# DESCRIPTION

    This template is can be used to create a dataset of services pricing of aws using boto3.
---

## Prerequiste

* Install Python
* AWS Configure : provide the credentials in aws_config.py file

## Steps

### 0. Clone the source code from github

    ```bash
    git clone https://github.com/knoldus/boto3pricing.git
    cd boto3pricing/
    ```

### 1. create python virtual_env

    ```bash
     python3 -m venv ./venv
     source ./venv/bin/activate
    ```

### 2. install dependencies

    ```bash
     pip3 -r install ./requirements.txt
    ```

### 3. create the dataset

    ```bash
     python3 pricing.py
    ```

* Note: First update the services required in code
