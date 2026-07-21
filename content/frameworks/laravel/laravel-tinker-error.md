---
title: "[Solution] Laravel Tinker Shell Error"
description: "Fix Laravel Tinker PsySH runtime errors. Resolve Tinker not working or throwing exceptions in Laravel."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when `php artisan tinker` fails to start or throws runtime exceptions while interacting with the REPL.

## Common Causes

- PsySH dependency is missing or outdated
- PHP version incompatible with the installed PsySH version
- Tinker tries to autoload a class with syntax errors
- Xdebug or other debugger interferes with the REPL loop
- Memory limit too low for large object inspection

## How to Fix

1. Update Tinker and its dependencies:

```bash
composer update laravel/tinker --with-all-dependencies
```

2. Increase PHP memory limit for Tinker:

```bash
php -d memory_limit=512M artisan tinker
```

3. Disable Xdebug when using Tinker:

```bash
# Use phpdbg instead
phpdbg -qrr artisan tinker
# Or disable xdebug in php.ini
```

4. Use `dd()` or `dump()` instead for quick debugging:

```php
$user = User::first();
dd($user->toArray());
// or
dump($user->email);
```

## Examples

```php
// Tinker session with Xdebug hangs
$ php artisan tinker
>>> $users = User::all();
// (hangs indefinitely)

// Fix by disabling Xdebug
$ Xdebug.mode=off php artisan tinker

// Memory exhausted inspecting large collection
>>> $all = User::all();
// PHP Fatal error: Allowed memory size exhausted
>>> $all = User::take(100)->get(); // use limit
```
