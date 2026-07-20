---
title: "[Solution] Twig Template Error Fix"
description: "Fix Twig template errors. Check template syntax, verify variable names, clear cache, check template paths."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1119
---

# Twig Template Error

Twig template errors occur during template compilation or rendering when the template syntax is invalid, variables are undefined, filters or functions don't exist, or template inheritance chains are broken. These errors typically throw `Twig\Error\Error` or `Twig\Error\LoaderError`.

## Common Causes

```twig
{# Cause 1: Undefined variable #}
<h1>{{ user.name }}</h1> {# $user not passed to template #}

{# Cause 2: Syntax error in template #}
{% if condition %}  {# missing endif #}

{# Cause 3: Unknown filter #}
{{ value|nonexistent_filter }}

{# Cause 4: Template not found #}
{% extends "base.html.twig" %} {# File doesn't exist #}

{# Cause 5: Invalid function call #}
{{ function() }} {# function not registered in Twig #}
```

## How to Fix

### Fix 1: Pass all required variables to templates

```php
<?php
// Bad: missing variable
$template = $twig->load('profile.html.twig');
echo $template->render(['name' => 'John']); // Missing 'email'

// Good: pass all required variables
echo $template->render([
    'name'  => 'John',
    'email' => 'john@example.com',
    'age'   => 30,
]);

// Or use default filter in template
{# In template: #}
{# {{ user.email|default('No email') }} #}
```

### Fix 2: Fix template syntax errors

```twig
{# Bad: missing endif #}
{% if user %}
    <h1>{{ user.name }}</h1>

{# Good: proper closing tags #}
{% if user %}
    <h1>{{ user.name }}</h1>
{% endif %}

{# Bad: unclosed block #}
{% block content %}
    <p>Hello</p>

{# Good: closed block #}
{% block content %}
    <p>Hello</p>
{% endblock %}

{# Bad: wrong filter syntax #}
{{ items | join(', ') }}

{# Good: proper filter chaining #}
{{ items|join(', ') }}
```

### Fix 3: Register custom filters and functions

```php
<?php
use Twig\Environment;
use Twig\Loader\FilesystemLoader;

$loader = new FilesystemLoader('/path/to/templates');
$twig = new Environment($loader);

// Register custom filter
$filter = new \Twig\TwigFilter('reverse_string', function (string $string) {
    return strrev($string);
});
$twig->addFilter($filter);

// Register custom function
$function = new \Twig\TwigFunction('path_for', function (string $name, array $params = []) {
    return $this->router->pathFor($name, $params);
});
$twig->addFunction($function);

// Now these work in templates
{# {{ value|reverse_string }} #}
{# {{ path_for('home') }} #}
```

### Fix 4: Verify template paths are configured correctly

```php
<?php
use Twig\Loader\FilesystemLoader;
use Twig\Environment;

// Check template paths
$loader = new FilesystemLoader([
    '/path/to/templates',           // Main templates
    '/path/to/bundles/templates',   // Bundle templates
]);

$twig = new Environment($loader, [
    'cache' => '/tmp/twig_cache',
    'auto_reload' => true, // Recompile when templates change
    'debug' => true,       // Show detailed errors
]);

// Debug: list registered paths
var_dump($loader->getPaths());
```

### Fix 5: Clear Twig cache when templates change

```php
<?php
// Clear Twig cache
$cacheDir = '/tmp/twig_cache';

if (is_dir($cacheDir)) {
    $files = new RecursiveIteratorIterator(
        new RecursiveDirectoryIterator($cacheDir, RecursiveDirectoryIterator::SKIP_DOTS),
        RecursiveIteratorIterator::CHILD_FIRST
    );

    foreach ($files as $fileinfo) {
        $action = ($fileinfo->isDir() ? 'rmdir' : 'unlink');
        $action($fileinfo->getRealPath());
    }

    rmdir($cacheDir);
}

// Or disable cache in development
$twig = new Environment($loader, [
    'cache' => false, // Disable caching in dev
]);
```

## Examples

```php
<?php
// Complete Twig setup with error handling

use Twig\Environment;
use Twig\Loader\FilesystemLoader;
use Twig\Error\LoaderError;
use Twig\Error\RuntimeError;
use Twig\Error\SyntaxError;

function renderTemplate(
    Environment $twig,
    string $templateName,
    array $context = []
): string {
    try {
        $template = $twig->load($templateName);
        return $template->render($context);
    } catch (LoaderError $e) {
        // Template file not found
        error_log("Template not found: {$e->getMessage()}");
        return '<div class="error">Template not available</div>';
    } catch (SyntaxError $e) {
        // Template has syntax errors
        error_log("Template syntax error: {$e->getMessage()}");
        return '<div class="error">Template error</div>';
    } catch (RuntimeError $e) {
        // Error during rendering
        error_log("Template render error: {$e->getMessage()}");
        return '<div class="error">Render error</div>';
    }
}

// Usage
$loader = new FilesystemLoader('/path/to/templates');
$twig = new Environment($loader, ['cache' => '/tmp/twig_cache']);

$html = renderTemplate($twig, 'page.html.twig', [
    'title' => 'My Page',
    'content' => 'Hello World',
]);
```

## Related Errors

- [Twig Error]({{< relref "/languages/php/twig-error" >}}) — general Twig errors
- [Symfony Form Error]({{< relref "/languages/php/symfony-form-error" >}}) — Symfony form rendering
- [Laravel View Error]({{< relref "/languages/php/laravel-view-error" >}}) — Laravel Blade errors
