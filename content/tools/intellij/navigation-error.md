---
title: "[Solution] IntelliJ IDEA Go to definition failed"
description: "Fix IntelliJ IDEA navigation failures. Resolve Go to Definition, Go to Symbol, and Go to Implementation errors."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "navigation", "go-to-definition", "symbol-resolution", "psi"]
severity: "error"
---

# Go to definition failed

## Error Message

```
Navigation error
Cannot find declaration to go to
No symbol found at cursor position
Navigation failed: Source file not found
Cannot navigate to declaration in external library
```

## Common Causes

- Symbol is defined in a dependency that is not resolved
- Source attachment is missing for library classes
- IDE indexing is incomplete or the symbol is not indexed
- PSI element does not have a valid navigation target
- Generated or synthetic code lacks navigation data

## Solutions

### Solution 1: Attach Source Files to Library

Attach source JAR files to external libraries so navigation works into dependency code.

```
File → Project Structure → Libraries
# Select the library → Click '+' (Add)
# Choose 'Attach Files or Directories'
# Navigate to the source JAR or source directory

# For Maven dependencies:
# In Maven Tool Window → Expand dependency
# Right-click → Download Sources

# For Gradle:
# File → Settings → Build Tools → Gradle
# ☑ 'Download external annotations for dependencies'
# Then re-sync Gradle project
```

### Solution 2: Navigate to Implementation Instead

Use Go to Implementation as an alternative when Go to Definition fails.

```
# Go to Definition:
Ctrl+B (Windows/Linux)
⌘B or ⌥↓ (macOS)

# Go to Implementation (finds concrete class):
Ctrl+Alt+B (Windows/Linux)
⌘⌥B (macOS)

# Go to Symbol by name:
Ctrl+Alt+Shift+N (Windows/Linux)
⌘⌥⇧O (macOS)

# Find Usages instead:
Alt+F7 (Windows/Linux)
⌥F7 (macOS)
```

### Solution 3: Rebuild Indexes

Rebuild the IDE indexes which are required for symbol resolution and navigation.

```
File → Invalidate Caches
# Check: ☑ Clear file system cache and Local History
# Click 'Invalidate and Restart'

# Wait for indexing to complete (shown in status bar)
# This may take several minutes for large projects

# Monitor progress:
# Help → Activity Monitor
# Look for IDE process CPU activity
```

### Solution 4: Use Find Action for Navigation Shortcuts

Use Find Action to discover and execute navigation commands when shortcuts don't work.

```
# Open Find Action:
Ctrl+Shift+A (Windows/Linux)
⌘⇧A (macOS)

# Search for:
#   'Go to Declaration'
#   'Go to Implementation'
#   'Go to Symbol'
#   'Go to Type Declaration'

# Or navigate via structure:
# Ctrl+F12 (Windows/Linux) / ⌘F12 (macOS)
# Shows file structure popup with searchable members
```

## Prevention Tips

- Download sources for all major dependencies to enable full code navigation
- Use Ctrl+Click on any symbol to navigate to its declaration quickly
- Use Type Hierarchy (Ctrl+H) to understand class inheritance before navigation
- Bookmark important declarations with F11 for quick navigation later

## Related Errors

- [Code Completion Error]({{< relref "/tools/intellij/code-completion-error" >}})
- [Indexing Error]({{< relref "/tools/intellij/indexing-error" >}})
- [Rename Error]({{< relref "/tools/intellij/rename-error" >}})
