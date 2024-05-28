import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, smtp_server, port, sender_email, password):
        self.smtp_server = smtp_server
        self.port = port
        self.sender_email = sender_email
        self.password = password

    def send_email(self, subject, body, to_email):
        try:
            # Create a multipart message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = to_email
            msg['Subject'] = subject

            # Add body to email
            msg.attach(MIMEText(body, 'html'))

            # Log in to the server and send email
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Secure the connection
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, to_email, msg.as_string())
            print(f"Email sent successfully to {to_email}")
        except Exception as e:
            print(f"Error sending email to {to_email}: {e}")

def create_html_email_body(survey_link):
    return f"""
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>استبيان أهداف التنمية المستدامة</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            direction: rtl;
            text-align: right;
        }}
        .email-container {{
            max-width: 600px;
            margin: 20px auto;
            background-color: #ffffff;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 8px;
        }}
        h1 {{
            color: #333;
        }}
        p {{
            color: #666;
            line-height: 1.6;
        }}
        .cta-button {{
            display: inline-block;
            background-color: #28a745;
            color: #ffffff;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 4px;
            margin-top: 20px;
            font-size: 16px;
        }}
        .cta-button:hover {{
            background-color: #218838;
        }}
    </style>
</head>
<body>
    <div class="email-container">
        <h1>شارك في استبيان أهداف التنمية المستدامة</h1>
        <p>عزيزي/عزيزتي،</p>
        <p>نحن نعمل على تحقيق أهداف التنمية المستدامة، ونود سماع آرائك واقتراحاتك من خلال هذا الاستبيان. سيساعدنا ذلك في تحسين جهودنا وضمان أننا نسير في الاتجاه الصحيح لتحقيق مستقبل أفضل للجميع.</p>
        <p>يرجى النقر على الزر أدناه لملء الاستبيان. شكراً لمشاركتك القيمة.</p>
        <a href="{survey_link}" class="cta-button">ملء الاستبيان</a>
    </div>
</body>
</html>"""

def main():
    # Gmail SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    port = 587  # For starttls
    sender_email = 'howto4prob@gmail.com'
    password = 'ddlbukjchdoadplp'

    # Create an instance of EmailSender
    email_sender = EmailSender(smtp_server, port, sender_email, password)

    # Read email data from CSV
    try:
        emails_df = pd.read_csv('contacts/emails.csv')
        subject = 'ODD'
        survey_link = "https://forms.fillout.com/t/owxwseT6C3uss"
        for index, row in emails_df.iterrows():
            to_email = row['to']
            # Send email
            body = create_html_email_body(survey_link)
            email_sender.send_email(subject, body, to_email)
    except FileNotFoundError:
        print("Error: CSV file not found.")

if __name__ == "__main__":
    main()
