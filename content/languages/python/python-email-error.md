---
title: "[Solution] Python email Module Error — Parse, MIME, and Header Issues"
description: "Fix Python email module errors including parser failures, MIME construction, header encoding, and charset problems. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 241
---

# Python email Module Error — Parse, MIME, and Header Issues

The `email` module in Python's standard library handles parsing, constructing, and encoding email messages. Errors arise when malformed messages are parsed, MIME parts are assembled incorrectly, headers contain invalid characters, or character set conversions fail.

## Common Causes

```python
# Cause 1: Parsing a malformed email message
from email.parser import Parser

parser = Parser()
# Missing required headers or malformed raw string
raw_email = "This is not a valid email message"
msg = parser.parsestr(raw_email)
print(msg["Subject"])  # Returns None — no subject header

# Cause 2: Incorrect MIME multipart construction
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg.attach(MIMEText("Hello", "plain"))
msg.attach(MIMEText("<h1>Hello</h1>", "html"))
# Forgetting to set subject or from — results in incomplete headers

# Cause 3: Header encoding with non-ASCII characters
from email.header import Header

# Fails if charset is not specified for non-ASCII text
header = Header("こんにちは世界")  # May raise LookupError if encoding fails

# Cause 4: Invalid Message-ID format
from email.utils import formatdate

# Message-ID without angle brackets
msgid = "abc123.example.com"  # Should be <abc123@example.com>

# Cause 5: Charset conversion errors
from email.charset import Charset

cs = Charset("utf-8")
# Trying to encode characters not supported by the target charset
encoded = cs.body_encode("Ünïcödé text")  # May fail with charset mismatch
```

## How to Fix

### Fix 1: Handle parser errors with boundary detection

```python
from email import policy
from email.parser import BytesParser

# Use the modern policy-based parser
with open("message.eml", "rb") as f:
    msg = BytesParser(policy=policy.default).parse(f)

# Check for missing headers safely
subject = msg.get("Subject", "No Subject")
sender = msg.get("From", "unknown@example.com")
print(f"From: {sender}, Subject: {subject}")
```

### Fix 2: Build MIME messages correctly

```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()
msg["Subject"] = "Report"
msg["From"] = "sender@example.com"
msg["To"] = "receiver@example.com"

msg.attach(MIMEText("Plain text body", "plain"))
msg.attach(MIMEText("<h1>HTML body</h1>", "html"))

# Attach a file properly
with open("report.pdf", "rb") as f:
    part = MIMEBase("application", "pdf")
    part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment", filename="report.pdf")
    msg.attach(part)
```

### Fix 3: Encode headers with the correct charset

```python
from email.header import Header

# Explicitly specify the charset
subject = Header("Report — Résumé attachment", "utf-8")
msg["Subject"] = subject

# Use email.utils for proper address formatting
from email.utils import formataddr, parseaddr

name, addr = parseaddr("Sender <sender@example.com>")
formatted = formataddr((name, addr), charset="utf-8")
```

### Fix 4: Generate valid Message-IDs

```python
from email.utils import formatdate, make_msgid
import socket

# Use make_msgid for RFC-compliant Message-IDs
domain = socket.getfqdn()
msgid = make_msgid(domain=domain)
print(msgid)  # <unique-string@example.com>

# Use formatdate for timestamps
date_header = formatdate(localtime=True)
```

### Fix 5: Handle charset errors in message bodies

```python
from email import policy
from email.parser import BytesParser

with open("message.eml", "rb") as f:
    msg = BytesParser(policy=policy.default).parse(f)

# Safely extract body with charset fallback
if msg.is_multipart():
    for part in msg.walk():
        content_type = part.get_content_type()
        charset = part.get_content_charset() or "utf-8"
        try:
            body = part.get_content()
        except (LookupError, UnicodeDecodeError):
            body = part.get_payload(decode=True).decode("latin-1", errors="replace")
        print(f"[{content_type}] {body}")
else:
    charset = msg.get_content_charset() or "utf-8"
    body = msg.get_content()
    print(body)
```

## Examples

```python
# Real-world: Parse an email from a file and extract attachments
from email import policy
from email.parser import BytesParser
import os

def parse_email(filepath):
    with open(filepath, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    result = {
        "subject": msg.get("Subject", ""),
        "from": msg.get("From", ""),
        "to": msg.get("To", ""),
        "date": msg.get("Date", ""),
        "attachments": [],
    }

    for part in msg.walk():
        if part.get_content_maintype() == "multipart":
            continue
        if part.get("Content-Disposition") is None:
            continue
        filename = part.get_filename()
        if filename:
            result["attachments"].append(filename)

    return result

# Real-world: Send a properly formatted MIME email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_addr, subject, body, attachment_path=None):
    msg = MIMEMultipart()
    msg["From"] = "sender@example.com"
    msg["To"] = to_addr
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    if attachment_path:
        from email.mime.base import MIMEBase
        from email import encoders
        with open(attachment_path, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f'attachment; filename="{os.path.basename(attachment_path)}"')
        msg.attach(part)

    with smtplib.SMTP("localhost") as server:
        server.send_message(msg)
```

## Related Errors

- [UnicodeDecodeError](/languages/python/unicodedecodeerror/) — character decoding failures in email bodies
- [smtplib errors](/languages/python/smtplib-error/) — SMTP transport errors when sending email
- [FileNotFoundError](/languages/python/filenotfounderror/) — missing attachment files
