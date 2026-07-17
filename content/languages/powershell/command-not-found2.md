---
title: "[Solution] PowerShell Command Not Recognized Fix"
description: "Fix 'command is not recognized' when PowerShell cannot find or execute a command."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PowerShell Command Not Recognized Fix

This error occurs when PowerShell encounters a token it cannot resolve as any known command. The error message reads: `The term 'X' is not recognized as the name of a cmdlet, function, script file, or operable program.`

## Description

PowerShell resolves commands through a lookup order: aliases, functions, cmdlets, and finally external executables via `PATH`. When none of these resolve the token, PowerShell raises a `CommandNotFoundException`. This is distinct from a module simply not being imported — it means the command cannot be found at all.

## Common Causes

- **External executable not installed** — the program was never installed or was removed.
- **PATH not refreshed** — after installing software, the current session doesn't see the new PATH entry.
- **Module not imported in current session** — the module is installed but hasn't been loaded yet.
- **Script block scope issue** — the command is defined in a different scope or session.

## How to Fix

### Fix 1: Check if the program is installed

```powershell
# Search for the executable on disk
Get-Command programname -ErrorAction SilentlyContinue
where.exe programname

# Reinstall the software if not found
```

### Fix 2: Refresh PATH in the current session

```powershell
# Reload PATH from the registry
$machinePath = [Environment]::GetEnvironmentVariable("PATH", "Machine")
$userPath = [Environment]::GetEnvironmentVariable("PATH", "User")
$env:PATH = "$machinePath;$userPath"
```

### Fix 3: Import the module explicitly

```powershell
# List available modules
Get-Module -ListAvailable | Where-Object { $_.Name -like "*keyword*" }

# Import the module
Import-Module ModuleName
```

### Fix 4: Use full path to the executable

```powershell
# Run with full path if PATH isn't set
& "C:\Program Files\App\program.exe" --arguments

# Or create a function alias
Set-Alias -Name prog -Value "C:\Program Files\App\program.exe"
```

## Examples

```powershell
PS> git status
git: The term 'git' is not recognized as the name of a cmdlet, function, script file, or operable program.

PS> kubectl get pods
kubectl: The term 'kubectl' is not recognized as the name of a cmdlet...

PS> Get-Module Az.Accounts
# Module is installed but not loaded

PS> Import-Module Az.Accounts
PS> Connect-AzAccount
# Works after importing
```

## Related Errors

- [CommandNotFoundException](command-not-found.md) — similar command lookup failure.
- [ModuleNotFound](module-not-loaded.md) — module cannot be found or loaded.
- [ParameterBindingException](parameter-binding.md) — parameter binding failure.
