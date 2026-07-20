---
title: "[Solution] Python Paramiko Error — SSH Connection Failures"
description: "Fix Python Paramiko errors like AuthenticationException, SSHException, socket errors, and key errors. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 427
---

# Python Paramiko Error — SSH Connection Failures

Paramiko errors occur when SSH authentication fails, host keys cannot be verified, connections are refused, or key file formats are invalid. These are common in remote server management and deployment automation.

## Common Causes

```python
# AuthenticationException: wrong password or key
import paramiko
client = paramiko.SSHClient()
client.connect("example.com", username="user", password="wrongpassword")

# SSHException: host key verification failed
client = paramiko.SSHClient()
client.connect("example.com")  # unknown host key

# socket.error: connection refused
client.connect("192.168.1.999", port=22)  # wrong IP or SSH not running

# SSHException: key file format invalid
client.connect("example.com", key_filename="/path/to/not-a-key.txt")

# ChannelException: channel already closed
stdin, stdout, stderr = client.exec_command("ls")
client.close()
stdout.read()  # channel already closed
```

## How to Fix

### Fix 1: Handle Host Key Verification
Set the policy for unknown host keys appropriately.
```python
import paramiko

client = paramiko.SSHClient()
# Auto-accept (convenient but less secure)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Or load known hosts
client.load_system_host_keys()
client.connect("example.com", username="user")
```

### Fix 2: Use Key-Based Authentication
Use SSH keys instead of passwords for more reliable authentication.
```python
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

private_key = paramiko.RSAKey.from_private_key_file("/home/user/.ssh/id_rsa")
client.connect("example.com", username="user", pkey=private_key)
```

### Fix 3: Verify Connection Before Running Commands
Check that the connection is active before executing commands.
```python
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("example.com", username="user", key_filename="/home/user/.ssh/id_rsa")

transport = client.get_transport()
if transport and transport.is_active():
    stdin, stdout, stderr = client.exec_command("ls -la")
    print(stdout.read().decode())
else:
    print("SSH connection not active")

client.close()
```

### Fix 4: Handle Socket Errors with Retry
Implement retry logic for transient network issues.
```python
import paramiko
import socket

def ssh_connect(host, username, key_path, retries=3):
    for attempt in range(retries):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host, username=username, key_filename=key_path, timeout=10)
            return client
        except socket.error as e:
            print(f"Connection attempt {attempt + 1} failed: {e}")
            if attempt == retries - 1:
                raise
    return None
```

### Fix 5: Use Ed25519 Keys for Modern SSH
Support newer key types alongside RSA.
```python
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Ed25519 key
private_key = paramiko.Ed25519Key.from_private_key_file("/home/user/.ssh/id_ed25519")
client.connect("example.com", username="user", pkey=private_key)
```

## Examples

```python
# Remote command execution with error handling
import paramiko

def run_remote_command(host, user, key_path, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, username=user, key_filename=key_path, timeout=10)
        stdin, stdout, stderr = client.exec_command(command, timeout=30)
        exit_status = stdout.channel.recv_exit_status()
        output = stdout.read().decode()
        errors = stderr.read().decode()
        return {"status": exit_status, "output": output, "error": errors}
    except paramiko.AuthenticationException:
        return {"status": -1, "output": "", "error": "Authentication failed"}
    except paramiko.SSHException as e:
        return {"status": -1, "output": "", "error": f"SSH error: {e}"}
    finally:
        client.close()
```

## Related Errors

- [Python boto3 Error](/languages/python/python-boto3-error/)
- [Python redis-py Error](/languages/python/python-redis-py-error/)
- [Python kafka-python Error](/languages/python/python-kafka-python-error/)
