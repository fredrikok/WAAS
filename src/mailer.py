import smtplib
import os

def send_mail(recipient, subject, body):
  # Sender email and password
  email_sender_address = os.environ.get('EMAIL_SENDER_ADDRESS')
  email_sender_password = os.environ.get('EMAIL_SENDER_PASSWORD')

  # Connect to the Gmail SMTP server
  email_sender_host = os.environ.get('EMAIL_SENDER_HOST')
  email_sender_port = os.environ.get('EMAIL_SENDER_PORT')
  smtp_server = smtplib.SMTP_SSL(email_sender_host, email_sender_port)

  smtp_server.connect()

  # Login to the smtp server
  smtp_server.login(email_sender_address, email_sender_password)

  # Construct the email message
  message = f'Subject: {subject}\n\n{body}'

  # Send the email
  smtp_server.sendmail(email_sender_address, recipient, message)

  # Disconnect from the server
  smtp_server.quit()

def send_success_email(job, connection, result, *args, **kwargs):
  email = job.meta.get('email')
  subject = 'Your file is ready'

  base_url = os.environ.get('BASE_URL')

  download_url = base_url + "/v1/download/" + job.id
  body = f'Your file is ready. Download it here: {download_url}'

  send_mail(email, subject, body)

def send_failure_email(job, connection, type, value, traceback):
  email = job.meta.get('email')
  subject = 'The transcription failed'

  body = "We're sorry, but we were unable to transcribe the file you uploaded. Please try again or contact the team for assistance."

  send_mail(email, subject, body)