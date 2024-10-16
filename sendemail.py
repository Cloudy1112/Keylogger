import smtplib, ssl
from email.mime.text import MIMEText

def sendEmail(message):
    sender_email = "{yourmail}"
    password = "{yourpass}"
    receiver_email = "{yourmail}"

    try:
        # Create a secure SMTP connection
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)

            # Create the email message
            email = MIMEText(message)
            email['From'] = sender_email
            email['To'] = receiver_email

            # Send the email
            server.sendmail(sender_email, receiver_email, email.as_string())
            server.quit()
            print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred while sending email: {e}")