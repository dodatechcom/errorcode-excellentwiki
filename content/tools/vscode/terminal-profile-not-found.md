---
title: "[Solution] VS Code Terminal Profile Not Found"
description: "Fix VS Code terminal profile not found errors. Resolve issues when custom terminal profiles fail to launch."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Terminal Profile Not Found

Fix VS Code terminal profile not found errors. Resolve issues when custom terminal profiles fail to launch.

## Common Causes

- Shell executable path is incorrect or the binary does not exist
- Terminal profile override is set to a non-existent profile name
- Default terminal profile detected by VS Code is not valid
- Environment variable for the shell path is undefined in the system

## How to Fix

### Verify VS Code Terminal Profile Not Found Configuration

Check your VS Code settings for the relevant configuration. Open settings.json and verify the correct values are set.

```json
{
  // Verify this setting is correctly configured
  "editor.customize": {
    "enabled": true
  }
}
```

### Restart VS Code

Close all VS Code windows and restart to clear the affected state.

```bash
# Close and reopen VS Code
code --new-window
```

### Check the Developer Console

1. Open the command palette with Ctrl+Shift+P
2. Run 'Developer: Toggle Developer Tools'
3. Look for error messages in the Console tab

### Update VS Code and Extensions

Ensure VS Code and all related extensions are on the latest version to avoid known bugs.

## Examples

```json
// settings.json
{
  "editor.suggestSelection": "first",
  "editor.wordBasedSuggestions": "allDocuments"
}
```