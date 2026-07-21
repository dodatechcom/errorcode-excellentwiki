---
title: "[Solution] macOS Python Error -- Python Not Working or Command Not Found"
description: "Fix macOS Python error when Python is not installed or Python commands fail on Mac. Resolve Python installation issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Python Error -- Python Not Working or Command Not Found

Python is a widely-used programming language. On macOS, Python may not be installed, or multiple versions may conflict with each other.

## Common Causes
- Python is not installed (removed from macOS in recent versions)
- Multiple Python versions are installed and conflicting
- PATH does not include the Python installation directory
- pip is not installed or not working
- Virtual environment is corrupted

## How to Fix
1. Install Python via Homebrew for the latest version
2. Use pyenv to manage multiple Python versions
3. Check PATH configuration for Python
4. Install pip if it is missing
5. Recreate virtual environments if corrupted

```bash
# Install Python via Homebrew
brew install python

# Check Python version
python3 --version

# Check pip
pip3 --version

# Install pyenv for version management
brew install pyenv
```

## Examples

```bash
# Check which Python is being used
which python3

# List installed Python versions
ls -la /usr/local/bin/python*
```

This error is common when Python is not installed (removed from macOS Catalina+), when multiple Python versions conflict, or when the PATH does not include the Python directory.
