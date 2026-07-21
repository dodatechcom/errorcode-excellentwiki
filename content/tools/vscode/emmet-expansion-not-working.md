---
title: "[Solution] VS Code Emmet Expansion Not Working"
description: "Fix VS Code emmet expansion not working errors. Resolve issues when Emmet abbreviations do not expand."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Emmet Expansion Not Working

Fix VS Code emmet expansion not working errors. Resolve issues when Emmet abbreviations do not expand.

## Common Causes

- Emmet extension is disabled or not included in the default extensions
- Trigger on tab setting is disabled in the editor configuration
- Current file type is not supported by Emmet by default
- Another extension is intercepting the tab key before Emmet

## How to Fix

### Verify VS Code Emmet Expansion Not Working Configuration

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