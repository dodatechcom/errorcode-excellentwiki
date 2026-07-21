---
title: "[Solution] VS Code Git Conflict Decorators Missing"
description: "Fix VS Code git conflict decorators missing errors. Resolve issues when merge conflict markers are not displayed."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Git Conflict Decorators Missing

Fix VS Code git conflict decorators missing errors. Resolve issues when merge conflict markers are not displayed.

## Common Causes

- Git extension is disabled or not loaded properly in VS Code
- File encoding causes the conflict markers to be invisible to the extension
- VS Code window needs to be refreshed to pick up new git state
- Repository contains nested submodules that confuse the git decorator

## How to Fix

### Verify VS Code Git Conflict Decorators Missing Configuration

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