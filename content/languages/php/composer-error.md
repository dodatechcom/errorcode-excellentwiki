---
title: "PHP Composer: No matching package found / version conflict"
description: "Fix PHP Composer package errors. Resolve version conflicts, missing packages, and dependency resolution failures."
languages: ["php"]
error-types: ["build-error"]
severities: ["error"]
tags: ["composer", "dependency", "version-conflict", "package", "install"]
weight: 5
---

# PHP Composer: No matching package found / version conflict

Composer errors occur when the dependency resolver cannot find a compatible set of packages. This happens due to version constraints, missing repositories, or conflicting requirements.

## Common Causes

- Version constraints are too strict and no compatible version exists
- Package was removed from Packagist
- PHP version requirement not met by available package versions
- Missing private repository configuration

## How to Fix

### Check Current Dependencies

```bash
composer show --installed
composer why vendor/package
```

### Relax Version Constraints

```json
{
    "require": {
        "vendor/package": "^1.0"
    }
}
```

```bash
composer update vendor/package
```

### Add Private Repository

```json
{
    "repositories": [
        {
            "type": "composer",
            "url": "https://private.repo.example.com/"
        }
    ]
}
```

### Ignore Platform Requirements Temporarily

```bash
composer install --ignore-platform-reqs
composer update --ignore-platform-req=php
```

## Examples

```bash
# Example 1: No matching package
composer require vendor/old-package
# Problem 1: don't recognize a unique package name
# Fix: verify package exists: composer search vendor/old-package

# Example 2: Version conflict
composer update
# Problem: laravel/framework (v10.0) requires php ^8.1 but you have 7.4
# Fix: upgrade PHP or downgrade laravel/framework

# Example 3: Plugin not found
composer require vendor/plugin
# Problem: could not find a version matching "vendor/plugin"
# Fix: check if package was renamed or archived on Packagist
```

## Related Errors

- [PHP Fatal error: Call to undefined function]({{< relref "/languages/php/call-to-undefined" >}})
- [PHP Fatal Error: Allowed memory size exhausted]({{< relref "/languages/php/fatal-error" >}})
- [PHP PDOException: SQLSTATE[HY000] database errors]({{< relref "/languages/php/pdo-error" >}})
