---
title: "[Solution] Ruby Rack — Middleware, Status/Header/Body, config.ru Errors"
description: "Fix Ruby Rack errors. Handle middleware issues, response format, halt, and config.ru configuration errors."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, rack, middleware, config_ru, http"]
severity: "error"
---

# Ruby Rack Errors

## Error Message

```
RuntimeError: missing required keys from Hash
# or
Rack::Lint::LintError: response is not an Array
# or
Rack::Utils::HeaderHash is not compatible with ...
```

## Common Causes

- Middleware not calling `@app.call(env)` to pass requests down the stack
- Returning invalid Rack response format (not [status, headers, body])
- Using deprecated Rack APIs or HeaderHash
- Missing `config.ru` for Rack-based applications

## Solutions

### Solution 1: Create Correct Rack Responses

Always return a 3-element array: `[status, headers, body]`.

```ruby
class MyMiddleware
  def initialize(app)
    @app = app
  end

  def call(env)
    status, headers, body = @app.call(env)

    # Add custom header
    headers["X-Custom"] = "value"

    [status, headers, body]
  end
end
```

### Solution 2: Use halt for Early Returns

Use `Rack::Response` or `halt` for short-circuiting the middleware stack.

```ruby
require "rack"

class AuthMiddleware
  def initialize(app)
    @app = app
  end

  def call(env)
    # Check authentication
    unless env["HTTP_AUTHORIZATION"]
      return [401, { "content-type" => "text/plain" }, ["Unauthorized"]]
    end

    @app.call(env)
  end
end
```

### Solution 3: Create a Proper config.ru

Set up Rack applications correctly in config.ru.

```ruby
# config.ru
require "rack"

app = Rack::Builder.new do
  use MyMiddleware
  run lambda { |env|
    [200, { "content-type" => "text/plain" }, ["Hello World"]]
  }
end

run app
```

### Solution 4: Use Rack::Builder for Middleware Stacking

Stack middleware in the correct order using `use` and `run`.

```ruby
# config.ru
require "rack"

use Rack::CommonLogger
use Rack::ShowExceptions
use Rack::Static, urls: ["/public"], root: "public"

run lambda { |env|
  [200, { "content-type" => "text/html" }, ["<h1>Hello</h1>"]]
}
```

## Prevention Tips

- Always return `[status, headers, body]` — body must respond to `each`
- Call `@app.call(env)` in middleware to pass requests to the next layer
- Use `Rack::Response` for convenient response building
- Test middleware with `Rack::MockRequest`

## Related Errors

- [Rails Rack Error]({{< relref "/languages/ruby/rails-rack-error" >}})
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
- [RuntimeError]({{< relref "/languages/ruby/runtime-error" >}})
