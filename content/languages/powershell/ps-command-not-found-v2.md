---
title: "[Solution] PowerShell Command Not Found Term Not Recognized Fix"
description: "Fix PowerShell 'term is not recognized as cmdlet' errors. Learn why commands are not found and how to register cmdlets properly."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

The PowerShell `CommandNotFoundException` error occurs when PowerShell cannot find a cmdlet, function, script, or executable in the current session. The error message reads: `The term 'X' is not recognized as the name of a cmdlet, function, script file, or operable program.`

## Why It Happens

- The cmdlet is from a module that has not been imported yet
- The script or executable is not in the system PATH
- A typo in the command name
- The module is installed for a different PowerShell version
- The command was removed or renamed in a newer module version
- Running a cmdlet in PowerShell Core that is only available in Windows PowerShell
- A custom function is defined in a different session

## How to Fix It

### Import the required module first

```powershell
# WRONG: Using cmdlet without importing module
Get-Mailbox -Identity user@example.com  # CommandNotFoundException

# CORRECT: Import the module first
Import-Module ExchangeOnlineManagement
Get-Mailbox -Identity user@example.com
```

### Check available commands with Get-Command

```powershell
# WRONG: Guessing the command name
Get-Processs  # typo

# CORRECT: Verify the command exists
Get-Command Get-Process
# Or search for similar commands
Get-Command *Process*
```

### Update the PATH for custom scripts

```powershell
# WRONG: Running script from non-PATH directory
.\my-script.ps1  # works with relative path, but not as standalone command

# CORRECT: Add script directory to PATH
$env:Path += ";C:\MyScripts"
my-script  # now findable
```

### Use fully qualified module names

```powershell
# WRONG: Module not loaded automatically
Get-AzVM  # Az module not imported

# CORRECT: Import with fully qualified name
Import-Module Az.Compute
Get-AzVM
```

### Check PowerShell edition compatibility

```powershell
# WRONG: Using Windows-only module in PowerShell Core
Get-ActiveSyncDevice  # may not exist in Core

# CORRECT: Check edition and use compatible commands
if ($PSVersionTable.PSEdition -eq "Desktop") {
    Get-ActiveSyncDevice
} else {
    Write-Warning "This command requires Windows PowerShell"
}
```

### Use the module auto-loading feature correctly

```powershell
# CORRECT: PowerShell 3.0+ can auto-load modules
# But the module must be in a PSModulePath location
$env:PSModulePath -split ";"

# If module is in custom location, add it
$customPath = "C:\CustomModules"
$env:PSModulePath = "$customPath;$env:PSModulePath"

# Now cmdlets from modules in customPath auto-load
Get-SomethingFromCustomModule  # auto-imports
```

## Common Mistakes

- Not realizing that PowerShell module auto-loading requires modules in PSModulePath
- Forgetting that some cmdlets have aliases that may not be available
- Running PowerShell scripts without the `.ps1` extension
- Using Windows-specific modules in PowerShell Core without checking compatibility
- Assuming that installing a module via `Install-Module` makes it available in all sessions

## Related Pages

- [PowerShell Module Not Found](ps-module-not-found-v2) - module loading failed
- [PowerShell Execution Policy](ps-execution-policy-v2) - script execution blocked
- [PowerShell Parameter Binding](ps-parameter-binding) - parameter error
- [PowerShell Command Syntax](command-syntax) - syntax error
