---
title: "[Solution] Ansible WinRM Certificate Error"
description: "Resolve WinRM SSL certificate validation errors in Ansible"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible fails to connect via WinRM due to SSL certificate validation issues.

```
UNREACHABLE! => SSLError: certificate verify failed
```

## Common Causes

- Self-signed certificate on Windows host
- Certificate not trusted by Ansible controller
- Certificate hostname mismatch
- WinRM HTTPS listener misconfigured

## How to Fix

```ini
# ansible.cfg (testing only)
[winrm]
server_cert_validation = ignore
```

```yaml
# Production with proper certificates
- hosts: win
  vars:
    ansible_winrm_transport: certificate
    ansible_winrm_cert_pem: /etc/ansible/certs/client.pem
    ansible_winrm_cert_key_pem: /etc/ansible/certs/client-key.pem
    ansible_winrm_server_cert_validation: validate
    ansible_winrm_ca_trust_path: /etc/ansible/certs/ca.pem
```
