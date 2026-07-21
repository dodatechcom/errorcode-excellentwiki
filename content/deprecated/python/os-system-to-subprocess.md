---
title: "[Solution] Deprecated Function Migration: os.system() to subprocess"
description: "Migrate from deprecated os.system() to subprocess.run() in Python for safer and more flexible command execution."
deprecated_function: "os.system()"
replacement_function: "subprocess.run()"
languages: ["python"]
deprecated_since: "Python 2.6+"
---

# [Solution] Deprecated Function Migration: os.system() to subprocess

The `os.system()` has been deprecated in favor of `subprocess.run()`.

## Migration Guide

os.system() runs a shell command and returns the exit code but provides no error handling or output capture. subprocess.run() gives full control over input, output, errors, and return codes.

Always use subprocess.run() over os.system(). Pass arguments as a list to avoid shell injection.

## Before (Deprecated)

```python
os.system("ls -la /tmp")
os.system("grep pattern file.txt")
os.system("python script.py arg1 arg2")
os.system("rm -rf " + user_input)  # dangerous
```

## After (Modern)

```python
import subprocess

result = subprocess.run(["ls", "-la", "/tmp"], capture_output=True, text=True)
print(result.stdout, result.returncode)

result = subprocess.run(["grep", "pattern", "file.txt"], capture_output=True, text=True)

subprocess.run(["python", "script.py", "arg1", "arg2"], check=True)
```

## Key Differences

- subprocess.run() returns CompletedProcess with stdout, stderr, returncode
- Use check=True to raise on non-zero exit
- Pass arguments as a list to avoid shell injection
