---
title: "[Solution] Ruby Nokogiri XML Parse Error Fix"
description: "Fix Nokogiri XML parsing errors. Learn why XML parsing fails and how to handle malformed XML properly."
languages: ["ruby"]
severities: ["error"]
error-types: ["parse-error"]
weight: 5
---

## What This Error Means

A Nokogiri XML parse error occurs when Nokogiri cannot parse the provided XML content due to malformed XML, encoding issues, or invalid document structure.

## Common Causes

- Malformed XML (unclosed tags, mismatched tags)
- Invalid characters in XML
- Encoding mismatch
- Namespace issues

## How to Fix

```ruby
# WRONG: Parsing malformed XML
xml = "<root><item>hello</root>"  # Unclosed tag
doc = Nokogiri::XML(xml)  # XML::SyntaxError

# CORRECT: Ensure valid XML
xml = "<root><item>hello</item></root>"
doc = Nokogiri::XML(xml)
```

```ruby
# WRONG: Not handling encoding
xml = "\xFF\xFE<hello>"  # Invalid UTF-8
doc = Nokogiri::XML(xml)

# CORRECT: Fix encoding
xml = "<hello>".encode("UTF-8", invalid: :replace, undef: :replace)
doc = Nokogiri::XML(xml)
```

```ruby
# WRONG: Strict parsing of imperfect XML
doc = Nokogiri::XML(xml) { |config| config.strict }

# CORRECT: Lenient parsing
doc = Nokogiri::XML(xml) do |config|
  config.noerror  # Suppress errors
end
```

## Examples

```ruby
# Example 1: Parse with error handling
begin
  doc = Nokogiri::XML(xml_content)
rescue Nokogiri::XML::SyntaxError => e
  puts "Parse error: #{e.message}"
end

# Example 2: Parse HTML (more lenient)
doc = Nokogiri::HTML(html_content)

# Example 3: Validate XML
errors = Nokogiri::XML(xml_content).errors
puts errors unless errors.empty?
```

## Related Errors

- [Nokogiri XPath error](nokogiri-xpath-error) — XPath query failed
- [LoadError](loaderror-ruby) — cannot load such file
- [Encoding error](encoding-error) — encoding issues
