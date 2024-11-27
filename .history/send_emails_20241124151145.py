import smtplib
import pandas as pd
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


body = """\
<html>
  <head>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap");

      body {
        font-family: "Poppins", Arial, sans-serif;
        color: #333333;
        line-height: 1.6;
        margin: 0;
        padding: 0;
        background-color: #f4f4f9;
      }
      .container {
        width: 100%;
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        animation: fadeIn 1s ease-in-out;
      }
      @keyframes fadeIn {
        from {
          opacity: 0;
          transform: translateY(-10px);
        }
        to {
          opacity: 1;
          transform: translateY(0);
        }
      }
      .header {
        text-align: center;
        background-color: #254381;
        color: #ffffff;
        padding: 20px;
        border-radius: 8px 8px 0 0;
        animation: slideDown 1s ease-out;
      }
      @keyframes slideDown {
        from {
          transform: translateY(-20px);
        }
        to {
          transform: translateY(0);
        }
      }
      .header .logo-container {
        background-color: #ffffff;
        display: inline-block;
        padding: 10px;
        margin-bottom: 10px;
      }
      .header img {
        max-width: 120px;
        display: block;
      }
      .header h1 {
        margin: 0;
        font-size: 24px;
        font-weight: 600;
      }
      .content {
        padding: 20px;
        animation: fadeInContent 1.5s ease-in-out;
      }
      @keyframes fadeInContent {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }
      .content h2 {
        color: #254381;
        font-size: 20px;
        font-weight: 600;
      }
      .content ul {
        margin: 10px 0;
        padding-left: 20px;
      }
      .content ul li {
        margin-bottom: 8px;
      }
      .footer {
        text-align: center;
        font-size: 14px;
        color: #666666;
        padding: 10px;
        border-top: 1px solid #e0e0e0;
        margin-top: 20px;
        animation: fadeInFooter 2s ease-in;
      }
      @keyframes fadeInFooter {
        from {
          opacity: 0;
          transform: scale(0.95);
        }
        to {
          opacity: 1;
          transform: scale(1);
        }
      }
      a {
        color: #254381;
        text-decoration: none;
        font-weight: 600;
      }
      .whatsapp-button {
        display: inline-block;
        background-color: #254381;
        color: #ffffff;
        padding: 15px 25px;
        font-size: 16px;
        font-weight: 600;
        border-radius: 8px;
        text-align: center;
        margin: 20px 0;
        text-decoration: none;
        transition: background-color 0.3s ease;
      }
      .whatsapp-button:hover {
        background-color: #1f3760;
        color: #ffffff;
      }
      #under-line {
        text-decoration: underline;
        cursor: pointer;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="header">
        <div class="logo-container">
          <img
            src="https://www.jainuniversity.ac.in/jain/home/assets/images/jain-logo.png"
            alt="Jain University Logo"
          />
        </div>
        <h1>Make-A-Thon 2024</h1>
        <p>Innovation. Creativity. Entrepreneurship.</p>
      </div>
      <div class="content">
        <p>Dear Participant,</p>
        <p>
          We are thrilled to invite you to
          <strong>Entrepreneurship Week 2024</strong>, organized by the CRCE
          Cells across all Jain University campuses! The highlight of this week
          is our flagship event, the <strong>Make-A-Thon</strong>, happening on
          <strong>25th November 2024</strong> at the
          <strong>Jain University Global Campus</strong>.
        </p>
        <h2>About the Event</h2>
        <p>
          The <strong>Make-A-Thon</strong> is a 24-hour
          <strong>Innovation Marathon</strong>, where teams will present and
          develop <em>tech-innovative ideas</em>—hardware or software-based.
          Showcase your <strong>creativity</strong>,
          <strong>technical skills</strong>, and
          <strong>problem-solving prowess</strong> in a vibrant, competitive
          environment.
        </p>
        <h2>Event Timeline</h2>
        <ul>
          <li><strong>Reporting Time:</strong> 7:45 AM</li>
          <li>
            <strong>Registration:</strong> 8:00 AM - 9:00 AM (Reception Area,
            Jain University Global Campus)
          </li>
          <li><strong>Event Start:</strong> 9:20 AM</li>
        </ul>
        <p>
          <em
            >Ensure you report promptly by 7:45 AM for a smooth registration
            process.</em
          >
        </p>
        <h2>What to Bring</h2>
        <ul>
          <li><strong>ID Card</strong> (compulsory)</li>
          <li><strong>Laptops</strong> and other required devices</li>
          <li><strong>Extension cords</strong> and chargers</li>
          <li>Project-specific materials</li>
          <li>Personal essentials for the 24-hour event</li>
          <li>Medications (if needed)</li>
        </ul>
        <p>
          <em
            >Food and snacks will be provided throughout the event to keep you
            energized.</em
          >
        </p>
        <h2>Important Links</h2>
        <p>
          <a href="https://bit.ly/412TUFg" id="under-line"
            >Rules and Regulations</a
          ><br />
          <a href="https://bit.ly/3CANSRZ" id="under-line"
            >Make-A-Thon Guidelines</a
          >
        </p>
        <h2>Contact Information</h2>
        <p>
          <strong>Bhavishi Kaushik</strong> (Secretary CRCE) | +91 86186
          90536<br />
          <strong>Udit Agrawal</strong> (Secretary CRCE) | +91 62605 05192
        </p>
        <p>
          We look forward to seeing your innovative ideas come to life. Let’s
          make this event an unforgettable success!
        </p>

        <!-- WhatsApp Join Section -->
        <div class="whatsapp-section">
          <h2>Join Our WhatsApp Group</h2>
          <p>
            Stay updated with event announcements and connect with other
            participants. Join the official WhatsApp group below:
          </p>
          <a
            href="https://chat.whatsapp.com/Cm07rl6PchyEXeaHCrenil"
            class="whatsapp-button"
            target="_blank"
            >Join WhatsApp Group</a
          >
        </div>
      </div>
      <div class="footer">
        <p>
          <strong>Make-A-Thon 2024</strong><br />Organized by CRCE Cell, Jain
          University Global Campus
        </p>
        <p>
          <em
            >If you received this email by mistake, please contact us to
            unsubscribe.</em
          >
        </p>
      </div>
    </div>
  </body>
</html>

"""


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
        msg.attach(MIMEText(body, "html"))

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
    from_email = "udit.2012005@gmail.com"
    password = "ywco zqaq kobd jezi"
    # from_email = input("Enter your Gmail address: ")
    # password = input("Enter your Gmail password (or app password): ")

    # Email template
    subject = "Your Subject Here"
    # body = body

    # File input
    file_path = "./email.csv"
    try:
        email_list = process_file(file_path)
        print(f"Emails to be sent: {len(email_list)}")
        for email in email_list:
            send_email(email, subject, body, from_email, password)
    except Exception as e:
        print(f"Error processing file: {e}")


if __name__ == "__main__":
    main()
