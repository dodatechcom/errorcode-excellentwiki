---
title: "[Solution] IntelliJ IDEA Move refactoring failed"
description: "Fix IntelliJ IDEA move refactoring failures. Resolve class/file/package move errors and import resolution issues."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "move", "refactoring", "package", "module"]
severity: "error"
---

# Move refactoring failed

## Error Message

```
Move refactoring failed
Cannot move 'UserRepository' to package 'com.example.repository':
Target package already contains a class with the same name
Move file: source and target must be in the same project
Cannot move class: it has usages in non-editable modules
```

## Common Causes

- Target package already contains a class with the same name
- File is referenced by non-editable or generated code
- Move target is outside the project source root
- Module dependencies prevent the move operation
- Package structure does not exist and cannot be created

## Solutions

### Solution 1: Move Class or File

Use the Move refactoring to relocate classes to different packages or directories.

```
# Move a class to a different package:
# 1. Right-click the class file → Refactor → Move
# 2. Or use F6 (Windows/Linux) / F6 (macOS)

# In the Move dialog:
#   To package: com.example.newpackage
#   ☑ Search for references: Checked
#   ☑ Move file: Checked (to move the file too)

# For moving to a new package:
# The IDE will create the target package automatically
# Review the preview before applying
```

### Solution 2: Resolve Name Conflicts

Handle name conflicts when the target location already has a class with the same name.

```
# If a name conflict exists:
# Option 1: Rename the source class before moving
#   Right-click class → Refactor → Rename
#   Then retry the move

# Option 2: Rename the target class first
#   Right-click target class → Refactor → Rename
#   Then move the source class

# Option 3: Check if both classes serve the same purpose
#   Merge their functionality and delete the duplicate

# Option 4: Move to a sub-package to avoid conflict
#   com.example.shared.model.User
#   com.example.v2.model.User
```

### Solution 3: Move Between Modules

Move classes between modules while maintaining proper dependency relationships.

```
# Move to a different module:
# 1. Right-click class → Refactor → Move
# 2. Select target module from dropdown
# 3. Specify target package

# Ensure module dependencies are correct:
File → Project Structure → Modules
# Check that target module has:
#   - Correct source roots configured
#   - Required library dependencies
#   - Proper module SDK

# After moving, verify imports:
# Build → Rebuild Project
# Fix any broken import statements
```

### Solution 4: Move Multiple Files at Once

Move multiple files simultaneously using the Move dialog with multi-selection.

```
# Select multiple files to move:
# Ctrl+Click (Windows/Linux) / ⌘Click (macOS) on each file
# Then right-click → Refactor → Move (F6)

# Or in the Project view:
# Select multiple files → F6
# Enter target package

# Review the preview:
# The Changes tool window shows all affected files
# Verify imports will be updated correctly
# Check for any circular dependency warnings

# Apply the refactoring
# Then run Build → Compile to verify no broken references
```

## Prevention Tips

- Always review the refactoring preview to verify all imports will be updated correctly
- Move related classes together to maintain package cohesion
- Run Build → Rebuild Project after large-scale moves to catch any missed references
- Use the Package view in the Project tool window to reorganize package structure

## Related Errors

- [Rename Error]({{< relref "/tools/intellij/rename-error" >}})
- [Refactoring Failed]({{< relref "/tools/intellij/refactoring-error" >}})
- [Change Signature Error]({{< relref "/tools/intellij/change-signature-error" >}})
