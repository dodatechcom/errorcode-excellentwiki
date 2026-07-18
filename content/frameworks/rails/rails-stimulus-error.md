---
title: "[Solution] Rails Stimulus Error — How to Fix"
description: "Fix Rails Stimulus errors. Resolve controller registration issues, JavaScript import problems, and Stimulus configuration errors."
frameworks: ["rails"]
error-types: ["javascript-error"]
severities: ["error"]
weight: 5
comments: true
---

A Rails Stimulus error occurs when Stimulus controllers fail to register, initialize, or interact with the DOM.

## Why It Happens

Stimulus errors happen due to incorrect controller registration, missing imports, DOM element mismatches, or JavaScript build issues.

## Common Error Messages

```
ReferenceError: Stimulus is not defined
```

```
TypeError: controllerClass is not a constructor
```

```
Error: Stimulus controller 'hello' not registered
```

```
SyntaxError: unexpected token '<'
```

## How to Fix It

### 1. Register Stimulus Controllers

Ensure proper registration.

```javascript
import { application } from './application'
import HelloController from './hello_controller'

application.register('hello', HelloController)

// Or auto-import
eagerLoadControllersFrom('controllers', application)
```

### 2. Define Stimulus Controllers

Create controllers with proper structure.

```javascript
import { Controller } from '@hotwired/stimulus'

export default class extends Controller {
  static targets = ['output', 'input']
  static values = { name: String }

  connect() {
    console.log('Hello controller connected')
  }

  greet() {
    this.outputTarget.textContent = `Hello, ${this.nameValue}!`
  }
}
```

### 3. Use Correct HTML Attributes

Connect controllers to elements.

```erb
<div data-controller="hello">
  <input data-action="input->hello#greet" data-hello-target="input">
  <p data-hello-target="output"></p>
</div>

<div data-controller="hello" data-hello-name-value="World">
  <button data-action="click->hello#greet">Greet</button>
</div>
```

### 4. Configure Import Maps

Set up for Rails 7.

```ruby
# config/importmap.rb
pin 'application'
pin '@hotwired/stimulus', to: 'stimulus.min.js'
pin '@hotwired/stimulus-loading', to: 'stimulus-loading.js'
pin_all_from 'app/javascript/controllers', under: 'controllers'
```

## Common Scenarios

**Scenario 1: Controller not connecting.**
Check data-controller matches registered name.

**Scenario 2: Import fails with unexpected token.**
Don't use `import` with import maps.

**Scenario 3: Controller method not found.**
Verify data-action matches method name.

## Prevent It

1. **Use Stimulus generator.**
Run `rails generate stimulus name`.

2. **Test in browser console.**
Use `application.getControllerForElementAndIdentifier()`.

3. **Keep controllers small.**
One controller per concern.

