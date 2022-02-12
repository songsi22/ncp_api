import hashlib
import hmac
import base64
import json
import time
import requests


def send(access_key, secret_key, uri, api_url):
    res = requests.get(api_url + uri, headers=make_signature(access_key, secret_key, uri))
    return json.loads(res.text)


def make_signature(access_key, secret_key, uri):
    timestamp = int(time.time() * 1000)
    timestamp = str(timestamp)
    secret_key = bytes(secret_key, 'UTF-8')
    method = "GET"
    message = method + " " + uri + "\n" + timestamp + "\n" + access_key
    message = bytes(message, 'UTF-8')
    signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
    headers = {
        "x-ncp-apigw-timestamp": timestamp,
        "x-ncp-iam-access-key": access_key,
        "x-ncp-apigw-signature-v2": signingKey,
    }
    return headers
