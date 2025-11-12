import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()


def send_mail():
    smtp_server = "smtp.protonmail.ch"
    port = 465  # SSL port
    sender_email = "np-reply@panado.dev"
    receiver_email = "panado@panado.dev"  # Change this to your desired recipient
    password = os.getenv("SMTP_TOKEN")

    if not password:
        print("Error: SMTP_TOKEN environment variable not set.")
        return

    # Create the email
    message = MIMEMultipart("alternative")
    message["Subject"] = "Test Email from Python"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Plain text version
    text = """\
Hi there,

This is a test email sent from the Python SMTP script.
If you're seeing this, the SMTP connection and credentials are working!

Regards,
Panado Bot
"""

    # HTML version
    html = """\
<html>
<body style="font-family: sans-serif;">
    <h2>SMTP Test Email</h2>
    <p>This is a <b>test email</b> sent from your Python script.</p>
    <p>If you're reading this, everything is working</p>
    <hr>
    <p style="font-size: 12px; color: #666;">Sent automatically by Panado Bot</p>
</body>
</html>
"""

    # Attach both versions
    message.attach(MIMEText(text, "plain"))
    message.attach(MIMEText(html, "html"))

    # Send the email securely
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.send_message(message)
            print(f"Test email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("Starting program...")
    send_mail()
    print("Done")
