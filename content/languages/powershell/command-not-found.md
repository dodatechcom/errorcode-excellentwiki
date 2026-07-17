---
title: "[Solution] PowerShell CommandNotFoundException Fix"
description: "Fix 'The term X is not recognized' when PowerShell cannot find a command or module."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PowerShell CommandNotFoundException Fix

This error occurs when PowerShell cannot find a cmdlet, function, script, or executable. The error message reads: `The term 'X' is not recognized as the name of a cmdlet, function, script file, or operable program.`

## Description

PowerShell searches for commands in a defined order: aliases, functions, cmdlets, and then executables in `PATH`. If none match, it throws `CommandNotFoundException`.

## Common Causes

- **Module not installed or imported** — the cmdlet belongs to a module that isn't loaded.
- **Typo in command name** — misspelling of a cmdlet or function name.
- **Command not in PATH** — the executable exists but isn't in the system PATH.
- **PowerShell edition mismatch** — cmdlet available in PowerShell 7 but not Windows PowerShell, or vice versa.

## How to Fix

### Fix 1: Find and install the missing module

```powershell
# Search for the module
Find-Module -Name "*ModuleName*"

# Install it
Install-Module -Name ModuleName -Scope CurrentUser

# Import it
Import-Module ModuleName
```

### Fix 2: Use command discovery to find the correct name

```powershell
# Search for available commands
Get-Command *keyword*

# Check if a module is loaded
Get-Module -ListAvailable
```

### Fix 3: Add the executable directory to PATH

```powershell
# View current PATH
$env:PATH

# Add to PATH for current session
$env:PATH += ";C:\path\to\directory"

# Permanently add via System Properties or:
[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";C:\path\to\directory", "User")
```

### Fix 4: Check PowerShell edition

```powershell
$PSVersionTable
# If cmdlet is PS7-only, run it in pwsh instead of powershell.exe
```

## Examples

```powershell
PS> Get-Process
# Works fine

PS> Invoke-WebRequest
The term 'Invoke-WebRequest' is not recognized as the name of a cmdlet...

PS> docker ps
The term 'docker' is not recognized as the name of a cmdlet, function, script file, or operable program.
```

## Related Errors

- [ParserError](command-syntax.md) — syntax errors when parsing commands.
