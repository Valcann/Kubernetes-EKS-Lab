import boto3
from botocore.exceptions import ClientError
from fastapi import FastAPI
import json
import os
app = FastAPI()

user = os.getenv('USER')

@app.get("/")
async def root():
    return {"message": f"Hello {user}"}

@app.get("/health")
async def root():
    return {"message": f"UP!"}

@app.get("/generate")
async def generate_random_password():
    http_response = {}
    client = boto3.client('secretsmanager', region_name="us-east-1")
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