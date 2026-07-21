---
title: "[Solution] VS Code Git Decorations Not Showing"
description: "Fix VS Code git decorations not showing errors. Resolve issues when source control indicators disappear."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Git Decorations Not Showing

Fix VS Code git decorations not showing errors. Resolve issues when source control indicators disappear.

## Common Causes

- Git integration is disabled in the source control settings
- Repository is too large causing the git extension to time out
- Git extension cannot find the git executable on the system PATH
- File is outside the workspace folder and not tracked by git

## How to Fix

### Verify VS Code Git Decorations Not Showing Configuration

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