---
title: "[Solution] IntelliJ IDEA Code formatting error"
description: "Fix IntelliJ IDEA code formatting failures. Resolve code style issues, formatter configuration errors, and reformatting problems."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "formatting", "code-style", "reformat", "indentation"]
severity: "error"
---

# Code formatting error

## Error Message

```
Code formatting error
Reformat Code failed: internal error
Formatter cannot format: incomplete code
Formatting changes would introduce syntax errors
Code style configuration error: unknown option 'WRAP_LONG_LINES'
```

## Common Causes

- Code contains syntax errors that prevent safe reformatting
- Code style configuration file is corrupted or has invalid settings
- Formatter plugin conflict with built-in formatter
- Code contains text blocks or raw strings that are hard to format
- Custom file type formatter is not configured

## Solutions

### Solution 1: Reformat Code with Correct Shortcuts

Use the correct keyboard shortcuts to reformat code according to the project's code style.

```
# Reformat whole file:
Ctrl+Alt+L (Windows/Linux)
⌥⌘L (macOS)

# Reformat selected code:
1. Select the code
2. Ctrl+Alt+L

# Optimize imports simultaneously:
Ctrl+Alt+O (Windows/Linux)
⌃⌥O (macOS)

# Reformat on commit:
# Settings → Tools → Actions on Save
# ☑ Reformat code
# ☑ Optimize imports
# ☑ Rearrange code
```

### Solution 2: Configure Code Style Settings

Configure the project's code style settings to match your team's conventions.

```
File → Settings → Editor → Code Style

# Key settings:
#   Java tab:
#     ☑ Use custom indent size: 4 spaces
#     ☑ Tab size: 4
#     ☑ Indent: 4
#     ☑ Continuation indent: 8

#   Right margin (columns): 120
#     ☑ Wrap at right margin: Checked

# Import/Export code style:
#   Click 'Manage' → 'Import' → Select XML file
#   Or export your team's code style:
#   Click 'Manage' → 'Export' → Save as XML
```

### Solution 3: Fix Formatter Configuration File

Reset or fix the code style configuration file if it is corrupted.

```xml
<!-- .idea/codeStyles/codeStyleConfig.xml -->
<component name="ProjectCodeStyleConfiguration">
  <state>
    <option name="USE_PER_PROJECT_SETTINGS" value="true" />
  </state>
</component>

<!-- .idea/codeStyles/Project.xml -->
<component name="ProjectCodeStyleConfiguration">
  <codeScheme name="Project" version="173">
    <option name="RIGHT_MARGIN" value="120" />
    <option name="WRAP_LONG_LINES" value="false" />
    <JavaCodeStyleSettings>
      <option name="CLASS_COUNT_TO_USE_IMPORT_ON_DEMAND" value="999" />
    </JavaCodeStyleSettings>
  </codeScheme>
</component>

# If configuration is corrupted, delete .idea/codeStyles/
# and reconfigure via File → Settings → Editor → Code Style
```

### Solution 4: Disable Formatting for Specific Code Sections

Use formatting markers to prevent the formatter from modifying specific code sections.

```java
// @formatter:off
// This code will not be reformatted
int[] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};
// @formatter:on

// For XML/HTML:
<!-- @formatter:off -->
<div>
    <span>Preserved formatting</span>
</div>
<!-- @formatter:on -->

# Configure formatting markers:
# File → Settings → Editor → Code Style
# → Formatter Control
# ☑ Enable formatter markers in comments: Checked
```

## Prevention Tips

- Configure 'Actions on Save' to automatically reformat and optimize imports
- Use .editorconfig files to share formatting rules across IDEs and team members
- Export and share code style settings via version control for team consistency
- Use Ctrl+Alt+L with 'Reformat only changed code' for faster formatting on large files

## Related Errors

- [Optimize Imports Error]({{< relref "/tools/intellij/optimize-imports-error" >}})
- [Code Analysis Error]({{< relref "/tools/intellij/code-analysis-error" >}})
- [Generate Error]({{< relref "/tools/intellij/generate-error" >}})
