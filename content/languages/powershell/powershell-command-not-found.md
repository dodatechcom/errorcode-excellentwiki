---
title: "[Solution] PowerShell CommandNotFoundException"
description: "Fix PowerShell 'CommandNotFoundException' when a cmdlet, function, or command is not recognized. Common with modules and aliases."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PowerShell CommandNotFoundException Fix

CommandNotFoundException occurs when PowerShell cannot find a command by name. The error reads: `The term 'X' is not recognized as the name of a cmdlet, function, script file, or operable program.`

## What This Error Means

PowerShell searches for commands in modules, aliases, functions, and executable files on the path. If no match is found, it throws this error.

## Common Causes

- Module not imported (cmdlet in unloaded module)
- Typo in command name
- Command requires specific module version
- Script file not on PATH
- Alias not defined in current session

## How to Fix

### 1. Find which module provides the command

```powershell
# Search for the command
Get-Command -Name CommandName -All

# Find module for a specific cmdlet
(Get-Command Some-Command).Source

# Search all modules
Get-Command -Module ModuleName
```

### 2. Import the required module

```powershell
# Import a specific module
Import-Module ModuleName

# Import with specific version
Import-Module ModuleName -RequiredVersion 2.0
```

### 3. Check available commands

```powershell
# List all available commands
Get-Command

# Search by partial name
Get-Command -Name *keyword*
```

### 4. Add script location to PATH

```powershell
# Add to current session
$env:Path += ";C:\Scripts"

# Make permanent
[Environment]::SetEnvironmentVariable("Path",
    $env:Path + ";C:\Scripts", "User")
```

## Related Errors

- [ModuleNotFound](powershell-module-not-found) — module import failures
- [ParameterBindingException](powershell-parameter-binding) — parameter issues
- [Script Syntax Error](script-syntax) — script parsing errors
