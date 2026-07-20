---
title: "[Solution] Python imaplib Error — IMAP Connection and Mailbox Failures"
description: "Fix Python imaplib errors including IMAP4.error, IMAP4.abort, IMAP4.readonly, login failures, and folder selection issues. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 246
---

# Python imaplib Error — IMAP Connection and Mailbox Failures

The `imaplib` module implements the IMAP4 and IMAP4rev1 protocols for accessing mailboxes. Errors occur during connection, authentication, folder selection, message fetching, or when the server returns error responses.

## Common Causes

```python
# Cause 1: Connection failure
import imaplib

mail = imaplib.IMAP4("imap.example.com", 143)  # ConnectionRefusedError

# Cause 2: Login failure
import imaplib

mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
mail.login("user@gmail.com", "wrong_password")  # IMAP4.error: [AUTHENTICATIONFAILED]

# Cause 3: Folder not found
import imaplib

mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
mail.login("user@gmail.com", "app-password")
status, data = mail.select("NonExistentFolder")  # IMAP4.error: [NONEXISTENT]

# Cause 4: Read-only folder access
import imaplib

mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
mail.login("user@gmail.com", "app-password")
mail.select("Sent", readonly=False)  # IMAP4.readonly: [CANNOT] Folder is read-only

# Cause 5: Server abort on connection loss
import imaplib

mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
# Network interruption during operation
mail.search(None, "ALL")  # IMAP4.abort: socket error
```

## How to Fix

### Fix 1: Handle connection and login errors

```python
import imaplib
from imaplib import IMAP4, IMAP4_SSL, IMAP4.error

def connect_imap(host, port=993, username=None, password=None, ssl=True):
    try:
        if ssl:
            mail = IMAP4_SSL(host, port, timeout=30)
        else:
            mail = IMAP4(host, port, timeout=30)

        if username and password:
            mail.login(username, password)
        return mail
    except IMAP4.error as e:
        if "AUTHENTICATIONFAILED" in str(e):
            print("Login failed — check credentials")
        elif "LOGIN" in str(e):
            print("Server requires LOGIN command")
        raise
    except (ConnectionRefusedError, OSError) as e:
        print(f"Connection failed: {e}")
        raise

mail = connect_imap("imap.gmail.com", 993, "user@gmail.com", "app-password")
```

### Fix 2: Select folders safely

```python
import imaplib

def safe_select_folder(mail, folder="INBOX"):
    try:
        status, data = mail.select(folder, readonly=True)
        if status == "OK":
            count = int(data[0])
            print(f"Selected {folder}: {count} messages")
            return True
        else:
            print(f"Failed to select {folder}: {data}")
            return False
    except imaplib.IMAP4.error as e:
        if "NONEXISTENT" in str(e):
            print(f"Folder '{folder}' does not exist")
        elif "READ-ONLY" in str(e):
            print(f"Folder '{folder}' is read-only")
        else:
            print(f"Error selecting folder: {e}")
        return False

mail = connect_imap("imap.gmail.com", 993, "user@gmail.com", "pass")
safe_select_folder(mail, "INBOX")
safe_select_folder(mail, "[Gmail]/Sent Mail")
```

### Fix 3: Handle read-only access

```python
import imaplib

def select_writable(mail, folder):
    try:
        status, data = mail.select(folder, readonly=False)
        if status == "OK":
            return True
    except imaplib.IMAP4.readonly as e:
        print(f"Folder '{folder}' is read-only: {e}")
        # Re-select as readonly
        mail.select(folder, readonly=True)
        return False
    except imaplib.IMAP4.error as e:
        print(f"Error: {e}")
        return False

mail = connect_imap("imap.gmail.com", 993, "user@gmail.com", "pass")
select_writable(mail, "INBOX")
```

### Fix 4: Recover from connection abort

```python
import imaplib
import time

def reconnect_on_abort(func):
    def wrapper(mail, *args, **kwargs):
        try:
            return func(mail, *args, **kwargs)
        except imaplib.IMAP4.abort as e:
            print(f"Connection lost: {e}. Reconnecting...")
            mail.shutdown()
            raise
    return wrapper

@reconnect_on_abort
def search_messages(mail, criteria="ALL"):
    status, data = mail.search(None, criteria)
    if status == "OK":
        return data[0].split()
    return []

# Wrap with reconnection logic
def search_with_retry(host, port, user, password, criteria="ALL"):
    for attempt in range(3):
        try:
            mail = connect_imap(host, port, user, password)
            return search_messages(mail, criteria)
        except imaplib.IMAP4.abort:
            time.sleep(2 ** attempt)
    return []
```

### Fix 5: Fetch messages safely

```python
import imaplib

def safe_fetch(mail, msg_id, parts="RFC822"):
    try:
        status, data = mail.fetch(msg_id, parts)
        if status == "OK":
            return data
        else:
            print(f"Fetch failed: {data}")
            return None
    except imaplib.IMAP4.error as e:
        print(f"Error fetching message: {e}")
        return None

mail = connect_imap("imap.gmail.com", 993, "user@gmail.com", "pass")
mail.select("INBOX")
msg_ids = []
status, data = mail.search(None, "ALL")
if status == "OK":
    msg_ids = data[0].split()

if msg_ids:
    msg = safe_fetch(mail, msg_ids[0])
    if msg:
        print(msg)
```

## Examples

```python
# Real-world: Search and download unread emails
import imaplib
from email import message_from_bytes

def download_unread_emails(host, user, password, save_dir="emails"):
    import os
    os.makedirs(save_dir, exist_ok=True)

    mail = imaplib.IMAP4_SSL(host, 993)
    mail.login(user, password)
    mail.select("INBOX")

    status, data = mail.search(None, "UNSEEN")
    if status != "OK":
        return []

    msg_ids = data[0].split()
    downloaded = []

    for msg_id in msg_ids:
        status, msg_data = mail.fetch(msg_id, "(RFC822)")
        if status == "OK":
            email_body = msg_data[0][1]
            msg = message_from_bytes(email_body)

            subject = msg.get("Subject", "no-subject")
            filename = f"{save_dir}/{msg_id.decode()}.eml"

            with open(filename, "wb") as f:
                f.write(email_body)
            downloaded.append(filename)

    mail.logout()
    return downloaded

# Real-world: List all folders in mailbox
def list_folders(host, user, password):
    mail = imaplib.IMAP4_SSL(host, 993)
    mail.login(user, password)

    status, folders = mail.list()
    if status == "OK":
        for folder in folders:
            print(folder.decode())

    mail.logout()
```

## Related Errors

- [ConnectionError](/languages/python/connectionerror/) — network connectivity issues
- [TimeoutError](/languages/python/timeouterror/) — operation timed out
- [OSError](/languages/python/oserror/) — system-level I/O errors
