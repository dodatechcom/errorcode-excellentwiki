---
title: "[Solution] Ruby URI — InvalidURIError, BadURIError, Parse Errors"
description: "Fix Ruby URI errors. Handle InvalidURIError, BadURIError, and URI.parse failures."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, uri, parse, invalid, bad_uri"]
severity: "error"
---

# Ruby URI Errors

## Error Message

```
URI::InvalidURIError: bad URI(is not URI?): ...
# or
URI::BadURIError: the URI is not RFC 2396 compliant: ...
```

## Common Causes

- Parsing URIs with invalid characters (spaces, special chars, unicode)
- Missing scheme (http/https) in URI strings
- Using URI.parse instead of URI.join for relative paths
- Passing URIs with encoded vs decoded characters inconsistently

## Solutions

### Solution 1: Validate and Encode URIs Before Parsing

Encode special characters before calling `URI.parse`.

```ruby
require "uri"

# BAD: spaces in URI
URI.parse("https://example.com/path with spaces")  # InvalidURIError

# GOOD: encode first
uri = URI.encode_www_form_component("path with spaces")
URI.parse("https://example.com/#{uri}")
# => #<URI::HTTPS https://example.com/path+with+spaces>

# Or use URI.open with encoded URL
URI.open(URI.encode("https://example.com/path with spaces"))
```

### Solution 2: Handle Missing Schemes

Ensure URIs have a valid scheme before parsing.

```ruby
require "uri"

# BAD: no scheme
URI.parse("example.com/path")  # InvalidURIError

# GOOD: add scheme if missing
def normalize_uri(str)
  str = "https://#{str}" unless str.match?(%r{\Ahttps?://})
  URI.parse(str)
end

normalize_uri("example.com/path")  # => #<URI::HTTPS https://example.com/path>
normalize_uri("https://example.com/path")  # => #<URI::HTTPS https://example.com/path>
```

### Solution 3: Build URIs with URI.join for Relative Paths

Use `URI.join` to resolve relative paths against a base URI.

```ruby
require "uri"

base = URI("https://example.com/api/v1/")

# BAD: string concatenation
URI.parse("https://example.com/api/v1/" + "users")  # works but fragile

# GOOD: use URI.join
URI.join(base, "users")  # => #<URI::HTTPS https://example.com/api/v1/users>
URI.join(base, "/users")  # => #<URI::HTTPS https://example.com/users>

# Handle trailing slashes
URI.join("https://example.com/api", "v1", "users")
# => #<URI::HTTPS https://example.com/api/v1/users>
```

### Solution 4: Parse and Extract URI Components Safely

Extract and modify URI components without re-parsing.

```ruby
require "uri"

uri = URI("https://user:pass@example.com:8080/path?q=1#frag")

uri.scheme    # => "https"
uri.host      # => "example.com"
uri.port      # => 8080
uri.path      # => "/path"
uri.query     # => "q=1"
uri.fragment  # => "frag"
uri.user      # => "user"
uri.password  # => "pass"

# Modify and rebuild
new_uri = uri.dup
new_uri.port = 443
new_uri.query = "q=2&sort=name"
new_uri.to_s  # => "https://user:pass@example.com:443/path?q=2&sort=name#frag"
```

## Prevention Tips

- Use `URI.encode_www_form_component` for special characters in URI components
- Always provide a scheme (`http://` or `https://`) before parsing
- Use `URI.join` for combining base URIs with relative paths
- Test URIs from user input with `URI.parse` in a rescue block

## Related Errors

- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
- [Ruby Net::HTTP Error]({{< relref "/languages/ruby/ruby-net-http-error" >}})
- [Ruby OpenURI Error]({{< relref "/languages/ruby/ruby-open-uri-error" >}})
