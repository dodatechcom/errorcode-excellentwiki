---
title: "[Solution] Ruby Importmap::MissingStaticFileError Fix"
description: "Fix Importmap::MissingStaticFileError in Rails. Learn why import maps fail to find JavaScript modules and how to configure import maps."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

An `Importmap::MissingStaticFileError` is raised when the Rails import map cannot find a JavaScript module file. Import maps allow you to use JavaScript modules without a build step, but the files must exist in the expected location.

## Common Causes

- JavaScript file not in `app/javascript` directory
- Wrong module path in import map
- File not added to import map configuration
- Vendor module not installed

## How to Fix

```ruby
# WRONG: Module path not in import map
# config/importmap.rb missing pin

# CORRECT: Add pin to import map
# config/importmap.rb
pin "application", preload: true
pin "controllers/hello_controller", to: "controllers/hello_controller.js"
```

```javascript
// WRONG: Wrong import path
import { Controller } from "@hotwired/stimulus"  // Path not in import map

// CORRECT: Use pinned path
import { Controller } from "stimulus"
```

```ruby
# WRONG: File not in expected location
# app/javascript/controllers/hello_controller.js missing

# CORRECT: Create the file in the correct location
# app/javascript/controllers/hello_controller.js
import { Controller } from "@hotwired/stimulus"
export default class extends Controller {
  greet() { alert("Hello!") }
}
```

## Examples

```ruby
# Example 1: Pin a module
# config/importmap.rb
pin "controllers", to: "controllers"
pin "controllers/application", to: "controllers/application.js"

# Example 2: Pin from CDN
pin "lodash", to: "https://cdn.jsdelivr.net/npm/lodash@4/lodash.js"

# Example 3: Check import map
Rails.application.config.importmap
```

## Related Errors

- [Propshaft compilation error](propshaft-error) — asset compilation failed
- [Asset pipeline error](asset-pipeline-error) — Sprockets error
- [Stimulus controller error](stimulus-error) — Stimulus controller failed
