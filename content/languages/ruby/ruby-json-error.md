---
title: "[Solution] Ruby JSON — Parse Error, NaN/Infinity, Generate Failures"
description: "Fix Ruby JSON errors. Handle parse errors, NaN/Infinity values, and JSON.generate failures."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, json, parse, serialization, infinity"]
severity: "error"
---

# Ruby JSON Errors

## Error Message

```
JSON::ParserError: 795: unexpected token at '...'
# or
JSON::GeneratorError: NaN not allowed for JSON
# or
JSON::GeneratorError: Infinity not allowed for JSON
```

## Common Causes

- Malformed JSON strings from user input or APIs
- NaN or Infinity float values from Math operations
- Encoding issues with non-ASCII characters in JSON
- Deeply nested structures causing parser errors

## Solutions

### Solution 1: Handle NaN and Infinity in Floats

Sanitize float values before JSON serialization.

```ruby
require "json"

# BAD: NaN and Infinity not valid JSON
value = 0.0 / 0.0  # => NaN
JSON.dump({ value: value })  # JSON::GeneratorError

value = Float::INFINITY
JSON.dump({ value: value })  # JSON::GeneratorError

# GOOD: sanitize before serialization
def sanitize(value)
  case value
  when Float
    value.finite? ? value : nil
  when Hash
    value.transform_values { |v| sanitize(v) }
  when Array
    value.map { |v| sanitize(v) }
  else
    value
  end
end

JSON.dump(sanitize({ val: Float::INFINITY }))
# => '{"val":null}'
```

### Solution 2: Parse JSON Safely with Error Handling

Use `parse` with rescue and validate input before parsing.

```ruby
require "json"

def safe_json_parse(str)
  JSON.parse(str)
rescue JSON::ParserError => e
  puts "Invalid JSON: #{e.message}"
  nil
end

safe_json_parse('{"valid": true}')  # => {"valid"=>true}
safe_json_parse('not json')         # => nil (prints error)

# Or use load with defaults
JSON.parse('{"name": "alice"}', { symbolize_names: true })
# => {name: "alice"}
```

### Solution 3: Handle Encoding in JSON

Ensure strings are properly encoded before JSON serialization.

```ruby
require "json"

# BAD: binary data
data = { content: "\xFF".force_encoding("ASCII-8BIT") }
JSON.dump(data)  # may raise encoding error

# GOOD: encode to UTF-8 first
data = { content: "\xFF".force_encoding("UTF-8").encode("UTF-8", invalid: :replace, undef: :replace) }
JSON.dump(data)

# Or use JSON.generate with options
JSON.generate({ key: "value" }, space: " ", space_before: ": ")
# => "{ : \"value\"}"
```

### Solution 4: Use Pretty Printing and Pretty Generate

Format JSON for debugging and output.

```ruby
require "json"

data = { users: [{ name: "alice", age: 30 }, { name: "bob", age: 25 }] }

# Pretty print
puts JSON.pretty_generate(data)
# {
#   "users": [
#     { "name": "alice", "age": 30 },
#     { "name": "bob", "age": 25 }
#   ]
# }

# Parse and re-generate
parsed = JSON.parse(JSON.dump(data))
JSON.pretty_generate(parsed)
```

## Prevention Tips

- Always rescue `JSON::ParserError` when parsing external data
- Sanitize float values — replace NaN/Infinity with nil before serialization
- Ensure strings are UTF-8 encoded before JSON operations
- Use `JSON.pretty_generate` for debugging, `JSON.dump` for compact output

## Related Errors

- [Ruby YAML Error]({{< relref "/languages/ruby/ruby-yaml-error" >}})
- [Encoding::UndefinedConversionError]({{< relref "/languages/ruby/ruby-encoding-error" >}})
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
