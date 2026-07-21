---
title: "[Solution] Laravel Mail Template Error"
description: "Mailable template not rendering."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Mailable template not rendering.

## Common Causes

Wrong view.

## How to Fix

Create mailable view.

## Example

```php
public function build() { return $this->view('emails.welcome'); }
```
