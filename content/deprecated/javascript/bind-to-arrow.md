---
title: "[Solution] Deprecated Function Migration: .bind(this) to arrow functions"
description: "Migrate from deprecated .bind(this) pattern to arrow functions for lexical this binding in JavaScript."
deprecated_function: ".bind(this)"
replacement_function: "arrow functions"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: .bind(this) to arrow functions

The `.bind(this)` has been deprecated in favor of `arrow functions`.

## Migration Guide

Arrow functions capture this from the surrounding scope (lexical binding), eliminating the need for .bind(this).

## Before (Deprecated)

```javascript
function Timer() {
    this.seconds = 0;
    setInterval(function() {
        this.seconds++;
        console.log(this.seconds);
    }.bind(this), 1000);
}
```

## After (Modern)

```javascript
class Timer {
    constructor() {
        this.seconds = 0;
        setInterval(() => {
            this.seconds++;
            console.log(this.seconds);
        }, 1000);
    }
}
```

## Key Differences

- Arrow functions inherit this from enclosing scope
- No need for .bind(this) or var self = this
- Cannot use as constructors (no new)
