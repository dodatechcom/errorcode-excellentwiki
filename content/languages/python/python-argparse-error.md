---
title: "[Solution] Python Argparse Error — Command-Line Argument Parsing Issues"
description: "Fix Python argparse errors by handling required arguments, type conversion, choice validation, and mutually exclusive groups. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 203
---

# Python Argparse Error — Command-Line Argument Parsing Issues

Argparse errors occur when command-line arguments are missing, have invalid types, fail validation, or conflict with each other. These errors typically surface when scripts are run from the command line with incorrect arguments.

## Common Causes

```python
# Missing required argument
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", required=True)
args = parser.parse_args([])  # error: the following arguments are required: --name
```

```python
# Type conversion failure
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--count", type=int)
args = parser.parse_args(["--count", "abc"])  # error: argument --count: invalid int value: 'abc'
```

```python
# Invalid choice value
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--mode", choices=["fast", "slow", "medium"])
args = parser.parse_args(["--mode", "turbo"])  # error: argument --mode: invalid choice: 'turbo'
```

```python
# Mutually exclusive arguments both provided
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("--input", type=str)
group.add_argument("--output", type=str)
args = parser.parse_args(["--input", "file.txt", "--output", "out.txt"])
# error: argument --output: not allowed with argument --input
```

```python
# Unrecognized argument
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args(["--verbose", "--unknown"])
# error: unrecognized arguments: --unknown
```

## How to Fix

### Fix 1: Provide all required arguments or set defaults

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", required=True, help="Your name")
parser.add_argument("--age", type=int, default=25, help="Your age (default: 25)")
args = parser.parse_args(["--name", "Alice"])

print(f"Name: {args.name}, Age: {args.age}")
```

### Fix 2: Use custom type functions with error handling

```python
import argparse

def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
    return ivalue

parser = argparse.ArgumentParser()
parser.add_argument("--count", type=positive_int)
parser.add_argument("--path", type=str)

args = parser.parse_args(["--count", "5"])
print(f"Count: {args.count}")
```

### Fix 3: Provide helpful error messages for choices

```python
import argparse

parser = argparse.ArgumentParser(description="Process data with a specific mode")
parser.add_argument(
    "--mode",
    choices=["fast", "slow", "medium"],
    default="medium",
    help="Processing mode (default: medium)"
)
parser.add_argument(
    "--input",
    required=True,
    help="Input file path"
)

args = parser.parse_args(["--input", "data.csv"])
print(f"Mode: {args.mode}, Input: {args.input}")
```

### Fix 4: Handle mutually exclusive groups with optional defaults

```python
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("--input", type=str, help="Input file path")
group.add_argument("--stdin", action="store_true", help="Read from stdin")

args = parser.parse_args([])
if args.stdin:
    print("Reading from stdin")
elif args.input:
    print(f"Reading from {args.input}")
else:
    print("No input specified, using default")
```

### Fix 5: Use subcommands for complex argument structures

```python
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

# Add subcommand
add_parser = subparsers.add_parser("add", help="Add an item")
add_parser.add_argument("name", type=str)
add_parser.add_argument("--quantity", type=int, default=1)

# Remove subcommand
remove_parser = subparsers.add_parser("remove", help="Remove an item")
remove_parser.add_argument("name", type=str)
remove_parser.add_argument("--force", action="store_true")

args = parser.parse_args(["add", "apple", "--quantity", "3"])
if args.command == "add":
    print(f"Adding {args.quantity} of {args.name}")
```

## Examples

### Complete argument parser with validation

```python
import argparse
import os

def validate_file(parser, arg):
    if not os.path.exists(arg):
        parser.error(f"The file {arg} does not exist")
    return arg

parser = argparse.ArgumentParser(
    description="Process files and generate reports",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""
examples:
  %(prog)s input.csv --output report.html
  %(prog)s input.csv --format json --verbose
"""
)

parser.add_argument("input", help="Input file path")
parser.add_argument("-o", "--output", default="report.html", help="Output file")
parser.add_argument("-f", "--format", choices=["html", "json", "csv"], default="html")
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("--max-rows", type=int, default=1000, metavar="N")

args = parser.parse_args(["input.csv", "-o", "result.html", "-v"])
print(f"Processing {args.input} -> {args.output} ({args.format})")
```

### Parsing with defaults from environment variables

```python
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--host", default=os.environ.get("APP_HOST", "localhost"))
parser.add_argument("--port", type=int, default=int(os.environ.get("APP_PORT", "8080")))
parser.add_argument("--debug", action="store_true", default=os.environ.get("APP_DEBUG", "false").lower() == "true")

args = parser.parse_args([])
print(f"Server: {args.host}:{args.port}, Debug: {args.debug}")
```

## Related Errors

- [SystemExit](/languages/python/systemexit/) — argparse calls sys.exit on parse errors
- [ValueError](/languages/python/valueerror/) — type conversion failures in arguments
- [TypeError](/languages/python/typeerror/) — incorrect argument types passed to argparse methods
