---
title: "[Solution] Ansible Connection Refused Error — Fix SSH Access"
description: "Fix Ansible SSH connection refused errors. Resolve firewall rules, SSH daemon issues, and network connectivity problems quickly."
---

## What This Error Means

The `Connection refused` error means Ansible cannot establish an SSH connection to the target host. The SSH port (usually 22) is either not open, blocked by a firewall, or the SSH daemon is not running on the remote machine.

A typical error:

```
host1 | FAILED! => {"msg": "Failed to connect to the host via ssh:
ssh: connect to host 192.168.1.10 port 22: Connection refused"}
```

## Why It Happens

Connection refused errors occur when:

- **SSH daemon is not running**: The `sshd` service was stopped or never started on the target.
- **Firewall blocking port 22**: Network firewalls, security groups, or iptables rules block SSH traffic.
- **Wrong SSH port**: The target SSH daemon listens on a non-standard port not configured in Ansible.
- **Host is down**: The target machine is powered off or unreachable at the network level.
- **SELinux blocking**: SELinux policies preventing SSH connections.

## How to Fix It

**Step 1: Verify the host is reachable**

```bash
ping 192.168.1.10
nmap -p 22 192.168.1.10
```

**Step 2: Check SSH daemon status on the target**

```bash
ssh root@192.168.1.10 "systemctl status sshd"
# Or access via console and check
systemctl status sshd
systemctl start sshd
```

**Step 3: Verify firewall rules**

```bash
# On the target host
iptables -L -n | grep 22
firewall-cmd --list-all
ufw status
```

**Step 4: Configure non-standard SSH port in inventory**

If SSH runs on a custom port:

```ini
# inventory.ini
[webservers]
web1 ansible_port=2222 ansible_host=192.168.1.10
```

Or in YAML inventory:

```yaml
all:
  children:
    webservers:
      hosts:
        web1:
          ansible_host: 192.168.1.10
          ansible_port: 2222
```

**Step 5: Test SSH manually before running Ansible**

```bash
ssh -v user@192.168.1.10
```

## Common Mistakes

- **Running Ansible from a network that cannot reach the target**: Verify network routing and VPN connectivity first.
- **Using wrong SSH port in playbook**: Always verify the target port in your inventory configuration.
- **Not checking security groups in cloud environments**: AWS, GCP, and Azure security groups must allow SSH inbound.
- **Forgetting to start sshd after OS deployment**: Many minimal OS images disable sshd by default.

## Related Pages

- [Ansible Unreachable Host](/tools/ansible/ansible-unreachable-host/) — Host reachability issues
- [Ansible Permission Denied](/tools/ansible/ansible-permission-denied/) — SSH authentication errors
- [Kubectl Connection Refused](/tools/kubectl/kubectl-connection-refused/) — API server connection issues
