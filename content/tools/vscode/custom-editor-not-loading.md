---
title: "[Solution] VS Code Custom Editor Not Loading"
description: "Fix VS Code custom editor not loading errors. Resolve issues when custom editors fail to open files."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Custom Editor Not Loading

Fix VS Code custom editor not loading errors. Resolve issues when custom editors fail to open files.

## Common Causes

- Custom editor extension does not declare support for the file type
- Webview panel provider returns undefined or throws during creation
- File scheme is not supported by the registered custom editor
- Activation event for the custom editor has not been triggered yet

## How to Fix

### Verify VS Code Custom Editor Not Loading Configuration

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