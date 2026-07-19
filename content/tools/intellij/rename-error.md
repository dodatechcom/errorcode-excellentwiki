---
title: "[Solution] IntelliJ IDEA Rename refactoring failed"
description: "Fix IntelliJ IDEA rename refactoring failures. Resolve symbol rename conflicts, reference resolution errors, and scope issues."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "rename", "refactoring", "symbol-resolution", "psi"]
severity: "error"
---

# Rename refactoring failed

## Error Message

```
Rename refactoring failed
Cannot rename 'UserService': usages in read-only files detected
Conflicts: 3 files have conflicting references
Rename refactoring: some occurrences could not be renamed
Cannot rename: element is defined in a non-editable scope
```

## Common Causes

- Symbol has usages in read-only or generated files
- Rename would create a conflict with existing symbols
- Element is defined in an external library or compiled class
- PSI tree is corrupted and references cannot be resolved
- Multiple modules define the same symbol name

## Solutions

### Solution 1: Use Safe Rename

Perform a safe rename that checks for conflicts before applying changes. Always use the preview feature.

```
# Position cursor on the symbol to rename
# Press Shift+F6 (Windows/Linux) or ⇧F6 (macOS)

# Or via menu:
# Right-click symbol → Refactor → Rename...

# In the rename dialog:
#   ☑ Search in comments and strings
#   ☑ Search for text occurrences
#   Click 'Preview' to review all changes
#   Review each file in the Changes tool window
#   Click 'Do Refactoring' when satisfied
```

### Solution 2: Resolve Read-Only File Conflicts

Handle usages in generated or read-only files by excluding them from the refactoring.

```
# In the Rename dialog:
# Click 'Options' or 'Refactoring options'
# Uncheck 'Search in comments and strings' if not needed

# For files in version control that are read-only:
#   Right-click file → Local History → Show History
#   Ensure file is not locked by another process

# For generated files:
#   Exclude generated directories:
#   File → Settings → Editor → File Types
#   Add patterns for generated files to ignore

# For library source files:
#   Only rename in your source code, not in libraries
```

### Solution 3: Find and Replace as Alternative

Use the Find and Replace tool as a manual alternative when rename refactoring fails.

```
# Open Find and Replace:
Ctrl+Shift+R (Windows/Linux)
⌘⇧R (macOS)

# Search for: OldSymbolName
# Replace with: NewSymbolName
# Scope: Whole project or Custom

# Options:
#   ☑ Match case
#   ☑ Words only
#   ☑ Regex (for complex patterns)
#   Scope: 'Project Files' or 'Directory'

# Click 'Replace All' after reviewing matches
# WARNING: This does NOT update string literals or comments automatically
```

### Solution 4: Rename via Structure View

Use the Structure view to rename symbols when direct refactoring is not available.

```
# Open Structure view:
Ctrl+F12 (Windows/Linux)
⌘F12 (macOS)

# Find the symbol in the structure tree
# Right-click → Rename (F2)

# Or use File Structure popup:
# Ctrl+F12 → Type symbol name → F2 to rename

# For renaming across files:
# Ctrl+Alt+Shift+N → Type old name → F2
# This opens the symbol for rename in-place
```

## Prevention Tips

- Always use Shift+F6 (Safe Rename) instead of Find and Replace for symbol renames
- Review the rename preview carefully before applying, especially for common names
- Check Local History after rename to ensure all expected changes were made
- For large-scale renames, consider using the 'Rename File' refactoring for class renames

## Related Errors

- [Refactoring Failed]({{< relref "/tools/intellij/refactoring-error" >}})
- [Extract Error]({{< relref "/tools/intellij/extract-error" >}})
- [Move Error]({{< relref "/tools/intellij/move-error" >}})
