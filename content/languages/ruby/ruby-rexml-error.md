---
title: "[Solution] Ruby REXML — Document Parse, XPath, and Malformed XML Errors"
description: "Fix Ruby REXML errors. Handle parse failures, XPath errors, and malformed XML documents."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, rexml, xml, xpath, parse"]
severity: "error"
---

# Ruby REXML Errors

## Error Message

```
REXML::ParseException: no < element (line N, column N)
# or
REXML::ParseException: malformed XML
# or
REXML::XPathUndefined: XPath unknown:
```

## Common Causes

- Malformed XML (unclosed tags, special characters not escaped)
- Invalid XPath expressions
- Parsing untrusted XML without entity expansion protection
- Namespaces not handled in XPath queries

## Solutions

### Solution 1: Parse XML Safely with REXML

Use `REXML::Document` with proper error handling.

```ruby
require "rexml/document"

xml_str = <<~XML
  <users>
    <user>
      <name>Alice</name>
      <email>alice@example.com</email>
    </user>
  </users>
XML

doc = REXML::Document.new(xml_str)
names = REXML::XPath.match(doc, "//user/name").map(&:text)
# => ["Alice"]
```

### Solution 2: Handle Parse Errors Gracefully

Rescue `REXML::ParseException` for malformed XML input.

```ruby
require "rexml/document"

def safe_parse(xml_str)
  REXML::Document.new(xml_str)
rescue REXML::ParseException => e
  puts "Parse error at line #{e.line}: #{e.message}"
  nil
end

safe_parse("<root><unclosed>")  # => nil (prints error)
safe_parse("<root><closed/></root>")  # => document
```

### Solution 3: Use XPath with Namespaces

Handle XML namespaces properly in XPath queries.

```ruby
require "rexml/document"

xml = <<~XML
  <feed xmlns="http://www.w3.org/2005/Atom">
    <entry>
      <title>First Post</title>
    </entry>
  </feed>
XML

doc = REXML::Document.new(xml)

# With namespace
names = REXML::XPath.match(
  doc,
  "//xmlns:entry/xmlns:title",
  { "xmlns" => "http://www.w3.org/2005/Atom" }
).map(&:text)

# Or without namespace prefix
REXML::XPath.match(doc, "//*[local-name()='entry']//*[local-name()='title']")
```

### Solution 4: Prevent Billion Laughs Attack

Disable entity expansion when parsing untrusted XML.

```ruby
require "rexml/document"
require "rexml/security"

# Disable entity expansion (Billion Laughs protection)
REXML::Security.entity_expansion_limit = 0

# Or parse with disabled DTDs
doc = REXML::Document.new(untrusted_xml_str)

# For even more safety, use Nokogiri with noent: false
# Nokogiri::XML(xml_str) { |config| config.noent.nodtd }
```

## Prevention Tips

- Always rescue `REXML::ParseException` when parsing external XML
- Disable entity expansion when processing untrusted XML documents
- Use `REXML::XPath.match` instead of `first` for multiple results
- Test XML parsing with malformed and malicious input

## Related Errors

- [Nokogiri Error]({{< relref "/languages/ruby/nokogiri-error" >}})
- [SyntaxError]({{< relref "/languages/ruby/syntax-error" >}})
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
