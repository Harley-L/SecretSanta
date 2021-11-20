from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email, smtplib, ssl

def send_email(email, name, content):
    subject = "Secret Santa"
    file = open("sample_email.txt")
    body = file.read().replace("{RECIPIENT}", name).replace("{SS}", content)
    file.close()
    sender_email = email_to_send_with
    receiver_email = email
    password = password_of_sender_email

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Add attachment to message and convert message to string
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)