---
title: "[Solution] Python BeautifulSoup Error — Parsing and Navigation Failures"
description: "Fix Python BeautifulSoup errors like FeatureNotFound, parser errors, tag navigation, and encoding issues. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 421
---

# Python BeautifulSoup Error — Parsing and Navigation Failures

BeautifulSoup errors occur when the library cannot find a parser, encounters malformed HTML, or fails during tag navigation and encoding conversion. These are common in web scraping workflows.

## Common Causes

```python
# FeatureNotFound: No parser found for the given markup
from bs4 import BeautifulSoup
soup = BeautifulSoup("<html></html>", "html5lib")

# AttributeError when navigating tags
from bs4 import BeautifulSoup
soup = BeautifulSoup("<div><p>Hello</p></div>", "html.parser")
result = soup.find("div").find("span").text  # span doesn't exist

# UnicodeEncodeError during output
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>café</p>", "html.parser")
encoded = soup.encode("ascii")  # can't encode 'é'

#_PARSER_PRESENT but version mismatch
from bs4 import BeautifulSoup
soup = BeautifulSoup("<html></html>", "lxml-xml")

# TypeError on invalid markup input
from bs4 import BeautifulSoup
soup = BeautifulSoup(12345, "html.parser")
```

## How to Fix

### Fix 1: Install the Correct Parser
Ensure you have the parser library installed alongside BeautifulSoup.
```bash
pip install beautifulsoup4 lxml
```
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup("<html></html>", "lxml")
```

### Fix 2: Handle None Results from Tag Navigation
Always check if a tag exists before accessing its attributes.
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup("<div><p>Hello</p></div>", "html.parser")
div = soup.find("div")
if div:
    p = div.find("p")
    if p:
        print(p.text)
```

### Fix 3: Use Correct Encoding for Output
Specify an encoding that supports the characters in your document.
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>café</p>", "html.parser")
encoded = soup.encode("utf-8")
```

### Fix 4: Pass a String to BeautifulSoup
Ensure the input to BeautifulSoup is a string, not an integer or other type.
```python
from bs4 import BeautifulSoup
html_content = str(12345)
soup = BeautifulSoup(html_content, "html.parser")
```

### Fix 5: Use `html.parser` as Fallback
If lxml or other parsers aren't installed, use the built-in parser.
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup("<html></html>", "html.parser")
```

## Examples

```python
# Extracting all links safely
from bs4 import BeautifulSoup
html = '<a href="https://example.com">Link</a><a href="https://test.com">Test</a>'
soup = BeautifulSoup(html, "html.parser")
links = [a["href"] for a in soup.find_all("a") if a.get("href")]

# Parsing tables
html = '<table><tr><td>Cell 1</td><td>Cell 2</td></tr></table>'
soup = BeautifulSoup(html, "html.parser")
rows = [[td.text for td in tr.find_all("td")] for tr in soup.find_all("tr")]
```

## Related Errors

- [Python requests Error](/languages/python/python-requests-error/)
- [Python httpx Error](/languages/python/python-httpx-error/)
- [Python Scrapy Error](/languages/python/python-scrapy-error/)
