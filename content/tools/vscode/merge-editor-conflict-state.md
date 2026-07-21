---
title: "[Solution] VS Code Merge Editor Conflict State"
description: "Fix VS Code merge editor conflict state errors. Resolve issues when conflict markers are not properly resolved."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Merge Editor Conflict State

Fix VS Code merge editor conflict state errors. Resolve issues when conflict markers are not properly resolved.

## Common Causes

- Merge editor did not save the resolved state of all conflicting blocks
- Incoming or current changes were accidentally discarded
- File encoding changed between the merge base and the current branch
- Three-way merge base cannot be determined from the commit history

## How to Fix

### Verify VS Code Merge Editor Conflict State Configuration

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