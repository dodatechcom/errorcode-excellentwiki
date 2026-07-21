---
title: "[Solution] Rails HTML Safe XSS Error"
description: "Fix Rails unsafe link_to or raw XSS vulnerability. Resolve Rails::Html::SafeBuffer and XSS safety errors."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["warning"]
---

This error or warning occurs when Rails detects that user-generated content may be rendered as raw HTML, potentially creating an XSS vulnerability.

## Common Causes

- Using `raw()` or `html_safe` on user input
- `link_to` with user-provided URLs that contain `javascript:` schemes
- Erb template bypasses `sanitize` for untrusted content
- Helper methods return unescaped HTML unintentionally
- `content_tag` receives unsanitized string arguments

## How to Fix

1. Never use `raw()` on user input:

```erb
<!-- BAD: renders user input as HTML -->
<%= raw @comment.body %>

<!-- GOOD: escapes by default -->
<%= @comment.body %>
```

2. Sanitize user content:

```ruby
sanitize(@comment.body, tags: %w[b i em strong p a], attributes: %w[href])
```

3. Use `link_to` safely with validated URLs:

```ruby
# Validate URL scheme before linking
def safe_link_to(url, text)
  uri = URI.parse(url)
  if %w[http https].include?(uri.scheme)
    link_to text, url, target: '_blank', rel: 'noopener'
  end
end
```

4. Mark content as safe only after sanitization:

```ruby
content = sanitize(user_input, tags: %w[p br b i])
content.html_safe  # safe after sanitization
```

## Examples

```erb
<!-- XSS vulnerability -->
<%= link_to "Click here", params[:url] %>
<!-- if params[:url] = "javascript:alert('xss')" -->

<!-- Fix: validate the URL -->
<% if params[:url].start_with?('http') %>
  <%= link_to "Click here", params[:url] %>
<% end %>
```
