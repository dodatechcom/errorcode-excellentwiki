---
title: "[Solution] VS Code Refactoring Not Available"
description: "Fix VS Code refactoring not available errors. Resolve issues when refactoring actions do not appear."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Refactoring Not Available

Fix VS Code refactoring not available errors. Resolve issues when refactoring actions do not appear.

## Common Causes

- Language server does not support refactoring for the current file type
- File contains syntax errors preventing the language server from analyzing code
- Light bulb icon is disabled in the editor settings
- Extension providing refactoring actions has been deactivated

## How to Fix

### Verify VS Code Refactoring Not Available Configuration

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