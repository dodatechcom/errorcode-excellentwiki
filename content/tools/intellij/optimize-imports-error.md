---
title: "[Solution] IntelliJ IDEA Optimize imports error"
description: "Fix IntelliJ IDEA optimize imports failures. Resolve import sorting, unused import removal, and import organization errors."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "imports", "import-organization", "code-style", "cleanup"]
severity: "error"
---

# Optimize imports error

## Error Message

```
Optimize imports error
Cannot optimize imports: file has syntax errors
Import optimization failed: ambiguous import reference
Unused import detected but cannot be removed: used by annotation processor
Organize imports: conflict between wildcard and specific imports
```

## Common Causes

- File contains syntax errors preventing import analysis
- Import is used by annotation processor but appears unused
- Ambiguous import references across multiple packages
- Import settings conflict between wildcard and specific imports
- Generated code references imports that the IDE cannot resolve

## Solutions

### Solution 1: Optimize Imports for Current File

Clean up imports in the current file using the Optimize Imports action.

```
# Optimize imports for current file:
Ctrl+Alt+O (Windows/Linux)
⌃⌥O (macOS)

# This will:
#   - Remove unused imports
#   - Sort imports by package
#   - Convert between wildcard and specific imports
#   - Add missing imports (if configured)

# For whole project:
# There is no built-in 'Optimize All Imports' action
# Use 'File → Settings → Tools → Actions on Save'
# ☑ Optimize imports (applies on every save)
```

### Solution 2: Configure Import Layout

Set up import organization rules in the code style settings.

```
File → Settings → Editor → Code Style → Java → Imports

# Import layout configuration:
#   ☑ Import layout: Java import layout

# Key settings:
#   Package count to use import with '*': 999
#     (Set high to prefer specific imports)
#   ☑ Import nested classes: Checked
#   Names count to use static import with '*': 999

# Import order:
#   1. static imports
#   2. java.*
#   3. javax.*
#   4. All other imports (alphabetical)
#   5. # package separation

# Apply and optimize imports again
```

### Solution 3: Fix Unused Import Warnings

Manually resolve unused import warnings that the optimizer cannot automatically fix.

```
# If an import is marked unused but is needed:

# For annotation processor imports:
# Add @SuppressWarnings for the specific warning:
@SuppressWarnings("unused")
import com.example.GeneratedAnnotation;

# For reflection-based imports:
# Add a comment to suppress the warning:
// noinspection unused
import com.example.ReflectiveClass;

# Or in Settings → Editor → Inspections:
# Java → Unused declaration
#   ☐ Skip imports: Uncheck to show unused import warnings
```

### Solution 4: Add Missing Imports Automatically

Configure the IDE to automatically add missing imports when editing code.

```
# Auto-add imports on code completion:
File → Settings → Editor → General → Auto Import
# Java section:
#   ☑ Add unambiguous imports on the fly: Checked
#   ☑ Optimize imports on the fly: Checked
#   ☑ Class count to use import with '*': 999
#   ☑ Names count to use static import with '*': 999

# Manually add missing imports:
# 1. Place cursor on unresolved class name
# 2. Press Alt+Enter (Windows/Linux) / ⌥Enter (macOS)
# 3. Select 'Import class'
# Or use Ctrl+Alt+O to auto-import all
```

## Prevention Tips

- Enable 'Optimize imports on the fly' for automatic import cleanup as you type
- Set 'Class count to use import with *' to a high number (999) to prefer specific imports
- Use Ctrl+Alt+O regularly to keep imports clean before committing code
- Configure import ordering to match your team's code style conventions

## Related Errors

- [Format Error]({{< relref "/tools/intellij/format-error" >}})
- [Code Analysis Error]({{< relref "/tools/intellij/code-analysis-error" >}})
- [Inspection Error]({{< relref "/tools/intellij/inspection-error" >}})
