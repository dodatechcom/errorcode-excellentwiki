---
title: "[Solution] Ansible WinRM Certificate Error"
description: "Fix WinRM SSL certificate errors in Ansible Windows management"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

WinRM connection fails due to SSL certificate issues.

```
UNREACHABLE! => SSLError: certificate verify failed
```

## Common Causes

- Self-signed certificate
- Certificate not trusted
- Hostname mismatch

## How to Fix

```ini
# ansible.cfg (testing only)
[winrm]
server_cert_validation = ignore
```

```powershell
New-SelfSignedCertificate -DnsName "winserver" -CertStoreLocation Cert:\LocalMachine\My
```
