---
title: "[Solution] Python Rich Error — Console, Table Rendering & Syntax Highlighting"
description: "Fix Python Rich library errors by resolving console issues, table rendering failures, and syntax highlighting problems. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 413
---

# Python Rich Error — Console, Table Rendering & Syntax Highlighting

Rich errors occur when console output fails due to encoding issues, tables have mismatched column counts, panels receive invalid dimensions, or syntax highlighting fails due to missing language definitions.

## Common Causes

```python
from rich.console import Console

# 1. Console output to closed stream
import sys
console = Console(file=sys.stdout)
sys.stdout.close()
console.print("Hello")  # ValueError or OSError
```

```python
# 2. Table with mismatched column count
from rich.table import Table
table = Table()
table.add_column("Name")
table.add_row("Alice", "extra")  # ValueError: wrong number of columns
```

```python
# 3. Panel with invalid width
from rich.panel import Panel
console = Console(width=-1)  # ValueError: width must be positive
```

```python
# 4. Syntax highlight for unknown language
from rich.syntax import Syntax
syntax = Syntax("code", "nonexistent_language")  # may raise error
```

```python
# 5. Markup parsing error
from rich.console import Console
console = Console()
console.print("[bold]unterminated tag")  # markup error
```

## How to Fix

### Fix 1: Create console with safe defaults

```python
from rich.console import Console
import sys

# Safe console creation
console = Console(
    file=sys.stdout,
    force_terminal=False,
    color_system="auto",
    width=min(120, 80),
)

console.print("Hello, [bold green]World[/bold green]!")
```

### Fix 2: Match row data to column count

```python
from rich.table import Table

table = Table(title="Users")
table.add_column("Name", style="cyan")
table.add_column("Age", style="magenta")

# Ensure each row has exactly as many values as columns
rows = [
    ("Alice", 30),
    ("Bob", 25),
]
for name, age in rows:
    table.add_row(name, str(age))

console = Console()
console.print(table)
```

### Fix 3: Set valid panel dimensions

```python
from rich.panel import Panel
from rich.console import Console

console = Console()

# Use auto-width or explicit positive width
panel = Panel(
    "This is the panel content with some text to display.",
    title="Info",
    border_style="blue",
    width=60,  # explicit positive width
)
console.print(panel)
```

### Fix 4: Use supported languages for syntax highlighting

```python
from rich.syntax import Syntax
from rich.console import Console

code = '''
def greet(name):
    return f"Hello, {name}!"
'''

# Use supported language names
syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console = Console()
console.print(syntax)
```

### Fix 5: Escape markup in user strings

```python
from rich.console import Console

console = Console()

user_input = "[bold]this is not markup"
# Escape rich markup to prevent parsing errors
from rich.text import Text
text = Text(user_input)
console.print(text)

# Or use escape function
from rich.markup import escape
console.print(escape("[bold]this renders as plain text"))
```

## Examples

```python
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax

console = Console()

# Build a complete formatted output
table = Table(title="Server Status", show_header=True, header_style="bold magenta")
table.add_column("Server", style="cyan", width=12)
table.add_column("Status", justify="center")
table.add_column("Load", justify="right")

servers = [
    ("web-01", "[green]UP[/green]", "0.45"),
    ("db-01", "[green]UP[/green]", "1.23"),
    ("cache-01", "[red]DOWN[/red]", "N/A"),
]

for name, status, load in servers:
    table.add_row(name, status, load)

console.print(Panel(table, title="Infrastructure Dashboard", border_style="green"))
```

## Related Errors

- [ValueError](/languages/python/valueerror/) — invalid parameter
- [OSError](/languages/python/oserror/) — file/stream error
- [KeyError](/languages/python/keyerror/) — missing style or theme
