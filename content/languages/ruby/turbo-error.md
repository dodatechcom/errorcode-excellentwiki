---
title: "[Solution] Ruby Turbo Navigation Error Fix"
description: "Fix Turbo navigation errors in Rails. Learn why Turbo Drive and Turbo Frames fail and how to handle navigation issues."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Turbo navigation error occurs when Turbo Drive or Turbo Frames cannot process a navigation request. Turbo provides SPA-like navigation without writing much JavaScript, but errors can arise from incompatible responses or missing configuration.

## Common Causes

- Response not compatible with Turbo
- Missing Turbo frame ID
- Redirect issues
- JavaScript response in Turbo frame

## How to Fix

```ruby
# WRONG: Rendering JavaScript response in Turbo frame
# Turbo expects HTML, not JS

# CORRECT: Use Turbo frame-compatible responses
respond_to do |format|
  format.turbo_stream do
    render turbo_stream: turbo_stream.replace("frame", partial: "content")
  end
  format.html { render :show }
end
```

```html
<!-- WRONG: Missing Turbo frame target -->
<turbo-frame id="frame1">
  <a href="/other">Link</a>  <!-- Navigates whole page -->
</turbo-frame>

<!-- CORRECT: Add data-turbo-frame -->
<turbo-frame id="frame1">
  <a href="/other" data-turbo-frame="frame1">Link</a>  <!-- Navigates frame -->
</turbo-frame>
```

```ruby
# WRONG: Redirect not compatible with Turbo
redirect_to root_path  # May cause Turbo error

# CORRECT: Use Turbo-compatible redirect
redirect_to root_path, status: :see_other
```

## Examples

```html
<!-- Example 1: Turbo frame -->
<turbo-frame id="modal">
  <h1>Modal Content</h1>
</turbo-frame>

<!-- Example 2: Turbo stream -->
<turbo-stream action="replace" target="modal">
  <template>
    <div id="modal">Updated content</div>
  </template>
</turbo-stream>
```

```ruby
# Example 3: Turbo stream response
turbo_stream.replace("list", partial: "list", locals: { items: @items })
```

## Related Errors

- [Hotwire error](hotwire-error) — Hotwire integration error
- [Stimulus controller error](stimulus-error) — Stimulus controller failed
- [ActionView::MissingTemplate](rails-template) — template not found
