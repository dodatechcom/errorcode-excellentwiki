---
title: "[Solution] Composer Dependency Conflict Error"
description: "Fix Composer dependency conflict. Use --with-all-dependencies, check version constraints, use composer why."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1109
---

# Composer Dependency Conflict Error

Composer dependency conflicts occur when two or more packages require incompatible versions of the same dependency. Composer cannot resolve a version that satisfies all constraints simultaneously, resulting in a conflict error.

## Common Causes

```bash
# Cause 1: Conflicting version constraints
composer require vendor/package-a:^2.0  # requires symfony/console ^5.0
composer require vendor/package-b:^3.0  # requires symfony/console ^6.0

# Cause 2: Root package constraint too restrictive
{
    "require": {
        "phpunit/phpunit": "^9.0",
        "php": ">=8.2"  # PHPUnit 9 needs PHP <8.2
    }
}

# Cause 3: Outdated lock file
# composer.lock doesn't match composer.json constraints

# Cause 4: Package dropped support for required version
# You need php ^8.1 but a package only supports php ^7.4|^8.0
```

## How to Fix

### Fix 1: Use --with-all-dependencies to update transitive dependencies

```bash
# Update all related packages together
composer update vendor/package-a --with-dependencies

# Or update everything
composer update

# This allows Composer to upgrade/downgrade other packages to resolve conflicts
```

### Fix 2: Analyze the conflict with composer why

```bash
# See why a specific package is required
composer why vendor/package-name

# Show all packages that require a specific package
composer why-not vendor/package-name:^3.0

# Show the dependency tree
composer why --tree vendor/package-name
```

### Fix 3: Adjust version constraints

```php
// Check your composer.json constraints
{
    "require": {
        "php": ">=8.1",
        "symfony/framework-bundle": "^6.0|^7.0",
        "doctrine/orm": "^2.14|^3.0"
    }
}

// Allow wider version ranges
{
    "require": {
        "symfony/console": "^5.4 || ^6.0 || ^7.0"
    }
}
```

### Fix 4: Remove and reinstall to force fresh resolution

```bash
# Remove lock file and vendor directory
rm -rf vendor/ composer.lock

# Fresh install
composer install

# If still failing, try with verbose output
composer install -vvv
```

### Fix 5: Use composer-provided tools for complex conflicts

```bash
# Check platform requirements
composer show --platform

# Show why a package was installed
composer show --installed vendor/package-name

# Check for abandoned packages
composer show --available vendor/package-name | grep abandoned

# Use inline aliases for conflicting packages (last resort)
{
    "repositories": [
        { "type": "vcs", "url": "https://github.com/vendor/forked-package" }
    ],
    "require": {
        "vendor/forked-package": "dev-main as 2.0.0"
    }
}
```

## Examples

```bash
# Real-world conflict resolution workflow

# Step 1: Identify the conflict
composer update
# Output: Your requirements could not be resolved...
# Problem 1: package-a requires symfony/console ^5.0
# Problem 2: package-b requires symfony/console ^6.0

# Step 2: Investigate dependency tree
composer why symfony/console

# Step 3: Try updating with dependencies
composer update vendor/package-a --with-dependencies

# Step 4: If that fails, try removing one package
composer remove vendor/package-a
composer require vendor/package-b:^3.0

# Step 5: Find alternative packages
composer search symfony/console

# Step 6: As last resort, fork and create compatibility
# Use composer inline aliases
```

## Related Errors

- [Composer Package Not Found]({{< relref "/languages/php/composer-package-not-found" >}}) — package not available
- [Composer Autoload Error]({{< relref "/languages/php/composer-autoload-error" >}}) — autoload failures
- [Composer Platform Error]({{< relref "/languages/php/composer-platform" >}}) — platform issues
