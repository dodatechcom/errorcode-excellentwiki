---
title: "[Solution] IntelliJ IDEA Code completion not working"
description: "Fix IntelliJ IDEA code completion failures. Resolve autocomplete not working, slow suggestions, and missing type inference."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "code-completion", "autocomplete", "intellisense", "productivity"]
severity: "error"
---

# Code completion not working

## Error Message

```
Code completion not working
Code completion popup does not appear
No suggestions available for this context
Completion failed: Internal error. Refer to IDE log
Basic code completion is not responding
```

## Common Causes

- Code completion is disabled in IDE settings
- IDE indexing is incomplete or paused due to error
- Memory pressure causing completion engine to timeout
- File type is not recognized or not associated with a language
- Third-party plugin is interfering with completion engine

## Solutions

### Solution 1: Verify Completion Settings

Ensure code completion is enabled and configured correctly in IDE settings.

```
File → Settings → Editor → General → Code Completion
# Verify these settings:
#   ☑ Basic completion (Ctrl+Space)
#   ☑ Smart completion (Ctrl+Shift+Space)
#   ☑ Case sensitive completion: None (recommended)
#   ☑ Auto-insert single suggestion: Checked
#   ☑ Show suggestions as you type: Checked

# For ML-assisted completion:
#   ☑ Machine Learning-based completion: Checked (if available)
```

### Solution 2: Trigger Manual Completion

Use keyboard shortcuts to force code completion and diagnose the issue.

```
# Basic completion:
Ctrl+Space (Windows/Linux)
⌃Space (macOS)

# Smart completion (filters by expected type):
Ctrl+Shift+Space (Windows/Linux)
⌃⇧Space (macOS)

# Class name completion:
Ctrl+Alt+Space (Windows/Linux)
⌃⌥Space (macOS)

# Postfix completion:
# Type variable name then '.' → choose postfix template
# e.g., 'list.for' → expands to for-each loop
```

### Solution 3: Restart IDE and Rebuild Indexes

Restart the IDE and wait for indexing to complete, which is required for code completion to function.

```
# Save all files (Ctrl+Shift+S)
# Invalidate caches:
File → Invalidate Caches → Invalidate and Restart

# Wait for indexing to complete:
# Status bar shows 'Indexing...' progress
# Do not use code completion until indexing finishes

# Monitor indexing progress:
# Help → Activity Monitor → Check CPU usage of IDE process
```

### Solution 4: Check Power Save Mode

Ensure Power Save Mode is not enabled, which disables code completion and other IDE features.

```
# Check if Power Save Mode is on:
File → Power Save Mode
# If checked, uncheck it to re-enable all IDE features

# Also check:
# File → Settings → Appearance
#   ☑ Enable animation: Checked (disabling reduces features)

# Status bar indicator:
# Look for 'Power Save' text in the status bar
```

## Prevention Tips

- Use Basic completion (Ctrl+Space) as a fallback when auto-popup is not appearing
- Customize completion suggestions by excluding unwanted packages in Settings
- Use postfix completion templates to write common patterns quickly
- Install the 'AI Assistant' plugin for enhanced ML-powered code completion

## Related Errors

- [Code Analysis Error]({{< relref "/tools/intellij/code-analysis-error" >}})
- [Navigation Error]({{< relref "/tools/intellij/navigation-error" >}})
- [Indexing Error]({{< relref "/tools/intellij/indexing-error" >}})
