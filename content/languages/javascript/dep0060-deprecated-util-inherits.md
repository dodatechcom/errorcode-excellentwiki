---
title: "[Solution] DEP0060 — Deprecation Warning: util.inherits() Fix"
description: "Fix DEP0060 warning for deprecated util.inherits(). Migrate to ES6 classes with extends."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# DEP0060 — util.inherits() is Deprecated

Replace `util.inherits()` with ES6 class inheritance.

## Before (deprecated)

```javascript
const util = require('util');

function Animal(name) {
  this.name = name;
}

function Dog(name) {
  Animal.call(this, name);
}
util.inherits(Dog, Animal);
```

## After

```javascript
class Animal {
  constructor(name) { this.name = name; }
}

class Dog extends Animal {
  constructor(name) { super(name); }
}
```
