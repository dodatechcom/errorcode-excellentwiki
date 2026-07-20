---
title: "[Solution] Ruby ERB — Template Syntax, Undefined Method, Safe Level Errors"
description: "Fix Ruby ERB errors. Handle template syntax issues, undefined methods in templates, and safe level restrictions."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, erb, template, safe_level, output"]
severity: "error"
---

# Ruby ERB Errors

## Error Message

```
NameError: undefined local variable or method `...' for #<Binding:...>
# or
SyntaxError: (erb): unexpected ...
# or
SecurityError: Insecure level set in $SAFE
```

## Common Causes

- Referencing undefined variables or methods in ERB templates
- Using `$SAFE` level (deprecated in Ruby 3.1+)
- Incorrect ERB tag syntax (`<% %>` vs `<%= %>`)
- Passing wrong binding to `result` method

## Solutions

### Solution 1: Pass Correct Binding to ERB Templates

Use the right binding to make instance variables available in templates.

```ruby
require "erb"

class WelcomeController
  def index
    @name = "Alice"
    template = ERB.new(File.read("welcome.html.erb"))
    template.result(binding)  # uses this binding with @name
  end
end

# Or create a custom binding with specific variables
class TemplateRenderer
  def initialize(name, items)
    @name = name
    @items = items
  end

  def render(template_str)
    ERB.new(template_str).result(binding)
  end
end

renderer = TemplateRenderer.new("Alice", [1, 2, 3])
renderer.render("Hello <%= @name %>, items: <%= @items.join(', ') %>")
```

### Solution 2: Handle ERB Syntax Correctly

Understand the difference between `<% %>` (execute) and `<%= %>` (output).

```erb
<%# This is a comment - no output %>
<%# This executes code but produces no output %>
<% items.each do |item| %>
  <%# This outputs the item %>
  <%= item %>
<% end %>

<%# Use <%== for raw output (unescaped) %>
<%== "<b>Bold text</b>" %>
```

### Solution 3: Set ERB Trim Mode for Clean Output

Use trim mode to avoid extra newlines in output.

```ruby
require "erb"

# Default: leaves newlines after tags
ERB.new("<% if true %>\nhello\n<% end %>").result
# => "\nhello\n\n"

# Trim mode: removes trailing newlines after %>-
template = ERB.new("<% if true -%>\nhello\n<% end -%>", trim_mode: "-")
template.result  # => "hello\n"

# Or use trim_mode: "nodiscard" to keep comments
ERB.new("<%# comment %>", trim_mode: "nodiscard").result  # => ""
```

### Solution 4: Use ERB Safe Level Safely

Avoid `$SAFE` (deprecated) and use ERB's `safe_level` parameter instead.

```ruby
require "erb"

# Ruby 3.1+: $SAFE is deprecated
# Use ERB.new with safe_level instead
template = ERB.new("Hello", safe_level: 1)
template.result

# Or better: validate input before rendering
def safe_render(template_str, context)
  sanitized = template_str.gsub(/<%=.*?%>/) do |match|
    # validate ERB expressions here
    match
  end
  ERB.new(sanitized).result(context)
end
```

## Prevention Tips

- Always use `<%= %>` for output, `<% %>` for control flow
- Pass `binding` explicitly to `result` for variable access
- Test ERB templates with both valid and invalid inputs
- Avoid `$SAFE` — validate and sanitize inputs at the application level

## Related Errors

- [NameError]({{< relref "/languages/ruby/name-error" >}})
- [SyntaxError]({{< relref "/languages/ruby/syntax-error" >}})
- [SecurityError]({{< relref "/languages/ruby/permission-denied" >}})
