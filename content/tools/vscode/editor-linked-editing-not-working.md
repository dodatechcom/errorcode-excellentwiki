---
title: "[Solution] VS Code Editor Linked Editing Not Working"
description: "Fix VS Code linked editing not working errors. Resolve issues when simultaneous tag or bracket editing fails."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Editor Linked Editing Not Working

Fix VS Code linked editing not working errors. Resolve issues when simultaneous tag or bracket editing fails.

## Common Causes

- Linked editing is not enabled for the current language in settings
- File contains malformed HTML or XML preventing tag detection
- Cursor is not positioned on a tag name that supports linked editing
- Extension providing linked editing support is not installed

## How to Fix

### Verify VS Code Editor Linked Editing Not Working Configuration

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