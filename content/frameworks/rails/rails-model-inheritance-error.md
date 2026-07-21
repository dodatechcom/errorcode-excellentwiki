---
title: "[Solution] Rails Model Inheritance Error"
description: "STI inheritance not working."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

STI inheritance not working.

## Common Causes

Wrong column.

## How to Fix

Check type column.

## Example

```ruby
class Animal < ApplicationRecord; end
class Dog < Animal; end
# animals table needs 'type' column
```
