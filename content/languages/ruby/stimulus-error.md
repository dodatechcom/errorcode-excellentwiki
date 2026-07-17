---
title: "[Solution] Ruby Stimulus Controller Error Fix"
description: "Fix Stimulus controller errors in Ruby on Rails. Learn why Stimulus controllers fail and how to handle JavaScript integration errors."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["stimulus", "javascript", "controller", "rails", "ruby"]
weight: 5
---

## What This Error Means

A Stimulus controller error occurs when a Stimulus JavaScript controller fails to initialize or execute properly. Stimulus is a modest JavaScript framework for HTML, and errors can arise from missing targets, wrong actions, or initialization issues.

## Common Causes

- Missing data-controller attribute
- Target element not found in DOM
- Action method not defined
- Controller not imported

## How to Fix

```html
<!-- WRONG: Missing data-controller -->
<div>
  <button data-action="click->greet#greet">Click</button>
</div>

<!-- CORRECT: Add data-controller -->
<div data-controller="greet">
  <button data-action="click->greet#greet">Click</button>
</div>
```

```javascript
// WRONG: Target not found
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static targets = ["output"]

  greet() {
    this.outputTarget.textContent = "Hello"  // Target not in DOM
  }
}
```

```javascript
// CORRECT: Check target existence
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static targets = ["output"]

  greet() {
    if (this.hasOutputTarget) {
      this.outputTarget.textContent = "Hello"
    }
  }
}
```

## Examples

```html
<!-- Example 1: Basic Stimulus controller -->
<div data-controller="hello">
  <input data-hello-target="name" type="text">
  <button data-action="click->hello#greet">Greet</button>
  <span data-hello-target="output"></span>
</div>
```

```javascript
// Example 2: Stimulus controller
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static targets = ["name", "output"]

  greet() {
    const name = this.nameTarget.value
    this.outputTarget.textContent = `Hello, ${name}!`
  }
}
```

## Related Errors

- [Turbo navigation error](turbo-error) — Turbo navigation failed
- [Hotwire error](hotwire-error) — Hotwire integration error
- [Importmap error](importmap-error) — import map issue
