---
title: "[Solution] TypeScript Decorator Metadata Error — Experimental Decorators Fix"
description: "Fix TypeScript decorator metadata errors. Enable experimental decorators, configure emitDecoratorMetadata, and fix decorator type issues."
languages: ["typescript"]
severities: ["error"]
error-types: ["type-error"]
weight: 5
---

# TypeScript: Decorator metadata error

Decorator metadata errors occur when TypeScript's decorator support is not properly configured, when decorators are used without enabling `experimentalDecorators`, or when `emitDecoratorMetadata` is needed for runtime type reflection. These errors are common in frameworks like NestJS, TypeORM, and Angular that rely heavily on decorators.

## Common Causes

- **`experimentalDecorators` not enabled** — decorators require this compiler option
- **`emitDecoratorMetadata` not enabled** — needed for runtime type information in decorators
- **Decorator type mismatch** — using a class decorator on a method or vice versa
- **Decorators used in a non-decorator context** — using `@` syntax without decorator support

## How to Fix

```json
// Fix 1: Enable decorators in tsconfig.json
{
  "compilerOptions": {
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true
  }
}
```

```typescript
// Fix 2: Correct decorator types
function Logger(target: any, propertyKey?: string, descriptor?: PropertyDescriptor) {
  if (propertyKey === undefined) {
    // Class decorator
    console.log(`Class ${target.name} created`);
  } else if (descriptor) {
    // Method decorator
    const original = descriptor.value;
    descriptor.value = function (...args: any[]) {
      console.log(`Calling ${propertyKey} with`, args);
      return original.apply(this, args);
    };
  } else {
    // Property decorator
    console.log(`Property ${propertyKey} decorated`);
  }
}

@Logger
class UserService {
  @Logger
  name: string = "Alice";

  @Logger
  getUser(id: number) {
    return { id, name: this.name };
  }
}
```

```typescript
// Fix 3: Use correct decorator signature for each context
// Class decorator
function sealed(constructor: Function) {
  Object.seal(constructor);
  Object.seal(constructor.prototype);
}

// Method decorator
function log(target: any, key: string, descriptor: PropertyDescriptor) {
  const original = descriptor.value;
  descriptor.value = function (...args: any[]) {
    console.log(`Method ${key} called`);
    return original.apply(this, args);
  };
}

// Property decorator
function validate(target: any, key: string) {
  let value: any;
  const getter = () => value;
  const setter = (newVal: any) => {
    if (typeof newVal !== "string") {
      throw new TypeError(`Property ${key} must be a string`);
    }
    value = newVal;
  };
  Object.defineProperty(target, key, {
    get: getter,
    set: setter,
  });
}
```

## Examples

```typescript
// Example 1: NestJS-style decorator (requires emitDecoratorMetadata)
import { Injectable } from "@nestjs/common";

@Injectable()
class CatsService {
  findAll(): string[] {
    return ["Tabby", "Persian"];
  }
}

// Example 2: TypeORM entity decorator
import { Entity, PrimaryGeneratedColumn, Column } from "typeorm";

@Entity()
class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  name: string;
}

// Example 3: Custom parameter decorator
function Body(key: string) {
  return (target: any, propertyKey: string | symbol, parameterIndex: number) => {
    const existingMetadata = Reflect.getMetadata("body", target, propertyKey) || {};
    existingMetadata[parameterIndex] = key;
    Reflect.defineMetadata("body", existingMetadata, target, propertyKey);
  };
}
```

## Related Errors

- [TS1219: Experimental decorators are not enabled]({{< relref "/languages/typescript/decorator-error" >}}) — missing experimentalDecorators
- [TS2688: Cannot find type definition file]({{< relref "/languages/typescript/ts2688" >}}) — missing reflect-metadata types
- [TS2345: Argument type not assignable]({{< relref "/languages/typescript/ts2345" >}}) — decorator function type mismatch
