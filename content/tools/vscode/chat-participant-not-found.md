---
title: "[Solution] VS Code Chat Participant Not Found"
description: "Fix VS Code chat participant not found errors. Resolve issues when Copilot Chat participants do not respond."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Chat Participant Not Found

Fix VS Code chat participant not found errors. Resolve issues when Copilot Chat participants do not respond.

## Common Causes

- Chat participant extension is not installed or has been disabled
- Participant name referenced in the command does not match registration
- Copilot Chat API is not available in the current VS Code version
- Extension providing the participant failed during activation

## How to Fix

### Verify VS Code Chat Participant Not Found Configuration

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