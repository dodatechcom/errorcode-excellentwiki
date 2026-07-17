---
title: "[Solution] Ruby Nokogiri XPath Error Fix"
description: "Fix Nokogiri XPath errors. Learn why XPath queries fail and how to write correct XPath expressions."
languages: ["ruby"]
severities: ["error"]
error-types: ["query-error"]
tags: ["nokogiri", "xpath", "query", "ruby"]
weight: 5
---

## What This Error Means

A Nokogiri XPath error occurs when an XPath query is invalid or the expression doesn't match any nodes in the document. This can happen due to syntax errors in the XPath or wrong namespace handling.

## Common Causes

- Invalid XPath syntax
- Wrong namespace prefix
- No nodes matching the query
- Special characters in XPath not escaped

## How to Fix

```ruby
# WRONG: Invalid XPath syntax
doc.xpath("//div[@class='hello")  # Missing closing bracket

# CORRECT: Valid XPath
doc.xpath("//div[@class='hello']")
```

```ruby
# WRONG: Wrong namespace
doc.xpath("//div")  # May not find nodes with namespaces

# CORRECT: Use namespace
doc.xpath("//xmlns:div", "xmlns" => "http://www.w3.org/1999/xhtml")
```

```ruby
# WRONG: Empty result not handled
title = doc.xpath("//h1").first.text  # NoMethodError if nil

# CORRECT: Check for nil
title = doc.xpath("//h1")&.first&.text || "No title"
```

## Examples

```ruby
# Example 1: Basic XPath
doc = Nokogiri::HTML("<html><body><h1>Hello</h1></body></html>")
doc.xpath("//h1").text  # "Hello"

# Example 2: CSS vs XPath
doc.at_css("h1")  # Simpler for basic selectors
doc.at_xpath("//h1")  # More powerful

# Example 3: Complex XPath
doc.xpath("//div[@class='content']//a[@href]")
```

## Related Errors

- [Nokogiri XML parse error](nokogiri-error) — XML parsing failed
- [Mechanize connection error](mechanize-error) — HTTP request failed
- [LoadError](loaderror-ruby) — cannot load such file
