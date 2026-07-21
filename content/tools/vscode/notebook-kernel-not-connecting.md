---
title: "[Solution] VS Code Notebook Kernel Not Connecting"
description: "Fix VS Code notebook kernel not connecting errors. Resolve issues when Jupyter or notebook kernels fail to connect."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Notebook Kernel Not Connecting

Fix VS Code notebook kernel not connecting errors. Resolve issues when Jupyter or notebook kernels fail to connect.

## Common Causes

- Kernel runtime package is not installed or not found in PATH
- Jupyter server is not running or the URL token has expired
- Kernel specification file is missing or contains invalid metadata
- Python environment does not have the required ipykernel package

## How to Fix

### Verify VS Code Notebook Kernel Not Connecting Configuration

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