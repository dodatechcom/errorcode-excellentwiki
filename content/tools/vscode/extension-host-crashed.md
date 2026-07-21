---
title: "[Solution] VS Code Extension Host Crashed"
description: "Fix VS Code extension host crashed errors. Resolve issues when the extension host process unexpectedly terminates."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Extension Host Crashed

Fix VS Code extension host crashed errors. Resolve issues when the extension host process unexpectedly terminates.

## Common Causes

- Extension consuming excessive memory causing the host to be killed
- Incompatible extension version causing crash on activation
- Corrupted extension cache files preventing proper initialization
- Two or more extensions conflicting with each other at runtime

## How to Fix

### Verify VS Code Extension Host Crashed Configuration

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