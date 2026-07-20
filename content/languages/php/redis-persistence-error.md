---
title: "[Solution] PHP REDIS_PERSISTENCE_ERROR — Redis Extension Loading Failure"
description: "Fix PHP Startup: redis — Unable to initialize module. Reinstall extension, check PHP version compatibility, and verify paths."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 109
---

# PHP REDIS_PERSISTENCE_ERROR — Redis Extension Loading Failure

PHP reports `PHP Startup: redis: Unable to initialize module` or `Call to undefined function redis()` because the phpredis C extension failed to load or is not installed. This is a build/installation issue — the extension binary is incompatible with the current PHP version, missing, or misconfigured in `php.ini`.

## Common Causes

### Extension not installed

```php
<?php
function_exists('redis'); // false
// PHP Fatal error: Uncaught Error: Class 'Redis' not found
?>
```

### PHP version mismatch after upgrade

```php
<?php
// After upgrading from PHP 8.1 to 8.3
// PHP Startup: redis: Unable to initialize module
// Module compiled with module API number 20210903
// PHP compiled with module API number 20230831
phpinfo(); // shows redis extension not loaded
?>
```

### Wrong extension path in php.ini

```ini
; /etc/php/8.3/cli/php.ini
extension=redis.so
; error: Extension 'redis' not found at /usr/lib/php/20190902/
```

### Missing dependency libraries

```bash
$ php -m | grep redis
PHP Warning: PHP Startup: redis: Unable to initialize module
Module requires module API number 20210903
```

### Compiled against wrong PHP headers

```php
<?php
// redis.so compiled against PHP 8.1 headers
// running on PHP 8.3 — binary incompatibility
echo phpversion(); // 8.3.x
// PHP Startup: redis: Unable to initialize module
?>
```

## How to Fix

### Fix 1: Install phpredis via PECL

Install or reinstall the extension using PECL with the correct PHP version.

```bash
# Stop any running PHP-FPM
sudo systemctl stop php8.3-fpm

# Install for PHP 8.3
sudo pecl -d phpize_dir=/usr/bin/phpize -d php_config=/usr/bin/php-config install redis

# Enable the extension
echo "extension=redis.so" | sudo tee /etc/php/8.3/mods-available/redis.ini

# Enable for CLI and FPM
sudo phpenmod -v 8.3 -s cli redis
sudo phpenmod -v 8.3 -s fpm redis

# Restart PHP-FPM
sudo systemctl start php8.3-fpm

# Verify
php -m | grep redis
```

### Fix 2: Install via Package Manager

Use your OS package manager to install the version-matched extension.

```bash
# Debian/Ubuntu
sudo apt update
sudo apt install php8.3-redis

# CentOS/RHEL
sudo dnf install php-redis

# Verify
php -m | grep redis
php --ri redis
```

### Fix 3: Verify Extension Path in php.ini

Ensure the extension path points to the correct location.

```bash
# Find the active php.ini
php --ini

# Check if extension_dir is correct
php -i | grep extension_dir

# Place redis.so in the correct directory
ls -la $(php -i | grep extension_dir | awk '{print $3}')/redis.so
```

```ini
; /etc/php/8.3/cli/php.ini
extension_dir = "/usr/lib/php/20230831/"
extension = redis.so
```

### Fix 4: Rebuild from Source Against Current PHP

Compile the extension from source for exact PHP version compatibility.

```bash
# Download the latest stable release
pecl download redis
tar -xzf redis-6.0.2.tgz
cd redis-6.0.2

# Build against current PHP
phpize
./configure --enable-redis
make -j$(nproc)
sudo make install

# Enable
echo "extension=redis.so" | sudo tee /etc/php/8.3/mods-available/redis.ini
sudo phpenmod redis

# Verify
php -r "var_dump(class_exists('Redis'));"  # bool(true)
```

### Fix 5: Check for Conflicting Extensions

Remove or disable duplicate or conflicting Redis extensions.

```bash
# List all loaded extensions
php -m | grep -i redis

# Check for igbinary or other conflicts
php --ri redis

# Disable conflicting extensions
sudo phpdismod -v 8.3 -s cli igbinary  # if not needed

# Restart services
sudo systemctl restart php8.3-fpm
```

## Examples

### Runtime Extension Check

```php
<?php
function ensureRedisExtension(): void
{
    if (!extension_loaded('redis')) {
        $iniPath = php_ini_loaded_file();
        throw new RuntimeException(
            "The phpredis extension is not loaded.\n"
            . "Active php.ini: {$iniPath}\n"
            . "Run: sudo apt install php" . PHP_MAJOR_VERSION . "." . PHP_MINOR_VERSION . "-redis"
        );
    }

    if (!class_exists('Redis')) {
        throw new RuntimeException(
            "The Redis class is not available. "
            . "The extension loaded but initialization failed — check php-fpm error logs."
        );
    }
}

ensureRedisExtension();
$redis = new Redis();
?>
```

### Health Check Script

```php
<?php
function redisExtensionReport(): array
{
    $report = [
        'extension_loaded' => extension_loaded('redis'),
        'class_available'  => class_exists('Redis'),
        'php_version'      => phpversion(),
        'extension_version' => phpversion('redis') ?: 'N/A',
        'extension_dir'    => php_ini_get('extension_dir'),
        'ini_file'         => php_ini_loaded_file(),
    ];

    return $report;
}

$report = redisExtensionReport();
print_r($report);

// Expected output when working:
// [extension_loaded] => 1
// [class_available]  => 1
// [php_version]      => 8.3.x
// [extension_version] => 6.0.2
?>
```

### Docker Setup

```dockerfile
FROM php:8.3-cli

# Install phpredis via PECL
RUN pecl install redis \
    && docker-php-ext-enable redis

# Verify installation
RUN php -r "var_dump(class_exists('Redis'));"

COPY app.php /app/app.php
CMD ["php", "/app/app.php"]
```

## Related Errors

- [Redis Connection Error]({{< relref "/languages/php/redis-connection-error" >}})
- [Redis Auth Error]({{< relref "/languages/php/redis-auth-error" >}})
- [Memcached Connection Error]({{< relref "/languages/php/memcached-connection-error" >}})
