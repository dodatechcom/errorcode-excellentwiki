---
title: "[Solution] Poetry Shell Completion Not Working Error — How to Fix"
description: "Fix Poetry shell completion not working errors. Enable tab completion for bash, zsh, and fish shells, and resolve Poetry completion configuration issues."
tools: ["poetry"]
error-types: ["completion-error"]
severities: ["error"]
weight: 5
comments: true
---

This error means Poetry's shell completion is not functioning. Tab completion for Poetry commands and options does not work, or the completion script failed to generate or load correctly.

## Why It Happens

- Poetry's completion script was never added to your shell's configuration file
- The completion script is outdated after a Poetry update
- Your shell type is not detected correctly (bash, zsh, fish)
- The completion script references a Poetry path that no longer exists after reinstall
- Shell configuration files are not sourced in the current session
- The Poetry binary is installed in a non-standard location

## Common Error Messages

```
poetry: command not found (when running poetry completion)
```

```
PoetryException

Could not determine shell type.
```

```
bash: completion function for poetry not found
```

```
/opt/homebrew/bin/poetry: line 1: Poetry: command not found
```

## How to Fix It

### 1. Generate the Completion Script

```bash
# For bash
poetry completion bash > ~/.bash-completion.d/poetry

# For zsh
poetry completion zsh > ~/.zfunc/_poetry

# For fish
poetry completion fish > ~/.config/fish/completions/poetry.fish
```

### 2. Source the Completion Script

**Bash:**

```bash
# Add to ~/.bashrc
echo 'source ~/.bash-completion.d/poetry' >> ~/.bashrc
source ~/.bashrc
```

**Zsh:**

First, ensure a completion directory exists:

```bash
mkdir -p ~/.zfunc
```

Add to `~/.zshrc`:

```bash
fpath+=~/.zfunc
autoload -Uz compinit && compinit
```

Then regenerate the completion script:

```bash
poetry completion zsh > ~/.zfunc/_poetry
```

Restart your shell or run:

```bash
source ~/.zshrc
```

**Fish:**

```bash
poetry completion fish > ~/.config/fish/completions/poetry.fish
source ~/.config/fish/config.fish
```

### 3. Regenerate After Poetry Update

```bash
poetry self update
poetry completion bash > ~/.bash-completion.d/poetry
source ~/.bashrc
```

### 4. Verify Completion Is Working

```bash
# Bash
complete -p poetry

# Zsh
which _poetry

# Fish
complete -c poetry
```

### 5. Fix Non-Standard Installation Paths

```bash
# Find Poetry's actual path
which poetry

# Use the full path in the completion script
poetry completion bash | sed "s|poetry|$(which poetry)|g" > ~/.bash-completion.d/poetry
```

### 6. Enable Completion via Poetry Config

```bash
poetry config virtualenvs.create false
```

If Poetry is installed globally via pipx, ensure the completion script references the correct binary.

## Common Scenarios

**Completion works in new terminal but not existing ones.** You need to source the completion script in your current session:

```bash
source ~/.bash-completion.d/poetry
```

**Poetry installed via Homebrew does not complete.** Homebrew may install completions to a different path. Check:

```bash
ls $(brew --prefix)/etc/bash_completion.d/
```

If Poetry is not there, generate it manually.

**Completion works for `poetry` but not `poetry run`.** The completion script handles all Poetry subcommands. Ensure you are using the latest version of the completion script.

## Prevent It

1. Regenerate the completion script after every Poetry update to ensure compatibility
2. Add the completion script to your shell's startup file so it loads automatically in every new session
3. Use `poetry completion <shell>` to generate the correct script for your shell instead of manually writing one
