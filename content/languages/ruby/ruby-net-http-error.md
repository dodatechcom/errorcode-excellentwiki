---
title: "[Solution] Ruby Net::HTTP — Timeout, SSL, Redirect, and Response Errors"
description: "Fix Ruby Net::HTTP errors. Handle timeouts, SSL errors, redirects, and HTTP 4xx/5xx responses."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, net-http, timeout, ssl, http"]
severity: "error"
---

# Ruby Net::HTTP Errors

## Error Message

```
Net::OpenTimeout: execution expired
# or
Net::ReadTimeout: execution expired
# or
OpenSSL::SSL::SSLError: certificate verify failed
# or
Net::HTTPRedirection: 301 Moved Permanently
```

## Common Causes

- No timeout set, causing requests to hang indefinitely
- SSL certificates not found or expired
- Redirects not followed automatically by Net::HTTP
- Server returning 4xx/5xx without checking response code

## Solutions

### Solution 1: Set Timeouts on HTTP Requests

Always set `open_timeout` and `read_timeout` to prevent hanging.

```ruby
require "net/http"
require "uri"

uri = URI("https://api.example.com/data")
http = Net::HTTP.new(uri.host, uri.port)
http.use_ssl = true

# Set timeouts (in seconds)
http.open_timeout = 5
http.read_timeout = 10

begin
  response = http.get(uri.request_uri)
  puts response.body
rescue Net::OpenTimeout => e
  puts "Connection timed out: #{e.message}"
rescue Net::ReadTimeout => e
  puts "Read timed out: #{e.message}"
end
```

### Solution 2: Handle SSL Certificate Verification

Configure SSL properly for HTTPS requests.

```ruby
require "net/http"
require "uri"
require "openssl"

uri = URI("https://secure.example.com")
http = Net::HTTP.new(uri.host, uri.port)
http.use_ssl = true

# Option 1: Use system certificates (preferred)
http.cert_store = OpenSSL::X509::Store.new
http.cert_store.set_default_paths

# Option 2: Verify SSL (default, preferred)
http.verify_mode = OpenSSL::SSL::VERIFY_PEER

# Option 3: Skip verification (insecure, for testing only)
# http.verify_mode = OpenSSL::SSL::VERIFY_NONE

response = http.get(uri.request_uri)
```

### Solution 3: Follow Redirects Manually

Net::HTTP does not auto-follow redirects; handle 3xx responses yourself.

```ruby
require "net/http"
require "uri"

def fetch(url, limit = 10)
  raise "Too many redirects" if limit == 0

  uri = URI(url)
  response = Net::HTTP.get_response(uri)

  case response
  when Net::HTTPRedirection
    location = response["location"]
    fetch(location, limit - 1)
  when Net::HTTPSuccess
    response
  else
    raise "HTTP #{response.code}: #{response.message}"
  end
end

response = fetch("https://example.com/old-page")
```

### Solution 4: Handle 4xx and 5xx Responses

Check response codes before accessing the body.

```ruby
require "net/http"
require "uri"

uri = URI("https://api.example.com/data")
response = Net::HTTP.get_response(uri)

case response
when Net::HTTPSuccess
  JSON.parse(response.body)
when Net::HTTPClientError
  puts "Client error #{response.code}: #{response.message}"
when Net::HTTPServerError
  puts "Server error #{response.code}: retry later"
else
  puts "Unexpected response: #{response.code}"
end
```

## Prevention Tips

- Always set `open_timeout` and `read_timeout` (5-10 seconds)
- Follow redirects manually — Net::HTTP does not handle them automatically
- Use `Net::HTTP.get_response` to check status codes before accessing the body
- Prefer the `http` gem or `open-uri` for simpler HTTP requests

## Related Errors

- [Timeout::Error]({{< relref "/languages/ruby/timeout-error" >}})
- [OpenSSL::SSL::SSLError]({{< relref "/languages/ruby/ruby-net-http-error" >}})
- [Errno::ECONNREFUSED]({{< relref "/languages/ruby/connection-refused" >}})
