---
title: "[Solution] Ansible Unreachable Host Error — Fix Connectivity"
description: "Fix Ansible UNREACHABLE host errors. Diagnose network issues, SSH timeouts, and host configuration problems with practical solutions."
---

## What This Error Means

The `UNREACHABLE` status means Ansible could not connect to the target host at all. Unlike connection refused (where the port responds but SSH fails), unreachable means no network response was received within the timeout period.

A typical error:

```
host1 | UNREACHABLE! => {
    "changed": false,
    "msg": "Failed to connect to the host via ssh: ssh: connect to host
    192.168.1.10 port 22: Connection timed out",
    "unreachable": true
}
```

## Why It Happens

Host unreachable errors happen when:

- **Host is powered off**: The machine is shut down or crashed.
- **Network routing failure**: No route exists between the Ansible controller and the target.
- **Firewall drops packets**: Firewall silently drops traffic instead of rejecting it.
- **DNS resolution failure**: Hostname resolves to an incorrect or non-existent IP address.
- **Security groups or NACLs**: Cloud network ACLs or security groups block the traffic.

## How to Fix It

**Step 1: Verify basic network connectivity**

```bash
ping -c 4 192.168.1.10
traceroute 192.168.1.10
```

**Step 2: Check DNS resolution**

```bash
nslookup host1.example.com
dig host1.example.com
```

**Step 3: Test SSH with verbose output**

```bash
ssh -vvv user@192.168.1.10
```

**Step 4: Configure SSH timeouts in Ansible**

Increase timeout values for slow networks:

```ini
# ansible.cfg
[defaults]
timeout = 60
remote_tmp = /tmp/.ansible/tmp

[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersist=60s -o ConnectTimeout=30
pipelining = True
```

**Step 5: Use a jump host or bastion**

```ini
[webservers]
web1 ansible_host=10.0.1.10 ansible_ssh_common_args='-o ProxyCommand="ssh -W %h:%p -q bastion@jump.example.com"'
```

## Common Mistakes

- **Not checking if the host is running**: Always verify the host is powered on and the OS has booted.
- **Assuming DNS works**: Always test both hostname and IP address connectivity.
- **Ignoring intermittent network issues**: Use `ping` and `traceroute` to diagnose latency or packet loss.
- **Not configuring timeout for cloud instances**: Cloud instances may take time to boot and start sshd.

## Related Pages

- [Ansible Connection Refused](/tools/ansible/ansible-connection-refused/) — SSH port issues
- [Ansible Permission Denied](/tools/ansible/ansible-permission-denied/) — Authentication failures
- [Kubectl Connection Refused](/tools/kubectl/kubectl-connection-refused/) — Kubernetes API connectivity
