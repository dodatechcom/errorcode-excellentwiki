---
title: "[Solution] Linux SSH Host Key Verification Failed — Fix"
description: "Fix Linux 'WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED' SSH host key errors. Manage known_hosts entries securely."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["ssh", "host-key", "known-hosts", "man-in-the-middle", "security"]
weight: 5
---

# Linux: SSH Host key verification failed

The `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED` error means the SSH server's host key does not match the key stored in your `~/.ssh/known_hosts` file. This can indicate a legitimate host key rotation or a man-in-the-middle attack.

## Common Causes

- Server operating system reinstall (generates new host keys)
- Server IP address reassigned to a different machine
- Container or VM rebuilt with new keys
- DHCP conflict (different machine now has the server's IP)
- Man-in-the-middle attack (rare but serious)
- `~/.ssh/known_hosts` corruption

## How to Fix

### 1. Verify the Host Identity

```bash
# First, verify it's the correct host
ssh -o StrictHostKeyChecking=accept-new user@host

# Check the new host key fingerprint
ssh-keyscan -t rsa host 2>/dev/null | ssh-keygen -lf -

# Compare with the server's actual fingerprint (on the server)
ssh-keygen -lf /etc/ssh/ssh_host_rsa_key.pub
```

### 2. Remove the Old Key (If Change Is Legitimate)

```bash
# Remove the old key for the host
ssh-keygen -R hostname

# Remove by hostname and IP
ssh-keygen -R hostname
ssh-keygen -R 192.168.1.100

# Remove from known_hosts.old if it exists
ssh-keygen -R hostname -f ~/.ssh/known_hosts.old
```

### 3. Accept the New Key Automatically

```bash
# Accept the new key and connect
ssh -o StrictHostKeyChecking=accept-new user@host

# Or update known_hosts in one step
ssh-keyscan hostname >> ~/.ssh/known_hosts
```

### 4. Check for DNS Spoofing or IP Changes

```bash
# Resolve the hostname
host hostname
dig hostname

# Check the server's actual IP
ping -c 1 hostname

# Add the correct entry to /etc/hosts if needed
echo "192.168.1.100 hostname" | sudo tee -a /etc/hosts
```

### 5. Disable Host Key Checking (Not Recommended)

```bash
# For testing only — this is insecure
ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null user@host
```

### 6. Automate Host Key Management (Ansible/Docker)

For infrastructure that spins up frequently:

```bash
# Generate a known_hosts file programmatically
ssh-keyscan -H hostname >> known_hosts

# For Ansible, set in ansible.cfg
# host_key_checking = False
```

## Examples

```bash
$ ssh user@server
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Add correct host key in /home/user/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /home/user/.ssh/known_hosts:5

$ ssh-keygen -R server
# Host server found: line 5
/home/user/.ssh/known_hosts updated.

$ ssh user@server
The authenticity of host 'server' can't be established.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'server' (ED25519) to the list of known hosts.
```

## Related Errors

- [SSH permission denied]({{< relref "/os/linux/ssh-error" >}}) — Authentication failures
- [SSH connection refused]({{< relref "/os/linux/linux-ssh-connection-refused" >}}) — SSH server not listening
- [SSH connection timed out]({{< relref "/os/linux/linux-ssh-timeout" >}}) — Network unreachable
