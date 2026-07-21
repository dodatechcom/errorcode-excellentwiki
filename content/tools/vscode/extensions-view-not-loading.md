---
title: "[Solution] VS Code Extensions View Not Loading"
description: "Fix VS Code extensions view not loading errors. Resolve issues when the extensions marketplace panel is blank."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Extensions View Not Loading

Fix VS Code extensions view not loading errors. Resolve issues when the extensions marketplace panel is blank.

## Common Causes

- Network connection to the marketplace server is blocked or slow
- VS Code authentication token has expired and needs refresh
- Cache directory for the extensions view is corrupted on disk
- Proxy settings are misconfigured preventing marketplace API access

## How to Fix

### Verify VS Code Extensions View Not Loading Configuration

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