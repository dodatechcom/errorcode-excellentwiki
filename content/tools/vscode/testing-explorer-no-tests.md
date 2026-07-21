---
title: "[Solution] VS Code Testing Explorer No Tests"
description: "Fix VS Code testing explorer no tests errors. Resolve issues when the test explorer shows no discovered tests."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Testing Explorer No Tests

Fix VS Code testing explorer no tests errors. Resolve issues when the test explorer shows no discovered tests.

## Common Causes

- Test framework adapter extension is not installed for the project
- Test configuration file is missing or points to incorrect paths
- Workspace trust is not enabled preventing test discovery
- Test file naming pattern does not match what the adapter expects

## How to Fix

### Verify VS Code Testing Explorer No Tests Configuration

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