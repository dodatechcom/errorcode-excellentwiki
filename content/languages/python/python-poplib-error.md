---
title: "[Solution] Python poplib Error — POP3 Connection and Retrieval Failures"
description: "Fix Python poplib errors including POP.error, POP3 timeout, authentication failures, and message retrieval errors. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 247
---

# Python poplib Error — POP3 Connection and Retrieval Failures

The `poplib` module implements the POP3 protocol for retrieving email from servers. Errors occur during connection, authentication, message listing, retrieval, or deletion. POP3 is simpler than IMAP but still faces timeout, permission, and network issues.

## Common Causes

```python
# Cause 1: Connection timeout
import poplib

server = poplib.POP3_SSL("pop.example.com", timeout=10)  # TimeoutError if slow

# Cause 2: Authentication failure
import poplib

server = poplib.POP3_SSL("pop.gmail.com", 995)
server.user("user@gmail.com")
server.pass_("wrong_password")  # poplib.error_proto: -ERR [AUTH] Invalid credentials

# Cause 3: Message not found
import poplib

server = poplib.POP3_SSL("pop.gmail.com", 995)
server.user("user@gmail.com")
server.pass_("app-password")
server.retr(99999)  # poplib.error_proto: -ERR No such message

# Cause 4: Connection refused
import poplib

server = poplib.POP3_SSL("pop.example.com", 995)  # ConnectionRefusedError

# Cause 5: Server busy or too many connections
import poplib

server = poplib.POP3_SSL("pop.gmail.com", 995)
server.user("user@gmail.com")
server.pass_("app-password")  # error_proto: -ERR Too many connections
```

## How to Fix

### Fix 1: Handle connection errors with timeout

```python
import poplib
from poplib import POP3, POP3_SSL, error_proto

def connect_pop3(host, port=995, username=None, password=None, ssl=True, timeout=60):
    try:
        if ssl:
            server = POP3_SSL(host, port, timeout=timeout)
        else:
            server = POP3(host, port, timeout=timeout)

        if username and password:
            server.user(username)
            server.pass_(password)
        return server
    except error_proto as e:
        error_msg = str(e)
        if "AUTH" in error_msg:
            print("Authentication failed — check credentials")
        elif "DENIED" in error_msg:
            print("Access denied — check account settings")
        raise
    except (ConnectionRefusedError, OSError) as e:
        print(f"Connection failed: {e}")
        raise

server = connect_pop3("pop.gmail.com", 995, "user@gmail.com", "app-password")
```

### Fix 2: Handle message retrieval errors

```python
import poplib
from poplib import error_proto

def safe_retrieve(server, msg_num):
    try:
        response, lines, octets = server.retr(msg_num)
        if response.startswith(b"+OK"):
            from email import message_from_bytes
            raw_email = b"\r\n".join(lines)
            return message_from_bytes(raw_email)
        else:
            print(f"Failed to retrieve message {msg_num}: {response}")
            return None
    except error_proto as e:
        if "No such message" in str(e):
            print(f"Message {msg_num} does not exist")
        else:
            print(f"POP3 error: {e}")
        return None
    except IndexError:
        print(f"Invalid message number: {msg_num}")
        return None

server = connect_pop3("pop.gmail.com", 995, "user@gmail.com", "app-password")
count, size = server.stat()
if count > 0:
    msg = safe_retrieve(server, 1)
```

### Fix 3: List messages safely

```python
import poplib

def list_messages(server):
    try:
        count, size = server.stat()
        print(f"Inbox: {count} messages, {size} bytes")

        response, messages, octets = server.list()
        if response.startswith(b"+OK"):
            for msg_info in messages:
                num, size = msg_info.split()
                print(f"  Message {num.decode()}: {size.decode()} bytes")
            return count
        return 0
    except poplib.error_proto as e:
        print(f"Error listing messages: {e}")
        return 0

server = connect_pop3("pop.gmail.com", 995, "user@gmail.com", "app-password")
list_messages(server)
```

### Fix 4: Delete messages safely

```python
import poplib

def safe_delete(server, msg_num):
    try:
        response = server.dele(msg_num)
        if response.startswith(b"+OK"):
            print(f"Message {msg_num} marked for deletion")
            return True
        else:
            print(f"Failed to delete message {msg_num}: {response}")
            return False
    except poplib.error_proto as e:
        print(f"Error deleting message: {e}")
        return False

def commit_deletions(server):
    try:
        server.quit()  # QUIT commits deletions
    except poplib.error_proto:
        pass  # Server may close connection after QUIT

server = connect_pop3("pop.gmail.com", 995, "user@gmail.com", "app-password")
safe_delete(server, 1)
commit_deletions(server)
```

### Fix 5: Use TOP for preview without downloading full message

```python
import poplib
from email import message_from_bytes

def preview_message(server, msg_num, lines=10):
    try:
        response, header_lines, octets = server.top(msg_num, lines)
        if response.startswith(b"+OK"):
            raw_header = b"\r\n".join(header_lines)
            msg = message_from_bytes(raw_header)
            return {
                "subject": msg.get("Subject", ""),
                "from": msg.get("From", ""),
                "date": msg.get("Date", ""),
            }
        return None
    except poplib.error_proto as e:
        print(f"Error previewing message: {e}")
        return None

server = connect_pop3("pop.gmail.com", 995, "user@gmail.com", "app-password")
preview = preview_message(server, 1)
if preview:
    print(f"Subject: {preview['subject']}")
```

## Examples

```python
# Real-world: Download all messages from POP3 server
import poplib
from email import message_from_bytes
import os

def download_all_messages(host, user, password, save_dir="pop3_emails"):
    os.makedirs(save_dir, exist_ok=True)

    server = poplib.POP3_SSL(host, 995, timeout=60)
    server.user(user)
    server.pass_(password)

    count, total_size = server.stat()
    print(f"Downloading {count} messages...")

    for i in range(1, count + 1):
        try:
            response, lines, octets = server.retr(i)
            raw_email = b"\r\n".join(lines)
            msg = message_from_bytes(raw_email)

            subject = msg.get("Subject", "no-subject")
            safe_subject = "".join(c if c.isalnum() or c in " -_" else "" for c in subject)
            filepath = os.path.join(save_dir, f"{i:04d}_{safe_subject[:50]}.eml")

            with open(filepath, "wb") as f:
                f.write(raw_email)
            print(f"  Downloaded: {subject[:60]}")
        except poplib.error_proto as e:
            print(f"  Failed message {i}: {e}")

    server.quit()
```

## Related Errors

- [ConnectionError](/languages/python/connectionerror/) — network connectivity issues
- [TimeoutError](/languages/python/timeouterror/) — operation timed out
- [OSError](/languages/python/oserror/) — system-level I/O errors
