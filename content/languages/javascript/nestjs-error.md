---
title: "[Solution] JavaScript NestJS Runtime Error — How to Fix"
description: "Fix JavaScript NestJS module configuration, dependency injection, guard/interceptor, and pipe/filter errors."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 812
---

# JavaScript NestJS Runtime Error

An `NestError`, `TypeError`, or `InjectorError` occurs when NestJS's DI system cannot resolve providers, modules are misconfigured, guards/interceptors throw exceptions, or pipes/filters fail to transform or catch errors.

## Why It Happens

NestJS errors arise from missing `@Injectable()` decorators, providers not registered in the correct module, circular dependency injection, guard return values that are not booleans, and pipes that do not handle transformation errors.

## Common Error Messages

- `NestError: Cannot resolve dependencies of UserService`
- `Error: Circular dependency detected between modules`
- `TypeError: Guard must return a boolean or throw`
- `Error: Pipe must return a transformed value`
- `Error: Unknown module 'xxx' in imports`

## How to Fix It

### Fix 1: Register providers in modules

```typescript
import { Module } from '@nestjs/common'
import { UserService } from './user.service'
import { UserController } from './user.controller'

@Module({
  controllers: [UserController],
  // ❌ Wrong - service not provided
  // ✅ Correct
  providers: [UserService],
  exports: [UserService]
})
export class UserModule {}
```

### Fix 2: Use forwardRef for circular deps

```typescript
import { Module, forwardRef } from '@nestjs/common'

// ❌ Wrong - direct circular import
// @Module({ imports: [ModuleB] }) class ModuleA {}
// @Module({ imports: [ModuleA] }) class ModuleB {}

// ✅ Correct - use forwardRef
@Module({
  imports: [forwardRef(() => ModuleB)]
})
class ModuleA {}

@Module({
  imports: [forwardRef(() => ModuleA)]
})
class ModuleB {}
```

### Fix 3: Guard must return boolean

```typescript
import { Injectable, CanActivate, ExecutionContext } from '@nestjs/common'

@Injectable()
export class AuthGuard implements CanActivate {
  canActivate(context: ExecutionContext): boolean {
    const request = context.switchToHttp().getRequest()
    // ❌ Wrong - returning undefined/null
    // ✅ Correct
    return request.headers.authorization?.startsWith('Bearer ') ?? false
  }
}
```

### Fix 4: Validation pipe with class-validator

```typescript
import { IsString, IsEmail, IsOptional } from 'class-validator'

export class CreateUserDto {
  @IsEmail()
  email: string

  @IsString()
  // ❌ Wrong - missing decorator for optional field
  // ✅ Correct
  @IsOptional()
  name?: string
}

// main.ts - register pipe globally
import { ValidationPipe } from '@nestjs/common'
app.useGlobalPipes(new ValidationPipe({ whitelist: true }))
```

## Examples

Exception filter catching all HTTP errors:

```typescript
import { ExceptionFilter, Catch, ArgumentsHost, HttpException } from '@nestjs/common'
import { Response } from 'express'

@Catch(HttpException)
export class HttpExceptionFilter implements ExceptionFilter {
  catch(exception: HttpException, host: ArgumentsHost) {
    const ctx = host.switchToHttp()
    const response = ctx.getResponse<Response>()
    const status = exception.getStatus()

    response.status(status).json({
      statusCode: status,
      timestamp: new Date().toISOString(),
      message: exception.message
    })
  }
}
```

## Related Errors

- [Angular Error](/languages/javascript/angular-error)
- [JavaScript TypeError](/languages/javascript/typeerror)
- [JavaScript Express Error](/languages/javascript/express-middleware)
