---
title: "Solved Python Bandit Error — How to Fix"
date: 2026-03-20T10:35:20+00:00
description: "Learn how to resolve Python Bandit security linter configuration errors and false positive handling."
categories: ["python"]
keywords: ["python bandit", "bandit error", "security linter", "bandit configuration", "bandit scan"]
error-types: ["runtime-error"]
severities: ["error"]
languages: ["python"]
weight: 5
comments: true
---

## Why It Happens

Bandit errors arise when the security linter detects potential vulnerabilities or when configuration issues prevent proper scanning. False positives and overly strict rules often complicate the scanning process.

Common causes include:
- Incorrectly configured exclusion patterns
- Inline `# nosec` annotations missing for known-safe code
- Configuration file syntax errors
- Missing plugins for custom security checks
- Scanning generated code or test files unintentionally

## Common Error Messages

```bash
$ bandit -r src/
[main]  INFO    profile include tests.testset
[main]  INFO    cli include tests.bandit
Run started:2026-03-20T10:00:00
[node_visitor]  WARNING  Unable to find qualified name for class
```

```bash
# Configuration error
Error: Could not read config file .bandit
```

```bash
# High severity finding
>> Issue: [B602:subprocess_popen_with_shell_true] subprocess call with shell=True identified
```

## How to Fix It

### 1. Configure Bandit with pyproject.toml

Set up comprehensive Bandit configuration.

```toml
# pyproject.toml
[tool.bandit]
exclude_dirs = ["tests", "venv", ".git", "build", "dist"]
skips = ["B101"]  # Skip assert warnings in all files
exclude = ["B101", "B311"]  # Also excludes these
tests = ["B201", "B301"]  # Only test these plugins
plugins = ["bandit.plugins.general"]

[tool.bandit.per-file-ignores]
"tests/**/*.py" = ["B101", "B102", "B110"]
"**/conftest.py" = ["B101"]
"scripts/**/*.py" = ["B101", "B602"]
```

```ini
# .bandit file (alternative)
[bandit]
exclude = tests,.venv,build
skips = B101,B102
```

```bash
# Run with configuration
bandit -r src/ -c pyproject.toml
bandit -r src/ -f json -o bandit-report.json
bandit -r src/ -ll  # Only medium and high severity
bandit -r src/ -ii  # Only high confidence
```

### 2. Handle False Positives Properly

Use inline annotations to suppress known-safe patterns.

```python
import subprocess
import os

# Safe: Using subprocess with shell=False (default)
def run_command(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, shell=False, capture_output=True)

# Suppress specific finding with reason
def run_shell_command(command: str) -> subprocess.CompletedProcess:
    # nosec B602 - Command is validated and sanitized before use
    return subprocess.run(command, shell=True, capture_output=True)

# Use context manager for safe file operations
import hashlib

def hash_file(path: str) -> str:
    sha256 = hashlib.sha256()  # nosec B303 - SHA256 is not used for security
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

# Disable specific checks for entire module
# bandit skips: B101,B311
```

### 3. Create Custom Bandit Plugins

Extend Bandit with project-specific checks.

```python
# custom_checks.py
import ast
from bandit.core import node_visitor, issue, utils

class CustomHardcodedPasswordCheck(node_visitor.NodeVisitor):
    """Check for hardcoded passwords in configuration."""
    
    qualname = "hardcoded_password"
    
    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if node.func.id == "connect":
                for arg in node.args:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        if len(arg.value) > 5 and any(c.isdigit() for c in arg.value):
                            self._report_issue(node, "Possible hardcoded password")
        
        self.generic_visit(node)
    
    def _report_issue(self, node, message):
        self.decorator_utils.add_issue(
            node.lineno,
            issue.Severity.HIGH,
            issue.Confidence.MEDIUM,
            message
        )

# Register the plugin
def get_checkers():
    return [CustomHardcodedPasswordCheck]
```

```toml
# pyproject.toml - register custom plugins
[tool.bandit]
plugins = ["bandit.plugins.general", "custom_checks"]
```

## Common Scenarios

### Scenario 1: CI/CD Security Scanning

Integrate Bandit into CI pipeline:

```yaml
# .github/workflows/security.yml
name: Security Scan
on: [push, pull_request]

jobs:
  bandit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install Bandit
        run: pip install bandit[toml]
      
      - name: Run Bandit
        run: |
          bandit -r src/ -c pyproject.toml -f json -o bandit-report.json || true
          bandit -r src/ -c pyproject.toml -ll
      
      - name: Upload Report
        uses: actions/upload-artifact@v4
        with:
          name: bandit-report
          path: bandit-report.json
```

```python
# ci_bandit.py
import json
import subprocess
import sys

def run_bandit(src_dir="src", severity="low", confidence="low"):
    """Run Bandit with proper error handling."""
    
    cmd = [
        "bandit", "-r", src_dir,
        "-f", "json",
        "--severity-level", severity,
        "--confidence-level", confidence
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.stdout:
        report = json.loads(result.stdout)
        
        high_severity = [
            result for result in report["results"]
            if result["issue_severity"] == "HIGH"
        ]
        
        if high_severity:
            print(f"Found {len(high_severity)} high severity issues")
            for issue in high_severity:
                print(f"  {issue['filename']}:{issue['line_number']}: {issue['issue_text']}")
            sys.exit(1)
    
    return report

if __name__ == "__main__":
    run_bandit()
```

### Scenario 2: Custom Exclusions for Generated Code

```toml
# pyproject.toml - exclude generated files
[tool.bandit]
exclude_dirs = [
    "tests",
    "migrations",
    "node_modules",
    ".venv",
    "build",
    "dist",
    "**/*.generated.py"
]

[tool.bandit.per-file-ignores]
"**/migrations/**/*.py" = ["all"]
"**/generated/**/*.py" = ["all"]
"**/tests/**/*.py" = ["B101", "B102", "B110", "B311"]
"**/conftest.py" = ["B101", "B311"]
"**/scripts/**/*.py" = ["B101", "B602"]
```

## Prevent It

- Run Bandit as part of CI with `bandit -r src/ -ll` for medium+ severity
- Use `# nosec BXXX` with specific check codes and comments explaining the suppression
- Configure `exclude_dirs` to skip test files and virtual environments
- Review Bandit findings regularly to identify patterns that need architectural fixes
- Use `--format json` for machine-readable output in automated pipelines