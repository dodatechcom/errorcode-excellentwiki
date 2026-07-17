---
title: "[Solution] Brew Python Error — Fix Homebrew Python Formula Conflicts"
description: "Fix Homebrew Python errors when brew python conflicts with system or other Python versions. Link, unlink, and configure PATH for the correct Python interpreter."
tools: ["brew"]
error-types: ["conflict-error"]
severities: ["error"]
weight: 5
---

This error means Homebrew detected a conflict between Python versions or the Homebrew Python installation is broken. Multiple Python formulas can coexist, but linking and PATH issues cause failures.

## What This Error Means

Homebrew provides `python@3.11`, `python@3.12`, etc. as separate formulas. When you install one, it may conflict with an already-linked version or with the macOS system Python:

```
Error: Cannot install python@3.11 because conflicting formulae are installed:
  python@3.12

Please `brew unlink python@3.12` before continuing.
```

Or:

```
Error: Python is required to be installed but could not be found
```

## Why It Happens

- Two Python versions are both linked into `/usr/local/bin`
- The macOS system Python path takes precedence over Homebrew's Python
- A formula depends on `python3` and Homebrew cannot resolve which version to use
- After upgrading macOS, the system Python changed and broke symlinks
- `pip` commands use a different Python than `python3`

## How to Fix It

### Link and Unlink Python Versions

```bash
brew unlink python@3.12
brew link python@3.11 --force --overwrite
```

### Use Version-Specific Commands

```bash
python3.11 --version
python3.12 --version
pip3.11 install <package>
```

### Set the Default Python via PATH

```bash
# In ~/.zshrc or ~/.bashrc
export PATH="/opt/homebrew/opt/python@3.11/bin:$PATH"
```

### Use a Virtual Environment

```bash
/opt/homebrew/opt/python@3.11/bin/python3.11 -m venv .venv
source .venv/bin/activate
```

### Check Which Python Is Being Used

```bash
which python3
which pip3
python3 --version
```

Ensure the output matches the version you expect.

### Force Overwrite Symlinks

```bash
brew link --overwrite python@3.11
```

This removes conflicting symlinks from other Python versions.

### Uninstall the Unneeded Version

```bash
brew uninstall python@3.12
brew install python@3.11
```

## Common Mistakes

- Assuming `python3` always points to the Homebrew Python
- Not using virtual environments and relying on system-wide Python links
- Running `brew upgrade` which may switch the linked Python version
- Mixing `pip install` (system) and `pip3 install` (Homebrew)
- Installing Python via pyenv without configuring it to work alongside Homebrew formulas

## Related Pages

- [Brew Install Error]({{< relref "/tools/brew/brew-install-error" >}}) -- formula installation failures
- [Brew Dependency Error]({{< relref "/tools/brew/brew-dependency-error" >}}) -- missing dependencies
- [Brew Xcode Error]({{< relref "/tools/brew/brew-xcode-error" >}}) -- Xcode tools required
