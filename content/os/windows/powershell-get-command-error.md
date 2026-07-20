---
title: "[Solution] PowerShell GET_COMMAND — Command Not Found Error"
description: "Fix PowerShell Get-Command error with these step-by-step solutions. Includes PowerShell commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 1006
---

# [Solution] PowerShell GET_COMMAND — Command Not Found Error

The PowerShell Get-Command error indicates that a command, function, alias, or cmdlet cannot be located by PowerShell. This prevents script execution and interactive use of expected commands.

## Description

When you run `Get-Command` or attempt to execute a command that PowerShell cannot find, you receive an error indicating the command does not exist or is not recognized. The full error message typically reads:

> "The term 'command-name' is not recognized as the name of a cmdlet, function, script file, or operable program."

Or when using Get-Command:

> "Get-Command: The requested command 'command-name' was not found. Check the spelling of the command name, or if a module was loaded, verify that the module name is spelled correctly."

## Common Causes

1. The command comes from a module that is not installed or loaded.
2. The command name is misspelled.
3. The module containing the command is not in the PSModulePath.
4. The command exists only in a different PowerShell version (e.g., PowerShell 5.1 vs 7+).
5. The command is an alias that has not been defined.
6. The module requires a specific PowerShell edition (Desktop vs Core).

## Solutions

### Solution 1: Search for the Command

Find where the command should come from:

```powershell
Get-Command -Name "CommandName" -All -ErrorAction SilentlyContinue
Get-Command -Name "*PartialName*" -ErrorAction SilentlyContinue
```

### Solution 2: Identify the Module

Check if the command is part of an uninstalled module:

```powershell
Get-Command | Where-Object { $_.Name -like "*keyword*" }
Find-Module -Name "*ModuleName*" -ErrorAction SilentlyContinue
```

### Solution 3: Install and Import the Module

Install the missing module and import it:

```powershell
Install-Module -Name "ModuleName" -Force -Scope CurrentUser
Import-Module -Name "ModuleName"
```

### Solution 4: Check PowerShell Edition

Verify you are using the correct PowerShell version:

```powershell
$PSVersionTable
$PSVersionTable.PSEdition
$PSVersionTable.PSVersion
```

Some commands are available only in PowerShell 5.1 (Desktop) or 7+ (Core).

### Solution 5: Use Fully Qualified Command Names

Disambiguate commands with module prefixes:

```powershell
# Use module-qualified name
Microsoft.PowerShell.Management\Get-Process
Microsoft.PowerShell.Utility\Get-Date

# Or use -Module parameter
Get-Command -Module "Microsoft.PowerShell.Utility"
```

### Solution 6: Check Command Availability

List all available commands to find the correct name:

```powershell
Get-Command -CommandType Cmdlet | Sort-Object Name | Format-Table Name, Source
Get-Command -CommandType Function | Sort-Object Name | Format-Table Name, Source
Get-Command -CommandType Alias | Sort-Object Name | Format-Table Name, Source
```

### Solution 7: Verify the Module Path

Ensure module directories are properly configured:

```powershell
$env:PSModulePath -split ";"
Get-Module -ListAvailable | Group-Object Name | Sort-Object Name
```

## Related Errors

- [PowerShell Module Not Found]({{< relref "/os/windows/powershell-module-not-found" >}}) — Module cannot be loaded
- [PowerShell Execution Policy Error]({{< relref "/os/windows/powershell-execution-policy-error" >}}) — Scripts cannot be loaded
- [PowerShell Invoke-Command Error]({{< relref "/os/windows/powershell-invoke-command-error" >}}) — Remote execution failed
