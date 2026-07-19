---
title: "[Solution] IntelliJ IDEA Refactoring failed"
description: "Fix IntelliJ IDEA refactoring failures. Resolve errors during rename, extract, move, and other code transformation operations."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "refactoring", "code-transformation", "psi", "code-quality"]
severity: "error"
---

# Refactoring failed

## Error Message

```
Refactoring failed
Cannot perform refactoring: element cannot be renamed.
java.lang.IllegalStateException: Unexpected state during refactoring
Conflicts detected: 2 files have conflicting usages.
Refactoring preview shows unexpected changes.
```

## Common Causes

- PSI tree is corrupted due to syntax errors in the codebase
- Refactoring scope includes files with unsaved changes
- Symbol references are ambiguous across multiple modules
- Generated code is being targeted by the refactoring
- Plugin modifies the code transformation pipeline

## Solutions

### Solution 1: Check for Syntax Errors First

Fix all compilation errors before attempting refactoring. The IDE's refactoring engine relies on a valid PSI tree.

```
# Run code inspection to find syntax errors:
Analyze → Inspect Code → Current File
# Fix all red squiggly lines before refactoring

# Or compile from command line:
mvn compile 2>&1 | head -20
# or
./gradlew compileJava 2>&1 | head -20
```

### Solution 2: Commit or Stash Changes

Save all changes before refactoring. Use Local History as a safety net.

```bash
# Stash changes:
git stash push -m "Before refactoring"

# Or commit:
git add . && git commit -m "Save state before refactoring"

# In IDE, also check Local History:
# Right-click file → Local History → Show History
# This provides an additional rollback safety net
```

### Solution 3: Use Refactoring Preview

Always review the refactoring preview before applying changes. Deselect files that should not be modified.

```
# When performing refactoring:
# 1. Right-click → Refactor → [Select operation]
# 2. In the refactoring dialog, click 'Preview'
# 3. Review ALL affected files in the Changes view
# 4. Uncheck files that should NOT be modified
# 5. Click 'Do Refactoring' when satisfied

# Keyboard shortcut for Refactor This:
Ctrl+Alt+Shift+T (Windows/Linux)
⌃⌥⇧T (macOS)
```

### Solution 4: Invalidate Caches Before Refactoring

Clear the IDE cache if refactoring fails repeatedly due to internal state issues.

```
File → Invalidate Caches
# Check all boxes:
#   ☑ Clear file system cache and Local History
#   ☑ Clear VCS Log caches and Local History
#   ☑ Drop Local History
# Click 'Invalidate and Restart'
# Wait for full indexing to complete
# Then retry the refactoring
```

## Prevention Tips

- Always fix compilation errors before attempting any refactoring operation
- Use Ctrl+Z to undo refactoring immediately if the result is unexpected
- Review the full refactoring preview carefully, especially for rename operations
- Use Local History as a safety net before large-scale refactoring operations

## Related Errors

- [Rename Error]({{< relref "/tools/intellij/rename-error" >}})
- [Extract Error]({{< relref "/tools/intellij/extract-error" >}})
- [Move Error]({{< relref "/tools/intellij/move-error" >}})
