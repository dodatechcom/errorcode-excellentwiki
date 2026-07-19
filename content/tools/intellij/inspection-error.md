---
title: "[Solution] IntelliJ IDEA Inspection error"
description: "Fix IntelliJ IDEA inspection errors. Resolve code inspection failures, false positives, and inspection profile misconfigurations."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "inspections", "code-analysis", "linting", "code-quality"]
severity: "error"
---

# Inspection error

## Error Message

```
Inspection error
Inspection 'JavaAnnotator' has failed
Internal error: java.lang.ArrayIndexOutOfBoundsException
Cannot inspect file: encoding not supported
Inspection result is incorrect: false positive detected
```

## Common Causes

- Inspection plugin has an internal bug causing exceptions
- File encoding is not supported by the inspection engine
- Custom inspection rules conflict with built-in inspections
- PSI element structure is unexpected for the inspection
- IDE version mismatch with inspection implementation

## Solutions

### Solution 1: Disable Specific Failing Inspection

Identify and disable the specific inspection that is causing errors.

```
File → Settings → Editor → Inspections
# Search for the failing inspection by name
# (e.g., 'JavaAnnotator' or the specific rule)

# Uncheck the inspection to disable it:
#   Java → General → [Failing inspection name]

# Click 'Apply' and 'OK'
# Re-run inspection to verify fix:
Analyze → Inspect Code → Current File
```

### Solution 2: Reset Inspection Profile to Defaults

Reset the inspection profile to factory defaults to eliminate misconfiguration.

```
File → Settings → Editor → Inspections
# Click on profile dropdown → 'Default' or 'Project Default'
# Click 'Manage' (gear icon)
# → 'Restore Defaults'

# If profile is locked:
# Create a new profile:
#   Click '+' → Name: 'Reset Profile'
#   Click 'Manage' → 'Restore Defaults'
# Set as default profile

# Re-run inspection:
Analyze → Inspect Code → Whole project
```

### Solution 3: Update IDE and Plugins

Update IntelliJ IDEA and all plugins to the latest versions to fix known inspection bugs.

```
# Check for IDE updates:
Help → Check for Updates
# Install available updates and restart IDE

# Check for plugin updates:
File → Settings → Updates
# → 'Check for Updates Now'

# Or from command line:
# Download latest version from:
# https://www.jetbrains.com/idea/download/
```

### Solution 4: Report the Bug to JetBrains

If the inspection error persists, report it with diagnostic information.

```
# Collect diagnostic info:
Help → Collect Memory and Diagnostic Info
# This generates a zip file with logs

# Submit bug report:
# https://youtrack.jetbrains.com/issues/IDEA

# Include in report:
#   - IDE version (Help → About)
#   - OS and JDK version
#   - Steps to reproduce
#   - Attached diagnostic zip
#   - Screenshot of the error
```

## Prevention Tips

- Create separate inspection profiles for different project types and team standards
- Export and share inspection profiles via Version Control for team consistency
- Use 'Analyze → Inspect Code' with specific profiles for different review contexts
- Review inspection severity levels and customize to match your team's coding standards

## Related Errors

- [Code Analysis Error]({{< relref "/tools/intellij/code-analysis-error" >}})
- [Code Completion Error]({{< relref "/tools/intellij/code-completion-error" >}})
- [Optimize Imports Error]({{< relref "/tools/intellij/optimize-imports-error" >}})
