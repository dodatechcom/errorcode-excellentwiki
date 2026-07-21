---
title: "[Solution] VS Code Live Share Session Join Failed"
description: "Fix VS Code Live Share session join failed errors. Resolve issues when joining a collaborative session fails."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Live Share Session Join Failed

Fix VS Code Live Share session join failed errors. Resolve issues when joining a collaborative session fails.

## Common Causes

- Invitation link has expired or was revoked by the host
- Firewall is blocking the required ports for Live Share connections
- VS Code Live Share extension is outdated and needs to be updated
- Authentication token is invalid or the guest account lacks permissions

## How to Fix

### Verify VS Code Live Share Session Join Failed Configuration

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