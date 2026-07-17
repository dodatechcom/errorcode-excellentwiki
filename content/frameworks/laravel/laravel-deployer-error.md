---
title: "Deployer deployment error"
description: "Laravel Deployer throws deployment errors when the Deployer task fails during deployment"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when a Deployer-based Laravel deployment fails during any of its tasks (checkout, composer install, migration, symlink creation, etc.).

## Common Causes

- SSH key not configured for the deployment user
- `composer install` fails on the production server
- Insufficient disk space for new releases
- `.env` file missing or misconfigured on the server
- Shared directory permissions incorrect

## How to Fix

1. Verify the `deploy.php` configuration:

```php
<?php
namespace Deployer;

require 'recipe/laravel.php';

set('repository', 'git@github.com:user/repo.git');
set('shared_files', ['.env']);
set('shared_dirs', ['storage']);
set('writable_dirs', ['storage', 'bootstrap/cache']);

host('production')
    ->set('deploy_path', '/var/www/app')
    ->set('user', 'deployer');
```

2. Test the deployment manually:

```bash
# Deploy to production
dep deploy production

# Run a specific task
dep deploy:unlock production
```

3. Check the deployment log:

```bash
# View release history
ls -la /var/www/app/releases/

# Check the latest release
cat /var/www/app/current/storage/logs/deployer.log
```

4. Ensure the server has required PHP extensions:

```bash
# On the production server
php -m | grep -E 'mbstring|xml|curl|mysql|zip'
composer install --no-dev --optimize-autoloader
```

## Examples

```bash
# Error: The "shared" directory does not exist
# Fix: Create the shared directory
ssh deployer@server "mkdir -p /var/www/app/shared/storage"
```

## Related Errors

- [Vapor error]({{< relref "/frameworks/laravel/vapor-error" >}})
- [Sail error]({{< relref "/frameworks/laravel/sail-error" >}})
