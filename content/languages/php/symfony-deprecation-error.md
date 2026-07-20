---
title: "[Solution] PHP SYMFONY_DEPRECATION_WARNING — Deprecated Feature Usage"
description: "Fix PHP SYMFONY_DEPRECATION_WARNING by following migration guides, updating deprecated code, and checking Symfony version compatibility. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 116
---

# PHP SYMFONY_DEPRECATION_WARNING — Deprecated Feature Usage

A deprecated Symfony feature was used. This warning indicates code that uses functionality scheduled for removal in a future Symfony version, requiring migration to the recommended alternative.

## Common Causes

```php
// Using deprecated form types
use Symfony\Component\Form\Extension\Core\Type\TextType;
// Old: $builder->add('name', 'text'); // deprecated string type
// New: $builder->add('name', TextType::class);
```

```php
// Using deprecated security configuration
// Old security.yaml format (Symfony 4.x)
security:
    encoders:
        AppBundle\Entity\User: bcrypt

// New format (Symfony 5.4+)
security:
    password_hashers:
        App\Entity\User: auto
```

```php
// Using deprecated annotation routes
/**
 * @Route("/blog", name="blog_index")
 */
// Deprecated in Symfony 6.4, use PHP 8 attributes instead
use Symfony\Component\Routing\Attribute\Route;

#[Route('/blog', name: 'blog_index')]
```

```php
// Using deprecated service autowiring
// Old: services: { _defaults: { autowire: true, autoconfigure: true } }
// New: explicit service configuration recommended
```

```php
// Using deprecated Doctrine methods
$em->persist($entity); // still works but method may be deprecated in newer versions
$em->remove($entity);
$em->flush();
```

## How to Fix

### Fix 1: Follow Migration Guide

```bash
# Check deprecated code in your project
php bin/console deprecation:detect

# Use Rector to auto-fix deprecations
composer require rector/rector --dev
vendor/bin/rector process --config=rector.php

# Check Symfony version deprecations
php bin/console --help | grep -i deprecat
```

```php
// Before (deprecated)
use Symfony\Component\Form\Extension\Core\Type\TextType;
$builder->add('name', 'text');

// After (modern)
use Symfony\Component\Form\Extension\Core\Type\TextType;
$builder->add('name', TextType::class);
```

### Fix 2: Update Deprecated Code

```php
// Before (deprecated in Symfony 6.4)
use Symfony\Component\Security\Core\User\UserInterface;

class User implements UserInterface
{
    public function getSalt(): ?string
    {
        return null; // getSalt() is deprecated
    }
}

// After (Symfony 6.0+)
class User implements UserInterface
{
    public function eraseCredentials(): void
    {
        // Clear temporary data
    }

    // getSalt() removed — password_hashers handles this
}
```

```php
// Before (deprecated form type)
use Symfony\Component\Form\Extension\Core\Type\ChoiceType;

$builder->add('status', ChoiceType::class, [
    'choices' => [
        'Active' => 'active',
        'Inactive' => 'inactive',
    ],
    'choice_label' => function ($value, $key) {
        return $key;
    },
]);

// After (modern approach)
$builder->add('status', ChoiceType::class, [
    'choices' => [
        'Active' => 'active',
        'Inactive' => 'inactive',
    ],
    'label_attr' => ['class' => 'radio-label'],
]);
```

### Fix 3: Check Symfony Version Compatibility

```bash
# Check current Symfony version
php bin/console --version

# Update Symfony components
composer update symfony/*

# Check compatibility
composer why symfony/*

# Review UPGRADE file
cat UPGRADE-6.0.md
cat UPGRADE-7.0.md
```

```php
// Use version checks in code
if (Kernel::VERSION_ID >= 70000) {
    // Use Symfony 7 features
} else {
    // Use backward-compatible code
}
```

### Fix 4: Configure Deprecation Handler

```php
// public/index.php
use Symfony\Component\ErrorHandler\Debug;

_Debug::enable();

// Or configure error handler
use Symfony\Component\ErrorHandler\ErrorHandler;
use Symfony\Component\ErrorHandler\ErrorRenderer\HtmlErrorRenderer;

ErrorHandler::register();
ErrorHandler::setHandler(function (\Throwable $error) {
    if ($error instanceof \ErrorException) {
        $message = $error->getMessage();

        // Log deprecation warnings
        if (strpos($message, 'deprecated') !== false) {
            error_log("Deprecation: {$message}");
            return; // Don't display deprecation warnings
        }
    }

    // Handle other errors
    $handler = ErrorHandler::register();
    return $handler($error);
});

// In config/packages/framework.yaml
framework:
    error_handler:
        disabled: false
```

## Examples

```php
// Rector config for auto-updating deprecated code
// rector.php
use Rector\Config\RectorConfig;
use Rector\Set\ValueObject\LevelSetList;

return RectorConfig::configure()
    ->withPaths([
        __DIR__ . '/src',
    ])
    ->withSets([
        LevelSetList::UP_TO_PHP_82,
    ])
    ->withSets([
        // Symfony-specific rules
        \Rector\Symfony\Set\SymfonySetList::SYMFONY_52,
        \Rector\Symfony\Set\SymfonySetList::SYMFONY_53,
        \Rector\Symfony\Set\SymfonySetList::SYMFONY_54,
        \Rector\Symfony\Set\SymfonySetList::SYMFONY_60,
        \Rector\Symfony\Set\SymfonySetList::SYMFONY_61,
        \Rector\Symfony\Set\SymfonySetList::SYMFONY_62,
        \Rector\Symfony\Set\SymfonySetList::SYMFONY_63,
        \Rector\Symfony\Set\SymfonySetList::SYMFONY_64,
    ])
    ->withPhpSets(
        php82: true
    );
```

## Related Errors

- [Symfony Form Error](/languages/php/symfony-form-error)
- [Symfony Route Error](/languages/php/symfony-route-error)
- [Deprecated Filter](/languages/php/deprecated-filter)
- [E-Deprecated](/languages/php/e-deprecated)
