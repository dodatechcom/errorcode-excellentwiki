---
title: "[Solution] IntelliJ IDEA Code analysis failed"
description: "Fix IntelliJ IDEA code analysis failures. Resolve inspection errors, code highlighting issues, and static analysis problems."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "code-analysis", "inspections", "static-analysis", "code-quality"]
severity: "error"
---

# Code analysis failed

## Error Message

```
Code analysis failed
Analysis task 'Inspections' has failed.
java.lang.AssertionError: Unexpected element: PsiElement
Internal error. Refer to IDE log for details.
Analysis completed with errors: some files were skipped.
```

## Common Causes

- Corrupted PSI tree or file cache in the IDE
- Plugin conflict affecting code analysis engine
- Inspection profile misconfigured with conflicting rules
- Memory pressure causing analysis timeout
- Language support plugin outdated or incompatible

## Solutions

### Solution 1: Restart Code Analysis

Manually trigger a re-analysis of the current file or the entire project.

```
# For current file:
Analyze → Inspect Code → Select scope

# For whole project:
Analyze → Inspect Code → Whole project
# Select inspection profile: 'Default' or custom
# Click 'OK' to start analysis

# To re-analyze a single file:
# Close and reopen the file, or use:
Analyze → Code Cleanup
```

### Solution 2: Reset Inspection Profile

Reset the inspection profile to default or create a clean configuration.

```
File → Settings → Editor → Inspections
# Click 'Manage' (gear icon) next to profile dropdown
# Select 'Restore Defaults' to reset current profile
# Or create new profile:
#   Click '+' → Name: 'Clean Profile'
#   Enable only essential inspections
# Apply and re-run analysis
```

### Solution 3: Increase Analysis Memory Allocation

Increase heap size specifically for code analysis operations in the IDE vmoptions.

```bash
# Edit custom VM options:
# Help → Edit Custom VM Options

# Add or modify these settings:
-Xms2048m
-Xmx8192m
-XX:ReservedCodeCacheSize=2048m
-XX:+UseG1GC
-XX:MaxGCPauseMillis=500

# Restart IDE after changes
```

### Solution 4: Disable Problematic Inspections

Temporarily disable problematic inspections to isolate which one is causing the failure.

```
File → Settings → Editor → Inspections
# Use the search bar to find specific inspections
# Uncheck suspected problematic ones:
#   - Third-party inspection plugins
#   - Custom inspections from team-shared profiles
#   - Heavyweight inspections (e.g., 'Whole project' scope)

# To export current profile for debugging:
# Click 'Manage' → 'Export' → Save as XML
```

## Prevention Tips

- Run code inspection periodically with Analyze → Inspect Code to catch issues early
- Create custom inspection profiles for different contexts (quick check vs. thorough)
- Disable unnecessary heavyweight inspections to improve analysis speed
- Check the IDE log (Help → Show Log in Explorer) when analysis fails silently

## Related Errors

- [Inspection Error]({{< relref "/tools/intellij/inspection-error" >}})
- [Refactoring Failed]({{< relref "/tools/intellij/refactoring-error" >}})
- [Code Completion Error]({{< relref "/tools/intellij/code-completion-error" >}})
