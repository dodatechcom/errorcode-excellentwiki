---
title: "[Solution] Python html Module Error — Parse, Escape, and Unescape Issues"
description: "Fix Python html module errors including HTMLParseError, html.escape, unescape, and character entity reference problems. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 243
---

# Python html Module Error — Parse, Escape, and Unescape Issues

The `html` module provides functions for escaping and unescaping HTML special characters, plus the `html.parser` module for parsing HTML and XHTML documents. Errors occur when handling malformed HTML, missing character entity references, or encoding issues.

## Common Causes

```python
# Cause 1: html.parser HTMLParseError in older Python versions
from html.parser import HTMLParser

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)

parser = MyParser()
# Malformed HTML causes issues in some edge cases
parser.feed("<div><p>unclosed paragraph</div>")  # May behave unexpectedly

# Cause 2: html.escape not handling all special characters
import html

# Double-encoding issues when escaping already-escaped text
escaped_once = html.escape("<script>alert('xss')</script>")
escaped_twice = html.escape(escaped_once)  # Now has &amp;lt; — double-escaped

# Cause 3: html.unescape with invalid entity references
import html

result = html.unescape("&invalid_entity;")  # Returns "&invalid_entity;" — no error raised
result = html.unescape("&#999999;")  # Returns "&#999999;" — numeric entity out of range

# Cause 4: Character entity references not recognized
import html

# Some named entities are not part of the HTML spec
html.unescape("&apos;")  # May not resolve on all Python versions
html.unescape("&apos;")  # Should resolve to apostrophe

# Cause 5: Encoding issues with non-ASCII in HTML
from html.parser import HTMLParser

parser = HTMLParser()
# Non-ASCII characters in attributes without proper encoding
parser.feed('<meta charset="utf-8"><div>Café résumé</div>')
```

## How to Fix

### Fix 1: Use html.escape with quote handling

```python
import html

# Default escaping — escapes <, >, &, and quotes
raw = '<div class="test">Hello & "World"</div>'
escaped = html.escape(raw)
print(escaped)  # &lt;div class=&quot;test&quot;&gt;Hello &amp; &quot;World&quot;&lt;/div&gt;

# Escape without quoting attribute values
escaped_no_quote = html.escape(raw, quote=False)
print(escaped_no_quote)  # &lt;div class="test"&gt;Hello &amp; "World"&lt;/div&gt;
```

### Fix 2: Avoid double-escaping

```python
import html

def safe_escape(text, already_escaped=False):
    if already_escaped:
        return text
    return html.escape(text)

# Correct usage — only escape once
user_input = '<script>alert("xss")</script>'
safe = html.escape(user_input)
# Pass already_escaped=True if the string was previously escaped
double_safe = safe_escape(safe, already_escaped=True)
```

### Fix 3: Use a robust HTML parser for complex documents

```python
from html.parser import HTMLParser
from html import unescape

class RobustHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.results = []

    def handle_starttag(self, tag, attrs):
        self.results.append(("start", tag, dict(attrs)))

    def handle_endtag(self, tag):
        self.results.append(("end", tag))

    def handle_data(self, data):
        self.results.append(("data", data))

    def handle_entityref(self, name):
        self.results.append(("entity", name, unescape(f"&{name};")))

    def handle_charref(self, name):
        self.results.append(("charref", name, unescape(f"&#{name};")))

    def error(self, message):
        print(f"Parser error: {message}")

parser = RobustHTMLParser()
parser.feed('<p>Hello &amp; <b>World</b> &#8212;</p>')
print(parser.results)
```

### Fix 4: Decode character entities manually

```python
import html

def decode_entities(text):
    # html.unescape handles most cases
    decoded = html.unescape(text)

    # Handle custom or extended entities
    custom_entities = {
        "&copy;": "\u00a9",
        "&reg;": "\u00ae",
        "&trade;": "\u2122",
        "&mdash;": "\u2014",
        "&ndash;": "\u2013",
    }
    for entity, char in custom_entities.items():
        decoded = decoded.replace(entity, char)

    return decoded

print(decode_entities("AT&amp;T &mdash; © 2024"))  # AT&T — © 2024
```

### Fix 5: Handle encoding declaration in HTML parsing

```python
from html.parser import HTMLParser

class EncodingAwareParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.encoding = None
        self.content = []

    def handle_starttag(self, tag, attrs):
        if tag == "meta":
            for attr, value in attrs:
                if attr == "charset":
                    self.encoding = value

    def handle_data(self, data):
        self.content.append(data)

    def get_text(self):
        return "".join(self.content)

parser = EncodingAwareParser()
parser.feed('<meta charset="utf-8"><div>Content here</div>')
print(parser.encoding)  # utf-8
print(parser.get_text())  # Content here
```

## Examples

```python
# Real-world: Sanitize user-submitted HTML
import html
import re

def sanitize_html(user_input):
    # Escape all HTML special characters
    escaped = html.escape(user_input)
    # Remove any remaining script-like patterns
    escaped = re.sub(r"<script.*?</script>", "", escaped, flags=re.IGNORECASE)
    return escaped

# Real-world: Extract text and entities from HTML
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_parts = []

    def handle_data(self, data):
        self.text_parts.append(data)

    def handle_entityref(self, name):
        from html import unescape
        self.text_parts.append(unescape(f"&{name};"))

    def handle_charref(self, name):
        from html import unescape
        self.text_parts.append(unescape(f"&#{name};"))

    def get_text(self):
        return " ".join(self.text_parts)

parser = TextExtractor()
parser.feed("<p>Hello &amp; welcome to the &ldquo;site&rdquo; &#8212; enjoy!</p>")
print(parser.get_text())  # Hello & welcome to the "site" — enjoy!
```

## Related Errors

- [UnicodeDecodeError](/languages/python/unicodedecodeerror/) — encoding issues with HTML content
- [AttributeError](/languages/python/attributeerror/) — calling methods on None from missing elements
- [TypeError](/languages/python/typeerror/) — passing wrong types to escape/unescape
