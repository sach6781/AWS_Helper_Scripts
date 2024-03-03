import sys
import boto3
import json
from botocore.config import Config
from warrant.aws_srp import AWSSRP

from botocore.exceptions import ClientError

import hmac
import hashlib
import base64


def calculate_secret_hash(client_id, client_secret, username):
    message = username + client_id
    dig = hmac.new(str(client_secret).encode('utf-8'),
                   msg=str(message).encode('utf-8'), digestmod=hashlib.sha256).digest()
    return base64.b64encode(dig).decode()


u_1 = 'test.io@yopmail.com'

# Pool details
pool_id = 'ap-south-1_XYZ'
client_id = 'XYZ'
client_secret = 'XYZ'

my_config = Config(
    region_name='ap-south-1')
client = boto3.client('cognito-idp', config=my_config)

# User details
email = 'test@cool.fr.nf'
password = 'ABC@12345'

attributes = [
    {'Name': 'email', 'Value': 'test@cool.fr.nf'},
]


def sign_up_and_verify_otp():
    try:
        secret_hash = calculate_secret_hash(client_id, client_secret, email)
        response = client.sign_up(
            ClientId=client_id,
            SecretHash=secret_hash,
            Username=email,
            Password=password,
            UserAttributes=attributes
        )

        print(f"User {email} has been signed up successfully. Confirmation code: {response['UserConfirmed']}")
        print(f"Final response - {response}")
        confirmation_code = input("Enter the confirmation code received: ")

        # Confirm the sign-up with the entered confirmation code
        confirm_response = client.confirm_sign_up(
            ClientId=client_id,
            SecretHash=secret_hash,
            Username=email,
            ConfirmationCode=confirmation_code
        )

        print(f"User {email} has been confirmed successfully. with response - {confirm_response}")

    except ClientError as e:
        print(f"Error: {e}")


def login():
    aws = AWSSRP(username=email, password=password, pool_id='ap-south-1_XYZ',
                 client_id='XYZ',
                 client_secret='XYZ', client=client)
    token = aws.authenticate_user()
    print(f"Complete token response - {token}")
    id_token = token["AuthenticationResult"]["IdToken"]
    print(id_token)


sign_up_and_verify_otp()
login()
