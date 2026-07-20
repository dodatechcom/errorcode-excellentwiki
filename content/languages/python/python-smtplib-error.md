---
title: "[Solution] Python smtplib Error — SMTP Connection and Authentication Failures"
description: "Fix Python smtplib errors including SMTPException, SMTPAuthenticationError, SMTPRecipientsRefused, STARTTLS, and connection errors. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 245
---

# Python smtplib Error — SMTP Connection and Authentication Failures

The `smtplib` module defines an SMTP client session object for sending email. Errors arise from connection failures, authentication issues, recipient rejection, STARTTLS negotiation problems, and SMTP server error responses.

## Common Causes

```python
# Cause 1: Connection refused — SMTP server not running
import smtplib

server = smtplib.SMTP("localhost", 25)  # ConnectionRefusedError

# Cause 2: Authentication failure
import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("user@gmail.com", "wrong_password")  # SMTPAuthenticationError

# Cause 3: Recipient rejected by server
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Hello")
msg["Subject"] = "Test"
msg["From"] = "sender@example.com"
msg["To"] = "invalid@nonexistentdomain.com"

server = smtplib.SMTP("smtp.example.com", 587)
server.starttls()
server.login("user", "pass")
server.send_message(msg)  # SMTPRecipientsRefused

# Cause 4: STARTTLS not supported
import smtplib

server = smtplib.SMTP("smtp.example.com", 25)
server.starttls()  # SMTPNotSupportedError on servers without TLS

# Cause 5: DNS resolution failure
import smtplib

server = smtplib.SMTP("nonexistent.smtp.server", 587)  # SMTPConnectError
```

## How to Fix

### Fix 1: Handle connection errors gracefully

```python
import smtplib
from smtplib import SMTPException, SMTPConnectError

def connect_smtp(host, port=587, timeout=30):
    try:
        server = smtplib.SMTP(host, port, timeout=timeout)
        return server
    except SMTPConnectError as e:
        print(f"Failed to connect to {host}:{port}: {e}")
        raise
    except OSError as e:
        print(f"Network error: {e}")
        raise

server = connect_smtp("smtp.gmail.com", 587)
```

### Fix 2: Handle authentication with app passwords

```python
import smtplib
from smtplib import SMTPAuthenticationError

def authenticate_smtp(host, port, username, password):
    server = smtplib.SMTP(host, port)
    server.ehlo()

    try:
        server.starttls()
        server.ehlo()
    except smtplib.SMTPNotSupportedError:
        print("STARTTLS not supported — sending in plaintext")

    try:
        server.login(username, password)
        return server
    except SMTPAuthenticationError as e:
        code, msg = e.args
        if code == 535:
            print("Authentication failed — check credentials or use app password")
        elif code == 534:
            print("Authentication method not allowed — enable less secure apps or use OAuth")
        server.quit()
        raise

# Gmail requires app passwords (not regular password)
server = authenticate_smtp(
    "smtp.gmail.com", 587,
    "user@gmail.com",
    "your-app-password-here"
)
```

### Fix 3: Handle recipient errors individually

```python
import smtplib
from email.mime.text import MIMEText

def send_to_multiple_recipients(server, from_addr, recipients, subject, body):
    results = {"sent": [], "failed": []}

    for recipient in recipients:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = from_addr
        msg["To"] = recipient

        try:
            server.sendmail(from_addr, [recipient], msg.as_string())
            results["sent"].append(recipient)
        except smtplib.SMTPRecipientsRefused as e:
            results["failed"].append((recipient, str(e)))
        except smtplib.SMTPException as e:
            results["failed"].append((recipient, str(e)))

    return results

# Usage
server = smtplib.SMTP("smtp.example.com", 587)
server.starttls()
server.login("user@example.com", "password")
results = send_to_multiple_recipients(
    server, "sender@example.com",
    ["alice@example.com", "bob@example.com"],
    "Update", "Hello team!"
)
print(f"Sent: {results['sent']}, Failed: {results['failed']}")
server.quit()
```

### Fix 4: Configure STARTTLS and SSL properly

```python
import smtplib
from smtplib import SMTPNotSupportedError

def create_secure_connection(host, port=587):
    server = smtplib.SMTP(host, port)
    server.ehlo()

    # Try STARTTLS first
    try:
        server.starttls()
        server.ehlo()
        print("Connected with STARTTLS")
    except SMTPNotSupportedError:
        print("STARTTLS not available")

    return server

# For SMTPS (implicit SSL on port 465)
server = smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30)
server.login("user@gmail.com", "app-password")
server.sendmail("from@example.com", "to@example.com", "Subject: Test\n\nHello")
server.quit()
```

### Fix 5: Use context manager for automatic cleanup

```python
import smtplib
from email.mime.text import MIMEText

def send_email(host, port, username, password, from_addr, to_addr, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr

    try:
        with smtplib.SMTP(host, port, timeout=30) as server:
            server.ehlo()
            try:
                server.starttls()
                server.ehlo()
            except smtplib.SMTPNotSupportedError:
                pass
            server.login(username, password)
            server.send_message(msg)
        return True
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
        return False
```

## Examples

```python
# Real-world: Send email with retry logic
import smtplib
import time
from email.mime.text import MIMEText

def send_with_retry(host, port, username, password, msg, max_retries=3):
    for attempt in range(max_retries):
        try:
            with smtplib.SMTP(host, port, timeout=30) as server:
                server.starttls()
                server.login(username, password)
                server.send_message(msg)
            return True
        except (smtplib.SMTPException, ConnectionError) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
    return False

msg = MIMEText("Hello, this is a test email.")
msg["Subject"] = "Test"
msg["From"] = "sender@example.com"
msg["To"] = "receiver@example.com"

send_with_retry("smtp.example.com", 587, "user", "pass", msg)
```

## Related Errors

- [ConnectionError](/languages/python/connectionerror/) — network connectivity issues
- [TimeoutError](/languages/python/timeouterror/) — operation timed out
- [OSError](/languages/python/oserror/) — system-level I/O errors
