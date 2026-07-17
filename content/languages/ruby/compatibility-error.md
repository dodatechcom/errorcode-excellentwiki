---
title: "[Solution] Ruby Encoding::CompatibilityError — Encoding Compatibility Fix"
description: "Fix Ruby Encoding::CompatibilityError. Handle incompatible string encodings in concatenation and operations."
languages: ["ruby"]
severities: ["error"]
error_types: ["encoding"]
weight: 150
---

# Encoding::CompatibilityError — Encoding Compatibility Fix

An `Encoding::CompatibilityError` is raised when an operation combines strings with incompatible encodings that cannot be automatically converted.

## Description

Ruby automatically encodes strings when possible, but some encoding combinations are incompatible. For example, combining a UTF-8 string with an ASCII-8BIT (binary) string containing bytes > 127 raises this error.

Common scenarios:

- **UTF-8 + binary data** — mixing text and binary strings.
- **ASCII + non-ASCII** — ASCII string with bytes that aren't valid in the target encoding.
- **Different multibyte encodings** — UTF-8 + Shift_JIS in same operation.
- **Regexp with wrong encoding** — regex pattern with incompatible encoding.

## Common Causes

```ruby
# Cause 1: Mixing UTF-8 and binary
utf8 = "hello"
binary = "\xFF\xFE".force_encoding('ASCII-8BIT')
utf8 + binary  # CompatibilityError

# Cause 2: ASCII string with invalid bytes
ascii = "hello".force_encoding('ASCII')
binary = "\x80\x81\x82".force_encoding('ASCII-8BIT')
ascii << binary  # CompatibilityError

# Cause 3: Incompatible regex match
str = "hello".force_encoding('UTF-8')
pat = "pattern".force_encoding('ASCII-8BIT')
str.match(pat)  # CompatibilityError

# Cause 4: Different multibyte encodings
utf8 = "héllo".force_encoding('UTF-8')
shift_jis = "こんにちは".force_encoding('Shift_JIS')
utf8 + shift_jis  # CompatibilityError
```

## Solutions

### Fix 1: Normalize encodings before combining

```ruby
# Wrong
utf8 = "hello"
binary = "\xFF\xFE".force_encoding('ASCII-8BIT')
result = utf8 + binary  # CompatibilityError

# Correct — encode both to the same encoding
utf8 = "hello"
binary = "\xFF\xFE".force_encoding('ASCII-8BIT')
result = utf8.encode('ASCII-8BIT') + binary
```

### Fix 2: Set encoding explicitly when reading

```ruby
# Wrong
data = File.read('file.txt')  # May have wrong encoding

# Correct
data = File.read('file.txt', encoding: 'UTF-8')
data.force_encoding('UTF-8') if data.encoding == Encoding::ASCII_8BIT
```

### Fix 3: Use encoding-aware string operations

```ruby
# Wrong — incompatible concatenation
str1 = "hello".force_encoding('UTF-8')
str2 = "\x80".force_encoding('ASCII-8BIT')
str1 + str2  # CompatibilityError

# Correct — encode to compatible encoding
str1 = "hello".force_encoding('UTF-8')
str2 = "\x80".force_encoding('ASCII-8BIT')
result = str1.encode('ASCII-8BIT') + str2
```

### Fix 4: Use String#b to create binary copy

```ruby
# String#b creates a binary copy
str = "hello"
binary_str = str.b  # Same content, ASCII-8BIT encoding

# Safe to combine with other binary data
other_binary = "\xFF".force_encoding('ASCII-8BIT')
result = str.b + other_binary  # Works
```

## Related Errors

- [Encoding::InvalidByteSequenceError](encoding-error) — invalid bytes in encoding.
- [ArgumentError](argument-error) — wrong encoding argument.
- [IOError](io-error) — stream closed or invalid I/O.
