---
title: "[Solution] Composer Package Not Found Error"
description: "Fix 'Could not find a version of package' error. Check package name, version constraints, repository availability."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1108
---

# Composer Package Not Found

The Composer "Could not find a version of package" error occurs when Composer cannot locate a package that matches your constraints. This is typically caused by typos in the package name, version constraints that don't match available releases, or packages not available in configured repositories.

## Common Causes

```bash
# Cause 1: Typo in package name
composer require monolog/monollog  # misspelled

# Cause 2: Version constraint too strict
composer require phpunit/phpunit:^11.0  # if PHP < 8.2

# Cause 3: Package removed or renamed
composer require symfony/http-kernel  # old name

# Cause 4: Private package not in repository
composer require company/internal-package

# Cause 5: Minimum stability mismatch
composer require vendor/package:dev-main  # requires minimum-stability: dev
```

## How to Fix

### Fix 1: Verify the exact package name on Packagist

```bash
# Search Packagist for the correct name
composer search monolog

# Check the exact name at https://packagist.org/
# Use the exact vendor/package format from Packagist
composer require monolog/monolog
```

### Fix 2: Relax version constraints

```php
// Check your composer.json
{
    "require": {
        "phpunit/phpunit": "^10.0",  // instead of ^11.0
        "monolog/monolog": "^2.0",    // instead of ^3.0
        "php": ">=8.1"               // ensure PHP version compatible
    }
}
```

```bash
# Check available versions
composer show --available phpunit/phpunit

# Or check all versions on Packagist
# https://packagist.org/packages/phpunit/phpunit

# Use less restrictive constraints
composer require phpunit/phpunit:"^9.5 || ^10.0"
```

### Fix 3: Check if package exists and is maintained

```bash
# Search for the package
composer search package-name

# Check package info
composer show vendor/package-name

# If package was abandoned, find replacement
composer show --available vendor/package-name
# Look for "abandoned" field
```

### Fix 4: Configure repositories for private packages

```json
{
    "repositories": [
        {
            "type": "composer",
            "url": "https://packages.example.com/",
            "options": {
                "http": {
                    "header": ["Authorization: Bearer TOKEN"]
                }
            }
        }
    ],
    "require": {
        "company/private-package": "^1.0"
    }
}
```

### Fix 5: Handle minimum-stability for dev versions

```json
{
    "minimum-stability": "dev",
    "prefer-stable": true,
    "require": {
        "vendor/package": "dev-main"
    }
}
```

```bash
# Or require with specific stability flag
composer require vendor/package:dev-main@dev

# Or prefer stable releases
composer require vendor/package:"^1.0@stable"
```

## Examples

```bash
# Complete debugging workflow

# 1. Verify package exists
composer show --available vendor/package-name

# 2. Check your PHP version
php -v

# 3. Check available versions
composer show --all vendor/package-name | head -20

# 4. Try without version constraint
composer require vendor/package-name

# 5. Clear cache and retry
composer clear-cache
composer update

# 6. Check for typos — diff with packagist
composer show --available monolog/monolog | grep -i name
```

## Related Errors

- [Composer Autoload Error]({{< relref "/languages/php/composer-autoload-error" >}}) — autoload failures
- [Composer Conflict Error]({{< relref "/languages/php/composer-conflict-error" >}}) — dependency conflicts
- [Composer Platform Error]({{< relref "/languages/php/composer-platform" >}}) — platform requirements
