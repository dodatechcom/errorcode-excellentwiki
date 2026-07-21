---
title: "[Solution] PowerShell Script Signature Invalid Error Fix"
description: "Fix PowerShell error about invalid or untrusted script digital signature on Windows. Resolve execution policy and code signing certificate issues."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] PowerShell Script Signature Invalid Error Fix

The PowerShell script signature invalid error means the digital signature on a PowerShell script cannot be verified. This happens when the signing certificate is expired, revoked, or not trusted by the system.

## Common Causes
- Signing certificate has expired
- Certificate not in the Trusted Publishers store
- Execution policy set to AllSigned blocking unsigned scripts
- Script modified after signing invalidating the signature
- Self-signed certificate not trusted by the system

## How to Fix

### Solution 1: Check Script Signature

```powershell
Get-AuthenticodeSignature -FilePath "C:\Scripts\myscript.ps1"
```

### Solution 2: Set Execution Policy

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Solution 3: Install the Signing Certificate

```powershell
Import-Certificate -FilePath "cert.cer" -CertStoreLocation Cert:\LocalMachine\TrustedPublisher
```

### Solution 4: Re-sign the Script

```powershell
$cert = Get-ChildItem Cert:\LocalMachine\My | Where-Object { $_.Subject -like '*YourName*' }
Set-AuthenticodeSignature -FilePath "C:\Scripts\myscript.ps1" -Certificate $cert
```

### Solution 5: Bypass for Testing

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

## Examples
```powershell
Get-AuthenticodeSignature -FilePath "C:\Scripts\myscript.ps1" | Format-List
```
