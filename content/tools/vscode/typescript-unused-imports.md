---
title: "[Solution] VS Code TypeScript Unused Imports"
description: "Fix VS Code TypeScript unused imports warnings. Resolve issues when unused import diagnostics appear incorrectly."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code TypeScript Unused Imports

Fix VS Code TypeScript unused imports warnings. Resolve issues when unused import diagnostics appear incorrectly.

## Common Causes

- Import is used only as a type and requires the type-only import syntax
- Re-exported symbol is flagged as unused by the language service
- Dynamic import path causes the static analysis to miss the usage
- tsconfig isolatedModules setting reports false positives for some patterns

## How to Fix

### Verify VS Code TypeScript Unused Imports Configuration

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