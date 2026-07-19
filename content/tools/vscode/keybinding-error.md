---
title: "[Solution] VS Code Keybinding conflict detected"
description: "Fix VS Code keybinding conflicts. Resolve issues when keyboard shortcuts are duplicated or not working as expected."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "vscode"
tags: ["vscode", "ide", "keybindings", "shortcuts", "configuration"]
severity: "error"
---

# Keybinding conflict detected

## Error Message

```
Keybinding conflict detected: 'ctrl+shift+p' is bound to 3 different commands. Only the first bound command will be executed. Check your keybindings.json.
```

## Common Causes

- Multiple extensions define the same keyboard shortcut
- Custom keybindings.json conflicts with extension keybindings
- Platform-specific keybindings not properly configured
- When clause contexts are not restricting keybinding activation

## Solutions

### Solution 1: List All Keybinding Conflicts

Open the Keyboard Shortcuts editor and filter by conflict to see all duplicated keybindings.

```
code --command 'workbench.action.openGlobalKeybindingFile'
```

### Solution 2: Override Conflicting Keybindings

Add keybindings to your keybindings.json to override extension defaults with higher priority.

```
[{"key": "ctrl+shift+p", "command": "workbench.action.showCommands", "when": "editorTextFocus"}, {"key": "ctrl+shift+p", "command": "-myExtension.customCommand"}]
```

### Solution 3: Disable Extension Keybindings

Create a when clause that disables specific extension keybindings when they conflict with your workflow.

```
[{"key": "ctrl+shift+f", "command": "-editor.action.triggerSuggest", "when": "editorTextFocus && !suggestWidgetVisible"}]
```

## Prevention Tips

- Use the Keyboard Shortcuts editor to visually identify conflicts
- Add when clauses to prevent keybindings from activating unexpectedly
- Document your custom keybindings for team consistency

## Related Errors

- [Extension activation failed]({{< relref "/tools/vscode/extension-activation-failed" >}})
- [Unable to open workspace]({{< relref "/tools/vscode/workspace-error" >}})
- [File association error]({{< relref "/tools/vscode/file-association-error" >}})
