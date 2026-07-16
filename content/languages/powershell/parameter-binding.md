---
title: "[Solution] PowerShell ParameterBindingException Fix"
description: "Fix 'Parameter cannot be found' when PowerShell cannot bind an argument to a cmdlet parameter."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["ParameterBindingException", "parameter", "binding"]
weight: 5
---

# PowerShell ParameterBindingException Fix

This error occurs when PowerShell cannot bind a supplied argument to any parameter of a cmdlet. The error message reads: `A parameter cannot be found that matches parameter name 'X'.`

## Description

PowerShell matches arguments to parameters by name or position. If a parameter name is misspelled, not available on the cmdlet, or the positional binding fails, the parameter binding mechanism throws this error.

## Common Causes

- **Misspelled parameter name** — typo in the `-ParameterName` argument.
- **Parameter not available on the cmdlet** — the cmdlet doesn't have that parameter, or it requires a specific module version.
- **Wrong parameter set** — the combination of parameters used doesn't match any defined parameter set.
- **Positional argument mismatch** — passing too many positional arguments or in the wrong order.

## How to Fix

### Fix 1: Verify the parameter exists

```powershell
# Check available parameters for a cmdlet
Get-Help Get-Process -Parameter *

# Confirm the exact spelling
(Get-Command Get-Process).Parameters.Keys
```

### Fix 2: Use tab completion to avoid typos

```powershell
# Type the cmdlet name and a dash, then press Tab to cycle through valid parameters
Get-Process -Na<Tab>
# Completes to -Name
```

### Fix 3: Check the correct parameter set

```powershell
# View all parameter sets for a cmdlet
Get-Help Get-ChildItem -Syntax

# Use the -Name parameter set explicitly
Get-ChildItem -Path "C:\Temp" -Filter "*.txt"
```

### Fix 4: Use splatting for complex parameter handling

```powershell
# Splatting avoids typos and makes parameters easier to manage
$params = @{
    Name = "notepad"
    ErrorAction = "Stop"
}
Get-Process @params
```

## Examples

```powershell
PS> Get-Process -Names "notepad"
ParameterBindingException: A parameter cannot be found that matches parameter name 'Names'.

PS> Get-Process -Name "notepad"
# Works — correct parameter name

PS> Get-ChildItem -Filter "*.txt" -Recurse -WhatIf
# Works — all parameters valid
```

## Related Errors

- [CommandNotFoundException](command-not-found.md) — command name not recognized.
- [ParserError](command-syntax.md) — syntax errors when parsing commands.
