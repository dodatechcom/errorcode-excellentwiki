---
title: "[Solution] VS Code Remote SSH Connection Refused"
description: "Fix VS Code remote SSH connection refused errors. Resolve issues when SSH connections to remote hosts fail."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Remote SSH Connection Refused

Fix VS Code remote SSH connection refused errors. Resolve issues when SSH connections to remote hosts fail.

## Common Causes

- SSH server on the remote host is not running or listening on the expected port
- Firewall rules blocking the SSH connection on the remote machine
- Incorrect SSH host key or host key verification failure
- SSH configuration file contains incorrect hostname or port settings

## How to Fix

### Verify VS Code Remote SSH Connection Refused Configuration

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