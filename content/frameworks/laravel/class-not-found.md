---
title: "Class 'X' not found"
description: "Laravel (via PHP) throws this error when the autoloader cannot locate the specified class during runtime."
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when PHP's autoloader (managed by Composer) cannot find the class file for the class you are referencing. It is common after adding new classes, changing namespaces, or forgetting to run `composer dump-autoload`.

## Common Causes

- The class was recently created or renamed but `composer dump-autoload` was not run
- The class namespace does not match the directory structure
- The class is in a package that has not been required via Composer
- Typo in the class name

## How to Fix

Regenerate the Composer autoload map:

```bash
composer dump-autoload
```

Verify the namespace matches the PSR-4 mapping in `composer.json`:

```json
{
  "autoload": {
    "psr-4": {
      "App\\": "app/"
    }
  }
}
```

```php
// app/Services/PaymentService.php
namespace App\Services;

class PaymentService
{
    // namespace must match App\Services to be autoloaded from app/Services/
}
```

## Example

```php
// routes/web.php
Route::get("/pay", function () {
    $service = new App\Services\Payment(); // class Payment does not exist, should be PaymentService
});
```

```text
Error: Class 'App\Services\Payment' not found
```

## Related Errors

- [Method X does not exist on instance]({{< relref "/frameworks/laravel/method-not-found" >}})
