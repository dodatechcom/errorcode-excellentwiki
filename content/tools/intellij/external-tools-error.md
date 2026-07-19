---
title: "[Solution] IntelliJ IDEA External tools error"
description: "Fix IntelliJ IDEA external tools configuration errors. Resolve tool integration failures, path issues, and tool execution errors."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "external-tools", "tool-integration", "external-programs", "configuration"]
severity: "error"
---

# External tools error

## Error Message

```
External tools error
Cannot run external tool: program not found at '/usr/bin/mytool'
External tool 'Linter' exited with code 1
Working directory does not exist: /path/to/working/dir
External tool timeout: process did not complete within 30 seconds
```

## Common Causes

- External tool executable path is incorrect or the tool is not installed
- Working directory specified in tool configuration does not exist
- Tool execution exceeds the configured timeout limit
- Environment variables are missing or incorrectly configured
- Tool requires specific runtime or dependencies not available in PATH

## Solutions

### Solution 1: Configure External Tool Path

Set the correct path to the external tool executable in IDE settings.

```
File → Settings → Tools → External Tools
# Click '+' to add a new tool

# Configure:
#   Name: My Linter
#   Description: Code linter tool
#   Program: /usr/local/bin/mytool
#     (Use absolute path or which mytool to find it)
#   Arguments: $FilePath$
#   Working directory: $ProjectFileDir$

# To find the tool path:
which mytool
# or
command -v mytool
```

### Solution 2: Set Correct Working Directory

Configure the working directory using IDE macros for dynamic paths.

```bash
# Find available macros:
# In External Tools dialog, click 'Insert Macro'

# Common macros:
#   $FilePath$          → Full path of current file
#   $FileName$          → Name of current file
#   $FileDir$           → Directory of current file
#   $ProjectFileDir$    → Project root directory
#   $ModuleFileDir$     → Module root directory
#   $SelectedText$      → Currently selected text
#   $Clipboard$         → Clipboard contents

# For working directory, use:
$ProjectFileDir$
# Or: $FileDir$

# Verify the directory exists:
ls -la "$ProjectFileDir$"
```

### Solution 3: Increase Tool Execution Timeout

Increase the timeout for external tools that require more time to execute.

```
File → Settings → Tools → External Tools
# Select your tool → Edit
# Click 'Output' tab:
#   Timeout: 60000 (milliseconds)
#     Default is 30000 (30 seconds)
#     Increase for long-running tools

# Or disable timeout:
#   Uncheck 'Cancel process on first output'

# For tool output handling:
#   ☑ Open console with tool output: Checked
#   ☑ Save output to file: Optional (for large outputs)
#   Output file: $ProjectFileDir$/tool-output.log
```

### Solution 4: Configure Environment Variables

Set up environment variables required by the external tool.

```
File → Settings → Tools → External Tools
# Select your tool → Edit
# Click 'Output' tab → 'Environment variables'

# Add variables:
#   JAVA_HOME → /usr/lib/jvm/java-17-openjdk
#   PATH → /usr/local/bin:/usr/bin
#   MY_TOOL_CONFIG → /path/to/config

# Or use system environment variables:
#   ☑ Include system environment variables: Checked

# For complex environments, create a .env file:
#   Program: bash
#   Arguments: -c 'source .env && mytool $FilePath$'
```

## Prevention Tips

- Use IDE macros ($FilePath$, $ProjectFileDir$) for portable tool configurations
- Test external tools from the command line first before configuring in the IDE
- Create tool groups in External Tools to organize tools by category
- Use 'Output' tab settings to capture and review tool output for debugging

## Related Errors

- [Terminal Error]({{< relref "/tools/intellij/terminal-error" >}})
- [Database Error]({{< relref "/tools/intellij/database-error" >}})
- [Format Error]({{< relref "/tools/intellij/format-error" >}})
