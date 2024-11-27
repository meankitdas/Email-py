import smtplib
import pandas as pd
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(to_email, subject, body, from_email, password):
    try:
        # Set up the server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, password)

        # Create the email
        msg = MIMEMultipart()
        msg["From"] = from_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Send the email
        server.send_message(msg)
        print(f"Email sent to {to_email}")

        # Close the server
        server.quit()
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {e}")


def process_file(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)["email"].tolist()
    elif file_path.endswith(".json"):
        with open(file_path, "r") as file:
            data = json.load(file)
            return [item["email"] for item in data]
    else:
        raise ValueError("Unsupported file format. Please use CSV or JSON.")


def main():
    # Input your Gmail credentials
    from_email = input("Enter your Gmail address: ")
    password = input("Enter your Gmail password (or app password): ")
    # from_email = input("Enter your Gmail address: ")
    # password = input("Enter your Gmail password (or app password): ")

    # Email template
    subject = "Your Subject Here"
    body = """\
    Dear User,

    This is a test email sent using Python.

    Best regards,
    Your Company
    """

    # File input
    file_path = input("Enter the path to your CSV or JSON file: ")
    try:
        email_list = process_file(file_path)
        print(f"Emails to be sent: {len(email_list)}")
        for email in email_list:
            send_email(email, subject, body, from_email, password)
    except Exception as e:
        print(f"Error processing file: {e}")


if __name__ == "__main__":
    main()
