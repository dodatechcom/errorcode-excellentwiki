---
title: "[Solution] VS Code Port Forwarding Not Working"
description: "Fix VS Code port forwarding not working errors. Resolve issues when remote port forwarding fails in tunnel sessions."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Port Forwarding Not Working

Fix VS Code port forwarding not working errors. Resolve issues when remote port forwarding fails in tunnel sessions.

## Common Causes

- Port is already in use on the local machine by another application
- SSH tunnel configuration does not include the required port mapping
- Remote server is not listening on the expected interface or port
- Permission denied on the remote host for the requested port binding

## How to Fix

### Verify VS Code Port Forwarding Not Working Configuration

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