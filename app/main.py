import boto3
from botocore.exceptions import ClientError
from fastapi import FastAPI
import json
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/generate")
async def generate_random_password():
    http_response = {}
    client = boto3.client('secretsmanager')
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
        http_response['body'] = json.dumps(f"Generated password: {response['RandomPassword']}")
        return http_response
    except ClientError as e:
        raise Exception("boto3 client error in generate_random_password: " + e.__str__())
    except Exception as e:
        raise Exception("Unexpected error in generate_random_password: " + e.__str__())