---
title: "[Solution] Bash Readline Inputrc Error"
description: "Fix Bash readline inputrc configuration errors when keyboard shortcuts and history search fail."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Bash Readline Inputrc Error

Bash readline configuration in inputrc or .inputrc causes incorrect keyboard behavior.

```
inputrc: line 50: parse error
```

## Common Causes

- Syntax error in .inputrc file
- Unclosed quotes in key binding definitions
- Incorrect terminal capability definitions
- Readline not reloaded after changes
- Conflict with system-wide inputrc

## How to Fix

### Check inputrc Syntax

```bash
# Test inputrc for errors
bind -f ~/.inputrc

# Reload without restarting bash
bind -f ~/.inputrc
```

### Correct Key Binding Syntax

```bash
# ~/.inputrc

# Fix backspace
"\C-?": backward-delete-char

# Ctrl+R reverse search
"\C-r": reverse-search-history

# Alt+Left/Right word movement
"\e[1;3D": backward-word
"\e[1;3C": forward-word
```

### Set History Search

```bash
# ~/.inputrc
"\e[A": history-search-backward
"\e[B": history-search-forward

# Case-insensitive completion
set completion-ignore-case on

# Show all matches if ambiguous
set show-all-if-ambiguous on
```

### Load System-Wide Config

```bash
# Check system inputrc
cat /etc/inputrc

# Override in user file
# ~/.inputrc takes precedence
```

### Test Bindings

```bash
# List current bindings
bind -p

# List specific binding
bind -p | grep "\C-r"

# Test a binding
bind '"\C-x\C-r": re-read-init-file'
```

## Examples

```bash
# ~/.inputrc - complete configuration
set editing-mode vi
set enable-keypad on
set input-meta on
set output-meta on

"\C-?": backward-delete-char
"\C-h": backward-delete-char
"\e[A": history-search-backward
"\e[B": history-search-forward
"\C-w": backward-kill-word
```
