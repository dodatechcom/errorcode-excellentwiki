---
title: "[Solution] Ruby OpenURI — Read Timeout, Redirect, Content Type Errors"
description: "Fix Ruby OpenURI errors. Handle read timeouts, redirects, content type mismatches, and SSL errors."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, open-uri, http, timeout, redirect"]
severity: "error"
---

# Ruby OpenURI Errors

## Error Message

```
OpenURI::HTTPError: 404 Not Found
# or
Timeout::Error: execution expired
# or
OpenURI::HTTPError: 301 Moved Permanently
```

## Common Causes

- No timeout set for HTTP requests using open-uri
- Content type mismatch (expecting HTML, getting binary data)
- Redirect responses not handled properly
- SSL certificate verification failures

## Solutions

### Solution 1: Set Timeouts on open-uri Requests

Use `open_timeout` and `read_timeout` options to prevent hanging.

```ruby
require "open-uri"

# Set timeouts (in seconds)
uri = URI("https://example.com/data")
data = URI.open(uri, open_timeout: 5, read_timeout: 10).read
puts data
```

### Solution 2: Handle HTTP Errors and Redirects

Use `open` with proper error handling for non-200 responses.

```ruby
require "open-uri"

begin
  data = URI.open("https://example.com/page").read
rescue OpenURI::HTTPError => e
  puts "HTTP Error: #{e.message}"
  # e.io contains the response object
  puts e.io.status  # => ["404", "Not Found"]
end
```

### Solution 3: Handle Content Type Mismatch

Check the content type before processing the response.

```ruby
require "open-uri"

response = URI.open("https://example.com/data")

# Check content type
content_type = response.content_type
puts content_type  # => "text/html"

case content_type
when "text/html"
  html = response.read
  process_html(html)
when "application/json"
  json = response.read
  process_json(json)
else
  raise "Unexpected content type: #{content_type}"
end
```

### Solution 4: Use open-uri with Custom Headers

Pass custom headers with open-uri using a Hash of options.

```ruby
require "open-uri"

# Custom headers
options = {
  "User-Agent" => "MyApp/1.0",
  "Accept" => "application/json",
  open_timeout: 5,
  read_timeout: 10
}

data = URI.open("https://api.example.com/data", options).read
parsed = JSON.parse(data)
```

## Prevention Tips

- Always set timeouts on open-uri requests
- Check `content_type` before assuming the response format
- Use `rescue OpenURI::HTTPError` to handle non-200 status codes
- Consider using Net::HTTP or the http gem for more control

## Related Errors

- [Timeout::Error]({{< relref "/languages/ruby/timeout-error" >}})
- [OpenSSL::SSL::SSLError]({{< relref "/languages/ruby/ruby-net-http-error" >}})
- [Errno::ECONNREFUSED]({{< relref "/languages/ruby/connection-refused" >}})
