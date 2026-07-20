---
title: "[Solution] Python string Module Error — Template and Format Failures"
description: "Fix Python string module errors including Template substitution errors, format_map issues, Formatter problems, and string constants. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 249
---

# Python string Module Error — Template and Format Failures

The `string` module provides Template class for string substitution, the Formatter class for custom formatting, and useful string constants. Errors occur when template placeholders are missing, format specifications are invalid, or substitution values have incompatible types.

## Common Causes

```python
# Cause 1: Missing template substitution values
from string import Template

t = Template("Hello, $name! You have $count messages.")
result = t.substitute(name="Alice")  # KeyError: 'count'

# Cause 2: Invalid format specifications
text = "Value: {:.2f}".format("not_a_number")  # ValueError: Unknown format code 'f'

# Cause 3: Template with invalid delimiter
from string import Template

t = Template("Hello ${name}")  # TemplateSyntaxError: Invalid placeholder in string

# Cause 4: format_map with missing keys
text = "Hello {name}, you have {count} messages"
result = text.format_map({"name": "Alice"})  # KeyError: 'count'

# Cause 5: Unsafe substitution with user input
from string import Template

t = Template("Hello $user")
user_input = "$HOME"  # User input contains template syntax
result = t.safe_substitute(user=user_input)  # May not behave as expected
```

## How to Fix

### Fix 1: Use safe_substitute for partial substitution

```python
from string import Template

t = Template("Hello, $name! You have $count messages.")

# safe_substitute leaves unresolved placeholders as-is
result = t.safe_substitute(name="Alice")
print(result)  # Hello, Alice! You have $count messages.

# Full substitution
result = t.safe_substitute(name="Alice", count=5)
print(result)  # Hello, Alice! You have 5 messages.
```

### Fix 2: Handle format specification errors

```python
# Catch ValueError for bad format specs
try:
    result = "{:.2f}".format("text")
except ValueError as e:
    print(f"Format error: {e}")
    result = str("text")

# Use conditional formatting
value = "hello"
if isinstance(value, (int, float)):
    result = f"{value:.2f}"
else:
    result = str(value)

print(result)
```

### Fix 3: Use string.Template for safe user templates

```python
from string import Template

def render_template(template_str, **kwargs):
    try:
        t = Template(template_str)
        return t.safe_substitute(**kwargs)
    except (ValueError, KeyError) as e:
        print(f"Template error: {e}")
        return template_str

# Safe against user input containing template syntax
user_template = "Hello $name, your balance is $amount"
result = render_template(user_template, name="Alice", amount=100)
print(result)  # Hello Alice, your balance is 100
```

### Fix 4: Use format_map with defaultdict

```python
from collections import defaultdict

class SafeFormatter(dict):
    def __missing__(self, key):
        return f"<{key}>"

text = "Hello {name}, you have {count} messages from {sender}"
result = text.format_map(SafeFormatter(name="Alice"))
print(result)  # Hello Alice, you have <count> messages from <sender>

# Alternative: use a default dict
defaults = defaultdict(lambda: "N/A", {"name": "Alice"})
result = text.format_map(defaults)
print(result)  # Hello Alice, you have N/A messages from N/A
```

### Fix 5: Handle special characters in templates

```python
from string import Template

# Use $$ to escape the delimiter
t = Template("Price: $$100 (tax: $tax)")
result = t.substitute(tax=20)
print(result)  # Price: $100 (tax: 20)

# Use iddelimiter for custom delimiters
t = Template("Hello %name%", iddelimiter="%")
result = t.substitute(name="World")
print(result)  # Hello World
```

## Examples

```python
# Real-world: Build SQL query safely (not for production — use parameterized queries)
from string import Template

def build_query(table, columns, where_clause):
    col_str = ", ".join(columns)
    t = Template("SELECT $columns FROM $table WHERE $where")
    return t.safe_substitute(
        columns=col_str,
        table=table,
        where=where_clause
    )

query = build_query("users", ["id", "name"], "active = 1")
print(query)  # SELECT id, name FROM users WHERE active = 1

# Real-world: Template-based email body
from string import Template

email_template = Template("""
Dear $customer_name,

Your order #$order_id has been confirmed.
Total: $$total_amount

Thank you for your purchase!
""")

body = email_template.substitute(
    customer_name="Alice Smith",
    order_id="12345",
    total_amount="99.99"
)
print(body)
```

## Related Errors

- [KeyError](/languages/python/keyerror/) — missing template variable
- [ValueError](/languages/python/valueerror/) — invalid format specification
- [TypeError](/languages/python/typeerror/) — incompatible type for formatting
