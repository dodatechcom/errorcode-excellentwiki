---
title: "[Solution] Rails Content Security Policy Error"
description: "Fix Rails Content Security Policy violation errors. Resolve CSP blocked script or style inline errors in Rails."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when the browser blocks inline scripts, styles, or external resources due to a strict Content Security Policy configured in Rails.

## Common Causes

- Rails 6+ ships with a default CSP that blocks inline scripts
- Turbolinks or Turbo requires specific CSP exceptions
- Inline `style=` attributes on HTML elements are blocked
- External CDN resources (fonts, analytics) not whitelisted
- `nonce` not provided for legitimate inline scripts

## How to Fix

1. Configure CSP in `config/initializers/content_security_policy.rb`:

```ruby
Rails.application.config.content_security_policy do |policy|
  policy.default_src :self
  policy.script_src  :self, :https, :unsafe_inline
  policy.style_src   :self, :https, :unsafe_inline
  policy.img_src     :self, :https, :data
  policy.font_src    :self, :https
  policy.connect_src :self, :https
end
```

2. Use nonces for inline scripts instead of `unsafe_inline`:

```ruby
policy.script_src  :self, :https, nonce: true
```

```html
<script nonce="<%= content_security_policy_nonce %>">
  // inline script allowed via nonce
</script>
```

3. Whitelist specific external domains:

```ruby
policy.script_src :self, 'https://cdn.example.com'
policy.style_src  :self, 'https://fonts.googleapis.com'
policy.font_src   :self, 'https://fonts.gstatic.com'
```

4. Disable CSP in development:

```ruby
# config/environments/development.rb
config.content_security_policy = nil
```

## Examples

```html
<!-- Inline script blocked by CSP -->
<script>
  alert('hello');
</script>
<!-- Refused to execute inline script because it violates the following Content Security Policy directive -->

<!-- Inline style blocked -->
<div style="color: red;">Error</div>
<!-- Refused to apply inline style because it violates Content Security Policy -->
```
