---
title: "[Solution] VS Code Outline View Empty"
description: "Fix VS Code outline view empty errors. Resolve issues when the outline panel shows no symbols."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Outline View Empty

Fix VS Code outline view empty errors. Resolve issues when the outline panel shows no symbols.

## Common Causes

- Language server has not indexed the current file for symbols
- Outline view is filtered to exclude certain symbol kinds
- File contains no recognizable symbols such as functions or classes
- Workspace trust settings prevent the outline from populating

## How to Fix

### Verify VS Code Outline View Empty Configuration

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