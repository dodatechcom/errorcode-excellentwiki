---
title: "[Solution] Ruby Encoding::UndefinedConversionError Fix"
description: "Fix Encoding::UndefinedConversionError from ASCII-8BIT to UTF-8 in Ruby. Learn why encoding mismatches occur and how to handle them."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, encoding, utf-8, ascii"]
severity: "error"
---

# Encoding::UndefinedConversionError

## Error Message

```
Encoding::UndefinedConversionError: "\xFF" from ASCII-8BIT to UTF-8
```

## Common Causes

- Reading binary data and treating it as UTF-8 text
- Mixing strings with different encodings in operations
- Database returning data with unexpected encoding
- File read without specifying encoding, defaulting to ASCII-8BIT

## Solutions

### Solution 1: Force or Set Correct Encoding on Strings

Use force_encoding to reinterpret bytes or encode to transcode between encodings.

```ruby
# WRONG: Binary data read as ASCII-8BIT
data = File.read("image.png")  # encoding: ASCII-8BIT
puts data.force_encoding("UTF-8")  # UndefinedConversionError

# CORRECT: Use force_encoding for binary data
data = File.read("image.png", mode: "rb")
data.force_encoding("UTF-8")

# CORRECT: Transcode if actual text content
data = File.read("data.csv", encoding: "ISO-8859-1")
data.encode!("UTF-8", invalid: :replace, undef: :replace)
```

### Solution 2: Set Default Encoding for Your Application

Configure the default source and external encoding for the entire Ruby process.

```ruby
# config/initializers/encoding.rb
# Set default encoding to UTF-8
Encoding.default_external = Encoding::UTF_8
Encoding.default_internal = Encoding::UTF_8

# Or set via environment variable
# RUBYOPT=-Eutf-8

# Verify current encoding
puts Encoding.default_external  # => #<Encoding:UTF-8>
```

### Solution 3: Handle Encoding in Database Operations

Ensure database connections and queries use consistent encoding to prevent conversion errors.

```ruby
# Check database encoding
ActiveRecord::Base.connection.execute(
  "SELECT pg_encoding_to_char(encoding) FROM pg_database WHERE datname = current_database()"
)

# Set encoding in database.yml
production:
  adapter: postgresql
  encoding: utf8
  url: <%= ENV['DATABASE_URL'] %>

# In migration, ensure column is UTF-8
class AddName < ActiveRecord::Migration[7.0]
  def change
    add_column :users, :name, :string, null: false
  end
end
```

### Solution 4: Safely Handle Mixed Encoding Strings

When combining strings from different sources, normalize encoding before operations.

```ruby
# WRONG: Mixing encodings
utf8_str = "hello"        # UTF-8
ascii_str = "world".force_encoding("ASCII-8BIT")
utf8_str + ascii_str  # Encoding::CompatibilityError

# CORRECT: Normalize before combining
utf8_str = "hello"
ascii_str = "world".force_encoding("UTF-8").encode("UTF-8")
utf8_str + ascii_str  # => "helloworld"

# Or use encode with replacements
result = utf8_str.encode("UTF-8",
  invalid: :replace,
  undef: :replace,
  replace: "?"
)
```

## Prevention Tips

- Always specify encoding when reading files: File.read(path, encoding: 'UTF-8')
- Set Encoding.default_external = Encoding::UTF-8 in an initializer
- Use force_encoding to reinterpret bytes, encode to transcode between encodings
- Test with strings containing non-ASCII characters (accented letters, CJK characters)

## Related Errors

- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
- [RuntimeError]({{< relref "/languages/ruby/runtime-error" >}})
- [IOError]({{< relref "/languages/ruby/io-error" >}})
