import boto3
from botocore.exceptions import ClientError
from fastapi import FastAPI
import json
import os
app = FastAPI()

user = os.getenv('USER')
role_arn = os.getenv("ROLE_ARN")

@app.get("/")
async def root():
    return {"message": f"Hello {user}"}

@app.get("/health")
async def root():
    return {"message": f"UP!"}

@app.get("/generate")
async def generate_random_password():


    client = boto3.client('sts')
    response = client.assume_role(
        RoleArn=role_arn,
        RoleSessionName='boto3-session')

    http_response = {}
    client = boto3.client('secretsmanager', 
                        region_name="us-east-1", 
                        aws_access_key_id=response['Credentials']['AccessKeyId'],
                        aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                        aws_session_token=response['Credentials']['SessionToken'])
    try:
        response = client.get_random_password(PasswordLength=18,
            ExcludeCharacters="",
            ExcludeNumbers=False,
            ExcludePunctuation=True,
            ExcludeUppercase=False,
            ExcludeLowercase = False,
            IncludeSpace=False,
            RequireEachIncludedType=True
        )
        http_response['statusCode'] = 200
        http_response['body'] = json.dumps(f"Generated password for {user}: {response['RandomPassword']}")
        return http_response
    except ClientError as e:
        raise Exception("boto3 client error in generate_random_password: " + e.__str__())
    except Exception as e:
        raise Exception("Unexpected error in generate_random_password: " + e.__str__())