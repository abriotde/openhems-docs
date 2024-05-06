#!/bin/env python3

import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
import mysql.connector
import yaml
import random
import string

DB_CONFIGURATION_FILE = "clients.yml"
# SENDER = "openproduct.fr@gmail.com"
# https://console.cloud.google.com/apis/credentials?authuser=2&hl=fr&project=openproduct-410817
GMAIL_API_KEY_FILE = "../OpenProduct/openproduct-docs/private/OpenProductMailSender_OAuth2_key.json"
SUBJECT = "Présentation de la solution OpenHEMS"
EMAIL_BODY_TEMPLATE_FILE = "templateProspectionCommunication.html"


# Get DB Configuration (user/password)
with open(DB_CONFIGURATION_FILE, 'r') as file:
	configuration = yaml.safe_load(file)
prospects = configuration["prospects"]
print(prospects)

SCOPES = [
    "https://www.googleapis.com/auth/gmail.send"
]
flow = InstalledAppFlow.from_client_secrets_file(GMAIL_API_KEY_FILE, SCOPES)
creds = flow.run_local_server(port=0)
service = build('gmail', 'v1', credentials=creds)


from jinja2 import Template
with open(EMAIL_BODY_TEMPLATE_FILE, 'r') as f:
	template = Template(f.read())
	for name,prospect in prospects.items():
		print(prospect)
		email = prospect["email"]
		body = template.render(prospect)
		message = MIMEText(body, 'html')
		message['to'] = email
		message['subject'] = SUBJECT
		# message.add_header('List-Unsubscribe', '<https://www.openproduct.fr/unsubcribe.php?mail='+email+'token='+token+'>')
		create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

		try:
			message = (service
				.users().messages()
				.send(userId="me", body=create_message)
				.execute()
			)
			print(F'sent message to {email} Message Id: {message["id"]}')
		except HTTPError as error:
			print(F'An error occurred: {error}')
			message = None

