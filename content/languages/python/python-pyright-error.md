---
title: "Solved Python Pyright Error — How to Fix"
date: 2026-03-20T10:30:00+00:00
description: "Learn how to resolve Python Pyright type checker configuration, strict mode, and type inference errors."
categories: ["python"]
keywords: ["python pyright", "pyright error", "pyright config", "pyright strict", "pyright type error"]
error-types: ["runtime-error"]
severities: ["error"]
languages: ["python"]
weight: 5
comments: true
---

## Why It Happens

Pyright errors occur when the static type checker finds type inconsistencies, missing imports, or configuration issues. Pyright's strict mode is particularly demanding and can surface latent type bugs.

Common causes include:
- Missing `pyrightconfig.json` or incorrect settings
- Type stubs not available for third-party packages
- Strict mode flags revealing previously hidden type issues
- Python version compatibility affecting available types
- Virtual environment not properly configured for type resolution

## Common Error Errors

```bash
$ pyright
No pyrightconfig.json; using default settings
error: Import "requests" could not be resolved
```

```bash
# Type mismatch
error: Argument of type "str" cannot be assigned to parameter of type "int"
```

```bash
# Missing stub
error: Import "untyped_lib" could not be resolved (reportMissingImports)
```

## How to Fix It

### 1. Configure Pyright Properly

Create comprehensive `pyrightconfig.json`.

```json
{
  "include": ["src"],
  "exclude": ["**/node_modules", "**/__pycache__", "tests"],
  "typeCheckingMode": "strict",
  "pythonVersion": "3.11",
  "pythonPlatform": "Linux",
  
  "reportMissingImports": true,
  "reportMissingTypeStubs": true,
  "reportUnknownMemberType": true,
  "reportUnknownParameterType": true,
  "reportUnknownVariableType": true,
  "reportUnknownArgumentType": true,
  "reportUnknownLambdaType": true,
  "reportUnknownDecoratorType": true,
  "reportUnknownVariableType": true,
  "reportGeneralTypeIssues": true,
  "reportPrivateUsage": true,
  "reportUntypedFunctionDecorator": true,
  "reportUntypedClassDecorator": true,
  
  "autoImportCompletions": true,
  "useLibraryCodeForTypes": true,
  
  "stubPath": "./stubs",
  
  "extraPaths": ["./src"],
  
  "executionEnvironments": [
    {
      "root": "./src",
      "extraPaths": ["./vendor"],
      "pythonVersion": "3.11"
    }
  ]
}
```

```bash
# Run Pyright
pyright
pyright --watch  # Watch mode
pyright --pythonversion 3.10  # Specific version
```

### 2. Handle Type Stubs and Missing Imports

Configure stub paths for untyped libraries.

```bash
# Install type stubs
pip install types-requests
pip install types-PyYAML

# Create custom stubs
mkdir -p stubs/mylibrary
```

```python
# stubs/mylibrary/__init__.pyi
from typing import Any, Dict, List, Optional, Union

def connect(
    host: str,
    port: int = 8080,
    timeout: Optional[float] = None
) -> 'Connection': ...

class Connection:
    def query(self, sql: str, params: Optional[Dict] = None) -> List[Dict[str, Any]]: ...
    def execute(self, sql: str, params: Optional[Dict] = None) -> int: ...
    def close(self) -> None: ...
    
    def __enter__(self) -> 'Connection': ...
    def __exit__(self, *args: Any) -> None: ...

class Error(Exception): ...
class ConnectionError(Error): ...
class QueryError(Error): ...
```

```json
// pyrightconfig.json additions
{
  "stubPath": "./stubs",
  "extraPaths": [
    "./vendor",
    "./typings"
  ]
}
```

### 3. Use Pyright's Strict Mode Effectively

Enable strict checking incrementally.

```python
# pyright: strict

from typing import TypeVar, Generic, Protocol

T = TypeVar('T')

# Strict mode catches these issues
def process(x: T) -> T:  # OK
    return x

def broken(x: int) -> str:  # Error: return type mismatch
    return x  # pyright will catch this

# Use type: ignore for known issues
x: int = "string"  # type: ignore[assignment]

# Use overloads for flexible signatures
from typing import overload

@overload
def fetch(url: str) -> str: ...
@overload
def fetch(url: str, as_json: bool) -> dict: ...
def fetch(url: str, as_json: bool = False) -> str | dict:
    if as_json:
        return {"url": url}
    return url
```

```json
// Incremental strict mode configuration
{
  "typeCheckingMode": "standard",
  
  "reportMissingImports": "error",
  "reportMissingTypeStubs": "warning",
  "reportGeneralTypeIssues": "error",
  "reportPrivateUsage": "warning",
  "reportUntypedFunctionDecorator": "warning",
  "reportUntypedClassDecorator": "warning",
  "reportUnknownMemberType": "none",
  "reportUnknownParameterType": "none",
  "reportUnknownVariableType": "none"
}
```

## Common Scenarios

### Scenario 1: VS Code Integration

Configure Pyright for VS Code development:

```json
// .vscode/settings.json
{
  "python.analysis.typeCheckingMode": "strict",
  "python.analysis.autoImportCompletions": true,
  "python.analysis.useLibraryCodeForTypes": true,
  "python.analysis.diagnosticMode": "workspace",
  "python.analysis.stubPath": "./stubs"
}
```

### Scenario 2: CI/CD Integration

```yaml
# .github/workflows/typecheck.yml
name: Type Check
on: [push, pull_request]

jobs:
  pyright:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install Pyright
        run: npm install -g pyright
      
      - name: Run Pyright
        run: pyright --outputjson | python -c "
          import json, sys
          data = json.load(sys.stdin)
          errors = data.get('summary', {}).get('errorCount', 0)
          if errors > 0:
              print(f'Found {errors} type errors')
              sys.exit(1)
          print('No type errors found')
        "
```

## Prevent It

- Use `pyright --verifytypes package_name` to check type completeness
- Enable `reportMissingImports` as error to catch import issues early
- Use `type: ignore[code]` with specific error codes for necessary suppressions
- Configure `executionEnvironments` for projects with multiple Python versions
- Run `pyright --outputjson` in CI for structured error reporting