---
title: "Flask-Mail SMTP Error"
description: "Flask-Mail raises SMTP errors when email sending fails due to connection, authentication, or configuration issues"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["mail", "smtp", "email", "notification", "flask"]
weight: 5
---

## What This Error Means

Flask-Mail errors occur when the SMTP server connection fails, authentication is rejected, or email messages are malformed. These errors typically manifest as `SMTPException`, `ConnectionRefusedError`, or `SMTPAuthenticationError`.

## Common Causes

- SMTP server connection refused (server not running)
- Invalid SMTP credentials (username/password)
- TLS/SSL configuration mismatch
- Email address validation failure
- Message exceeds size limits

## How to Fix

Configure Flask-Mail properly:

```python
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'noreply@example.com'

mail = Mail(app)
```

Send emails with error handling:

```python
from flask_mail import Mail, Message
import logging

@app.route('/send-notification', methods=['POST'])
def send_notification():
    msg = Message(
        subject='Notification',
        recipients=[request.form['email']],
        body='You have a new notification.'
    )
    try:
        mail.send(msg)
        return jsonify({'status': 'sent'}), 200
    except Exception as e:
        logging.error(f"Email send failed: {e}")
        return jsonify({'status': 'failed', 'error': str(e)}), 500
```

Use environment variables for credentials:

```python
import os

app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
```

Test SMTP connection:

```python
import smtplib

def test_smtp():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('user@gmail.com', 'app-password')
        server.quit()
        print("SMTP connection successful")
    except Exception as e:
        print(f"SMTP connection failed: {e}")
```

## Examples

```python
msg = Message('Hello', recipients=['invalid-email'])
mail.send(msg)
```

```text
smtplib.SMTPRecipientsRefused: {'invalid-email': (550, b'Rejected - invalid recipient')}
```

## Related Errors

- [Configuration error]({{< relref "/frameworks/flask/config-error" >}})
- [Import error]({{< relref "/frameworks/flask/import-error" >}})
