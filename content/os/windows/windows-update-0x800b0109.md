---
title: "[Solution] Windows Update Error 0x800b0109 Certificate Chain Error Fix"
description: "Fix Windows Update error 0x800b0109 (certificate chain not trusted) on Windows 10 and 11. Resolve update trust errors with certificate store repairs and root certificate updates."
platforms: ["windows"]
severities: ["error"]
error_types: ["system-error"]
weight: 5
---

# [Solution] Windows Update Error 0x800b0109 Certificate Chain Error Fix

Error 0x800b0109 means Windows Update could not establish a trust chain for the update package's digital certificate. The certificate chain — which connects the update's signature to a trusted root authority — could not be validated.

This error is similar to 0x80096004 but specifically indicates a chain-of-trust problem rather than a single certificate issue.

## What This Error Means

The full error message typically reads:

> "Some updates were not installed. Errors found: Code 0x800b0109. Windows Update ran into a problem."

Error 0x800b0109 maps to `CRYPT_E_NO_TRUST` — the certificate chain could not be built to a trusted root authority. Common triggers include:

- **Missing root certificates** — Trusted root certificates not installed
- **Corporate proxy interference** — Proxy breaking certificate chains
- **Outdated certificate store** — Windows certificate database not updated
- **Expired intermediate certificates** — Intermediate CA certificates have expired

## Common Causes

1. **Missing root certificates** — Root CA certificates not in the Windows trust store.
2. **Corporate proxy or firewall** — Network devices intercepting update connections.
3. **Outdated certificate store** — Certificate database not updated.
4. **Expired intermediate certificates** — Intermediate CA certificates expired.

## How to Fix

### Update Root Certificate Store

```cmd
certutil -generateSSTFromWU roots.sst
certutil -addstore Root roots.sst
del roots.sst
```

### Verify System Time

```powershell
Get-Date
```

If incorrect, resync:

```cmd
w32tm /resync /force
```

### Reset Windows Update Components

```cmd
net stop wuauserv
net stop cryptSvc
net stop bits
net stop msiserver
rd /s /q "C:\Windows\SoftwareDistribution"
rd /s /q "C:\Windows\System32\catroot2"
net start wuauserv
net start cryptSvc
net start bits
net start msiserver
```

### Check for Corporate Proxy Issues

```cmd
netsh winhttp show proxy
```

If behind a proxy, ensure it does not intercept HTTPS update connections. Reset proxy if needed:

```cmd
netsh winhttp reset proxy
```

### Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Download Update Manually

1. Note the KB number.
2. Visit [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. Download and install the update manually.

## Related Errors

- [Error 0x80096004]({{< relref "/os/windows/windows-update-0x80096004" >}}) — Certificate signature error
- [Error 0x800f0922]({{< relref "/os/windows/windows-update-0x800f0922" >}}) — Connection timeout
- [Error 0x8024402c]({{< relref "/os/windows/windows-update-0x8024402c" >}}) — Proxy connection error
