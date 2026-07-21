---
title: "[Solution] Deprecated Function Migration: prototype-based inheritance to ES6 classes"
description: "Migrate from deprecated prototype-based inheritance to ES6 class syntax in JavaScript."
deprecated_function: "prototype-based inheritance"
replacement_function: "ES6 class syntax"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: prototype-based inheritance to ES6 classes

The `prototype-based inheritance` has been deprecated in favor of `ES6 class syntax`.

## Migration Guide

ES6 class syntax provides a cleaner way to define constructors and inheritance compared to prototype manipulation.

## Before (Deprecated)

```javascript
function Animal(name) {
    this.name = name;
}
Animal.prototype.speak = function() {
    return this.name + " makes a noise.";
};

function Dog(name) {
    Animal.call(this, name);
}
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;
```

## After (Modern)

```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        return `${this.name} makes a noise.`;
    }
}

class Dog extends Animal {
    speak() {
        return `${this.name} barks.`;
    }
}
```

## Key Differences

- Use class keyword for constructors
- Use extends for inheritance
- Use super() to call parent methods
