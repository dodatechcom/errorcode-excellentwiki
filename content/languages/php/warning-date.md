---
title: "[Solution] PHP Warning: date() Timezone Database — Set date.timezone Fix"
description: "Fix PHP Warning: date(): Timezone database. Set date.timezone in php.ini or use DateTimeZone class for correct timezone handling."
languages: ["php"]
severities: ["warning"]
error_types: ["runtime"]
tags: ["date", "timezone", "date.timezone", "DateTime", "DateTimeZone"]
date: 2026-07-15
---

# PHP Warning: date(): Timezone Database

This warning appears when PHP cannot determine the correct timezone for date and time functions. It typically occurs when `date.timezone` is not set in `php.ini` or when the system timezone cannot be inferred from the OS configuration.

## Common Causes

- `date.timezone` is missing or commented out in `php.ini`
- The server's OS timezone is not set or is set to an unrecognized value
- Using `date()`, `time()`, or `strtotime()` without an explicit timezone context
- Calling date functions in a containerized environment with no timezone configured

## Solutions

### 1. Set `date.timezone` in `php.ini`

The most straightforward fix — define the default timezone in your PHP configuration.

```ini
; php.ini
date.timezone = UTC
```

Common timezone values: `America/New_York`, `Europe/London`, `Asia/Tokyo`, `UTC`.

### 2. Set It Programmatically with `date_default_timezone_set()`

Set the timezone at the top of your script if you can't modify `php.ini`.

```php
date_default_timezone_set("America/New_York");

// Now date() works without warnings
echo date("Y-m-d H:i:s");
```

### 3. Use the `DateTimeZone` Class

For more control, create `DateTime` objects with explicit timezone handling.

```php
$tz = new DateTimeZone("Europe/Berlin");
$date = new DateTime("now", $tz);

echo $date->format("Y-m-d H:i:s T"); // T shows the timezone abbreviation
```

### 4. Set the Environment Variable

In Docker or CLI environments, set the timezone via the environment.

```dockerfile
# Dockerfile
ENV TZ=America/Chicago
```

```bash
# Or in your shell
export TZ="America/Chicago"
php script.php
```

### 5. List Available Timezones

Find the correct timezone string for your location.

```php
// List all supported timezones
echo implode("\n", DateTimeZone::listIdentifiers());

// Or from the command line
// php -r "print_r(DateTimeZone::listIdentifiers());"
```

## Common Timezone Values

| Region | Timezone String |
|---|---|
| US Eastern | `America/New_York` |
| US Central | `America/Chicago` |
| US Pacific | `America/Los_Angeles` |
| UK | `Europe/London` |
| Central Europe | `Europe/Berlin` |
| Japan | `Asia/Tokyo` |
| India | `Asia/Kolkata` |
| UTC | `UTC` |

## Related Errors

- [PHP Deprecated Filter](/languages/php/deprecated-filter)
- [PHP Notice: Undefined Variable](/languages/php/notice-undefined-variable)
