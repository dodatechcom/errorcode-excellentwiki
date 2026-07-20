---
title: "[Solution] Windows Update Error 0x80240022 — Policy Conflict Fix"
description: "Fix Windows Update error 0x80240022 (policy conflict) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] Error 0x80240022 — Policy Conflict Fix

Windows Update error 0x80240022 indicates a group policy conflict is preventing Windows Update from functioning. This typically happens when conflicting policies from different sources override each other.

## Description

The full error message reads:

> "There were problems checking for updates. Error 0x80240022"

Error 0x80240022 maps to `WU_E_POLICY_UNSET`, meaning a policy required by Windows Update has been unset or overridden. This commonly occurs on domain-joined machines with conflicting Group Policy settings.

## Common Causes

1. **Conflicting Group Policy settings** — Multiple policies overriding Windows Update configuration.
2. **Registry policy overrides** — Manual registry edits conflicting with GPO.
3. **Third-party management tools** — Software applying conflicting update policies.
4. **Domain policy changes** — Recent GPO modifications interfering with updates.

## Solutions

### Solution 1: Check Group Policy Settings

Open Group Policy Editor:

```cmd
gpedit.msc
```

Navigate to:

```
Computer Configuration > Administrative Templates > Windows Components > Windows Update
```

Check for conflicting policies and set them to **Not Configured**.

### Solution 2: Reset Windows Update Group Policy

```cmd
RD /S /Q "%WinDir%\System32\GroupPolicy"
gpupdate /force
```

### Solution 3: Reset Windows Update Components

```cmd
net stop wuauserv
net stop cryptSvc
net stop bits
net stop msiserver
ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
ren C:\Windows\System32\catroot2 catroot2.old
net start wuauserv
net start cryptSvc
net start bits
net start msiserver
```

### Solution 4: Run System File Checker

```cmd
sfc /scannow
```

## Related Errors

- [Error 0x8024001e]({{< relref "/os/windows/windows-update-0x8024001e" >}}) — Service stopped
- [Error 0x8024402c]({{< relref "/os/windows/windows-update-0x8024402c" >}}) — Connection error
- [Error 0x8007000d]({{< relref "/os/windows/windows-update-0x8007000d" >}}) — Invalid data
