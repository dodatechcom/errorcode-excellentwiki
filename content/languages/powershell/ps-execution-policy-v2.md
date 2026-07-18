---
title: "[Solution] PowerShell Running Scripts Is Disabled Fix"
description: "Fix PowerShell 'running scripts is disabled' execution policy errors. Learn why scripts are blocked and how to set correct policies."
languages: ["powershell"]
severities: ["error"]
error-types: ["security-error"]
weight: 5
---

## What This Error Means

The PowerShell execution policy error occurs when you try to run a `.ps1` script file and the current execution policy prohibits it. The error message reads: `File C:\script.ps1 cannot be loaded because running scripts is disabled on this system.` This is a security feature designed to prevent accidental or malicious script execution.

## Why It Happens

- The default execution policy is `Restricted` on Windows client systems
- The script is downloaded from the internet and has a Zone.Identifier mark
- Group Policy enforces a restrictive execution policy
- The script was saved with an encoding that triggers security warnings
- Running scripts in PowerShell Core where policies differ from Windows PowerShell
- The script is not signed and the policy requires signed scripts

## How to Fix It

### Check the current execution policy

```powershell
# CORRECT: Always check current policy first
Get-ExecutionPolicy -List

# Output:
#        Scope ExecutionPolicy
#        ----- ---------------
# MachinePolicy       Undefined
#    UserPolicy       Undefined
#       Process       Undefined
#   CurrentUser       Undefined
#  LocalMachine      Restricted
```

### Set execution policy for current user

```powershell
# WRONG: Trying to set machine policy without admin rights
Set-ExecutionPolicy RemoteSigned  # fails without elevation

# CORRECT: Set for current user (no admin needed)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Bypass policy for a single script

```powershell
# WRONG: Running script directly when policy blocks it
.\deploy.ps1  # fails

# CORRECT: Bypass policy for one execution
powershell -ExecutionPolicy Bypass -File .\deploy.ps1

# Or from within PowerShell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\deploy.ps1
```

### Unblock downloaded scripts

```powershell
# WRONG: Running a downloaded script without unblocking
.\downloaded-script.ps1  # fails due to Zone.Identifier

# CORRECT: Remove the Zone.Identifier mark
Unblock-File -Path .\downloaded-script.ps1
.\downloaded-script.ps1
```

### Sign your scripts for production use

```powershell
# CORRECT: Create a self-signed certificate and sign scripts
$cert = New-SelfSignedCertificate -Type CodeSigningCert `
    -Subject "CN=MyScriptSigning" -CertStoreLocation Cert:\CurrentUser\My

# Sign a script
Set-AuthenticodeSignature -FilePath .\script.ps1 -Certificate $cert

# Then set policy to require signatures
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy AllSigned
```

### Understand policy scope precedence

```powershell
# CORRECT: Policy scopes are evaluated in this order:
# 1. Group Policy (MachinePolicy, UserPolicy) - highest priority
# 2. Registry key (LocalMachine, CurrentUser)
# 3. Process scope - lowest priority, most flexible

# Check which scope is active
Get-ExecutionPolicy -List | Sort-Object Scope
```

## Common Mistakes

- Setting `Unrestricted` policy system-wide instead of `RemoteSigned`
- Not understanding that Group Policy overrides local settings
- Forgetting that `RemoteSigned` allows local scripts but requires downloaded scripts to be signed
- Assuming execution policy is encryption or strong security (it is not)
- Not unblocking scripts downloaded from email or web browsers

## Related Pages

- [PowerShell Unauthorized Access](ps-unauthorized-access-v2) - access denied
- [PowerShell Profile Error](ps-profile-error) - profile load failure
- [PowerShell Script Block Error](ps-script-block-error) - script block failed
- [PowerShell Command Syntax](command-syntax) - syntax error
