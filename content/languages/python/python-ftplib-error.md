---
title: "[Solution] Python ftplib Error — FTP Connection and Transfer Failures"
description: "Fix Python ftplib errors including FTP.error, timeout, connection refused, 550 errors, and passive mode issues. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 244
---

# Python ftplib Error — FTP Connection and Transfer Failures

The `ftplib` module implements the FTP protocol client. Errors occur during connection, authentication, file transfer, or when the server returns error codes. Common issues include timeouts, permission denied (550 errors), passive mode configuration, and connection refused.

## Common Causes

```python
# Cause 1: Connection refused — server not running or wrong port
from ftplib import FTP

ftp = FTP()
ftp.connect("localhost", 21)  # ConnectionRefusedError if server not running

# Cause 2: Authentication failure
from ftplib import FTP

ftp = FTP("ftp.example.com")
ftp.login("wrong_user", "wrong_pass")  # ftplib.error_perm: 530 Login incorrect

# Cause 3: Timeout on slow connections
from ftplib import FTP

ftp = FTP()
ftp.connect("ftp.example.com", timeout=5)  # TimeoutError if server slow

# Cause 4: File not found (550 error)
from ftplib import FTP

ftp = FTP("ftp.example.com")
ftp.login("user", "pass")
ftp.retrbinary("RETR nonexistent.txt", lambda x: None)  # error_perm: 550 No such file

# Cause 5: Passive mode blocked by firewall
from ftplib import FTP

ftp = FTP("ftp.example.com")
ftp.set_pasv(True)  # May hang or fail if passive ports are blocked
ftp.retrbinary("RETR file.txt", lambda x: None)
```

## How to Fix

### Fix 1: Handle connection errors with retries

```python
from ftplib import FTP, all_errors
import time

def connect_ftp(host, port=21, max_retries=3, timeout=30):
    for attempt in range(max_retries):
        try:
            ftp = FTP()
            ftp.connect(host, port, timeout=timeout)
            return ftp
        except (ConnectionRefusedError, TimeoutError, OSError) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
    raise ConnectionError(f"Failed to connect to {host} after {max_retries} attempts")

ftp = connect_ftp("ftp.example.com")
```

### Fix 2: Handle authentication errors

```python
from ftplib import FTP, error_perm

def safe_login(host, username, password):
    ftp = FTP(host)
    try:
        ftp.login(username, password)
        return ftp
    except error_perm as e:
        if "530" in str(e):
            print("Login failed — check credentials")
        elif "530" in str(e) and "SSL" in str(e):
            print("Server requires FTPS — use FTP_TLS")
        ftp.quit()
        raise

# Use FTPS for secure connections
from ftplib import FTP_TLS

ftps = FTP_TLS("ftp.example.com")
ftps.login("user", "pass")
ftps.prot_p()  # Switch to secure data connection
```

### Fix 3: Set appropriate timeouts

```python
from ftplib import FTP

ftp = FTP()
ftp.connect("ftp.example.com", timeout=60)
ftp.login("user", "pass")

# Set longer timeout for large file transfers
ftp.voidcmd("NOOP")  # Keep-alive
ftp.retrbinary("RETR large_file.zip", lambda x: None, blocksize=8192)
```

### Fix 4: Handle 550 and other file errors

```python
from ftplib import FTP, error_perm, error_temp

def safe_retrieve(ftp, remote_path, local_path):
    try:
        with open(local_path, "wb") as f:
            ftp.retrbinary(f"RETR {remote_path}", f.write)
        return True
    except error_perm as e:
        code = int(str(e).split()[0])
        if code == 550:
            print(f"File not found: {remote_path}")
        elif code == 553:
            print(f"Permission denied: {remote_path}")
        else:
            print(f"FTP error {code}: {e}")
        return False
    except error_temp as e:
        print(f"Temporary error: {e}")
        return False

ftp = FTP("ftp.example.com")
ftp.login("user", "pass")
safe_retrieve(ftp, "data/report.pdf", "local_report.pdf")
```

### Fix 5: Configure passive mode correctly

```python
from ftplib import FTP

ftp = FTP("ftp.example.com")
ftp.login("user", "pass")

# Try passive mode first (default)
ftp.set_pasv(True)
try:
    files = []
    ftp.retrlines("LIST", files.append)
except Exception:
    # Fall back to active mode
    ftp.set_pasv(False)
    files = []
    ftp.retrlines("LIST", files.append)

for line in files:
    print(line)
```

## Examples

```python
# Real-world: Download all files from an FTP directory
from ftplib import FTP
import os

def download_directory(host, user, password, remote_dir, local_dir):
    os.makedirs(local_dir, exist_ok=True)
    ftp = FTP(host)
    ftp.login(user, password)
    ftp.cwd(remote_dir)

    items = []
    ftp.retrlines("LIST", items.append)

    for item in items:
        parts = item.split()
        name = parts[-1]
        if item.startswith("d"):
            # Recursively download subdirectories
            download_directory(host, user, password,
                             f"{remote_dir}/{name}",
                             os.path.join(local_dir, name))
        else:
            local_path = os.path.join(local_dir, name)
            with open(local_path, "wb") as f:
                ftp.retrbinary(f"RETR {name}", f.write)
            print(f"Downloaded: {name}")

    ftp.quit()

# Real-world: Upload file with progress callback
from ftplib import FTP
import os

def upload_with_progress(host, user, password, local_path, remote_path):
    ftp = FTP(host)
    ftp.login(user, password)

    file_size = os.path.getsize(local_path)
    uploaded = [0]

    def callback(data):
        uploaded[0] += len(data)
        progress = (uploaded[0] / file_size) * 100
        print(f"\rProgress: {progress:.1f}%", end="", flush=True)

    with open(local_path, "rb") as f:
        ftp.storbinary(f"STOR {remote_path}", f, callback=callback)

    print()
    ftp.quit()
```

## Related Errors

- [ConnectionError](/languages/python/connectionerror/) — network connectivity issues
- [TimeoutError](/languages/python/timeouterror/) — operation timed out
- [PermissionError](/languages/python/permissionerror/) — local file access denied
