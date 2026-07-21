---
title: "[Solution] Bash Prompt Escape Sequence Error"
description: "Fix Bash PS1 prompt escape sequence errors when custom prompts display raw escape codes."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Bash Prompt Escape Sequence Error

Bash PS1 prompt shows raw escape codes instead of formatted output.

```
\[033[01;32m\]user@host\[033[00m\]
```

## Common Causes

- Single quotes used instead of double quotes for PS1
- Missing \[ and \] around non-printing sequences
- Incorrect escape code format
- Terminal does not support color codes
- PS1 set in wrong shell config file

## How to Fix

### Use Double Quotes for PS1

```bash
# Wrong - single quotes prevent escape interpretation
PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\w\$ '

# Correct - double quotes allow escape interpretation
PS1="\[\033[01;32m\]\u@\h\[\033[00m\]:\w\$ "
```

### Wrap Non-Printing Characters

```bash
# Colors and formatting must be wrapped in \[ \]
PS1="\[\033[1;34m\][\u@\h \W]\$\[\033[0m\] "
```

### Use Tput for Portable Prompts

```bash
PS1="$(tput bold)$(tput setaf 2)\u@\h$(tput sgr0):\w\$ "
```

### Configure in .bashrc

```bash
# ~/.bashrc
if [[ $- == *i* ]]; then
    PS1="\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ "
fi
```

### Add Git Branch to Prompt

```bash
parse_git_branch() {
    git branch 2>/dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

PS1="\[\033[01;32m\]\u@\h\[\033[00m\]:\w\[\033[01;33m\]\$(parse_git_branch)\[\033[00m\]\$ "
```

## Examples

```bash
# Colorful prompt with timestamp
PS1="\[\033[01;36m\][\t] \[\033[01;32m\]\u@\h:\[\033[01;34m\]\w\[\033[00m\]\n\$ "

# Minimal prompt
PS1="\W\$ "

# Prompt with exit code of last command
PS1="\[\033[01;31m\][\$?]\[\033[00m\] \u@\h:\w\$ "
```
