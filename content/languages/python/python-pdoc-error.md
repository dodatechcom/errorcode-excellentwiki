---
title: "Solved Python pdoc Error — How to Fix"
date: 2026-03-20T10:10:45+00:00
description: "Learn how to resolve Python pdoc documentation generation errors and module scanning issues."
categories: ["python"]
keywords: ["python pdoc", "pdoc error", "pdoc documentation", "pdoc module", "pdoc build error"]
error-types: ["runtime-error"]
severities: ["error"]
languages: ["python"]
weight: 5
comments: true
---

## Why It Happens

pdoc errors occur when the lightweight documentation generator fails to import modules, parse docstrings, or generate HTML output. Unlike Sphinx, pdoc directly imports your modules, making import errors more frequent.

Common causes include:
- Module dependencies not installed in the documentation environment
- Circular imports between modules
- Syntax errors in docstrings or type annotations
- Modules with side effects on import
- Missing `__all__` causing unexpected public API

## Common Error Messages

```bash
$ pdoc mypackage
Could not import module 'mypackage.submodule'
```

```bash
# Import error
ModuleNotFoundError: No module named 'numpy'
```

```bash
# Syntax error in docstring
SyntaxError: invalid syntax in docstring
```

## How to Fix It

### 1. Configure pdoc with Proper Settings

Set up pdoc for reliable documentation generation.

```python
# generate_docs.py
import pdoc
from pathlib import Path

def generate_docs(module_name, output_dir="docs"):
    """Generate documentation for a module."""
    
    # Configure pdoc
    pdoc_config = pdoc.ModuleConfig()
    pdoc_config.show_source = True
    pdoc_config.show_inherited_members = True
    pdoc_config.show_root_heading = True
    
    # Import and document the module
    try:
        module = pdoc.import_module(module_name)
    except ImportError as e:
        print(f"Failed to import {module_name}: {e}")
        return False
    
    # Generate HTML
    html = pdoc.render(
        module,
        format=pdoc.Formats.HTML,
        config=pdoc_config
    )
    
    # Write output
    output_path = Path(output_dir) / module_name.replace(".", "/")
    output_path.mkdir(parents=True, exist_ok=True)
    
    for page_name, page_html in html.items():
        page_path = output_path / f"{page_name}.html"
        page_path.write_text(page_html)
        print(f"Generated: {page_path}")
    
    return True

if __name__ == "__main__":
    import sys
    module = sys.argv[1] if len(sys.argv) > 1 else "mypackage"
    generate_docs(module)
```

```bash
# Command-line usage
pdoc --html --output-dir docs mypackage
pdoc --http :8080 mypackage  # Serve live docs
```

### 2. Handle Import Errors Gracefully

Create stub modules for unavailable dependencies.

```python
# docs/stubs.py
import sys
from unittest.mock import MagicMock

# Mock unavailable dependencies
STUB_MODULES = [
    'torch', 'torch.nn', 'torch.optim',
    'tensorflow', 'tensorflow.keras',
    'numpy', 'pandas', 'scipy',
    'cv2', 'PIL', 'matplotlib',
]

for mod_name in STUB_MODULES:
    if mod_name not in sys.modules:
        sys.modules[mod_name] = MagicMock()

# Now import your module
import mypackage
```

```python
# docs/conf.py equivalent for pdoc
import os
import sys

# Add src to path
sys.path.insert(0, os.path.abspath('src'))

# Conditional import with error handling
def safe_import(module_name):
    try:
        return __import__(module_name)
    except ImportError:
        return None

# Check for required modules
required = ['requests', 'flask']
missing = [mod for mod in required if safe_import(mod) is None]

if missing:
    print(f"Warning: Missing modules for docs: {missing}")
```

### 3. Use pdoc with Type Annotations

Leverage type hints for better documentation.

```python
# mypackage/api.py
from typing import Optional, List, Dict, Any

def fetch_data(
    url: str,
    params: Optional[Dict[str, Any]] = None,
    timeout: int = 30
) -> List[Dict[str, Any]]:
    """Fetch data from an API endpoint.
    
    Args:
        url: The API endpoint URL
        params: Optional query parameters
        timeout: Request timeout in seconds
    
    Returns:
        List of data records from the API
    
    Raises:
        ConnectionError: If the API is unreachable
        TimeoutError: If the request times out
    
    Example:
        ```python
        data = fetch_data("https://api.example.com/data", {"page": 1})
        print(len(data))
        ```
    """
    pass

class DataProcessor:
    """Process and transform data records.
    
    Attributes:
        name: Name of the processor
        config: Configuration dictionary
    """
    
    def __init__(self, name: str, config: Optional[Dict] = None):
        self.name = name
        self.config = config or {}
    
    def process(self, data: List[Dict]) -> List[Dict]:
        """Process input data and return transformed results.
        
        Args:
            data: Input data records
        
        Returns:
            Transformed data records
        """
        pass
```

```bash
# Generate with type annotations visible
pdoc --html --show-source mypackage

# Serve with live reload
pdoc --http localhost:8080 mypackage
```

## Common Scenarios

### Scenario 1: Documenting CLI Applications

Handling modules with side effects:

```python
# mypackage/cli.py
"""CLI interface for mypackage."""
import sys
import argparse

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Command to execute")
    args = parser.parse_args()
    
    if args.command == "serve":
        start_server()
    elif args.command == "build":
        build_project()

# Guard against import-time execution
if __name__ == "__main__":
    main()
```

```python
# docs/generate.py
import sys
import importlib

# Temporarily override __name__ to prevent side effects
original_name = __name__
__name__ = "not_main"

try:
    # Import without triggering side effects
    module = importlib.import_module("mypackage.cli")
    
    # Generate documentation
    import pdoc
    html = pdoc.html(module)
    
finally:
    __name__ = original_name
```

### Scenario 2: Custom Documentation Templates

Extending pdoc with custom templates:

```python
# docs/custom.py
import pdoc
from pdoc.html_helpers import render_html

def custom_render(module, **kwargs):
    """Custom rendering with additional context."""
    context = {
        'project_name': 'MyPackage',
        'github_url': 'https://github.com/user/repo',
        'version': '1.0.0',
    }
    
    return render_html(module, **context)

# Use custom render function
pdoc.render = custom_render
```

## Prevent It

- Use `pdoc --http` during development for instant documentation preview
- Add `__all__` to modules to control public API surface
- Mock heavy dependencies before importing modules for documentation
- Use type annotations to generate better parameter documentation
- Run `pdoc` with `--show-source` to verify code examples in docstrings