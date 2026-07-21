---
title: "[Solution] Deprecated Function Migration: underscore convention to WeakMap/#private"
description: "Migrate from deprecated underscore _private convention to WeakMap or #private fields."
deprecated_function: "_private convention"
replacement_function: "#private or WeakMap"
languages: ["javascript"]
deprecated_since: "ES6/2015+/ES2022"
---

# [Solution] Deprecated Function Migration: underscore convention to WeakMap/#private

The `_private convention` has been deprecated in favor of `#private or WeakMap`.

## Migration Guide

The _underscore convention is only a naming convention. #private fields provide actual privacy.

## Before (Deprecated)

```javascript
function User(name, password) {
    this._name = name;
    this._password = password;
}
User.prototype.validate = function(pw) {
    return this._password === pw;
};
```

## After (Modern)

```javascript
class User {
    #name;
    #password;
    constructor(name, password) {
        this.#name = name;
        this.#password = password;
    }
    validate(pw) {
        return this.#password === pw;
    }
}
```

## Key Differences

- #private is the modern standard (ES2022)
- _underscore is only a convention
- Private fields cannot be accessed outside
