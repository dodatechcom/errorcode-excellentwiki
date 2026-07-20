---
title: "[Solution] PHP 8.4 Property Hook Error — Invalid Property Hook Definition"
description: "Fix PHP 8.4 Property Hook Error by using correct hook syntax, understanding virtual properties, and implementing hooks properly. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 316
---

# PHP 8.4 Property Hook Error — Invalid Property Hook Definition

A Property Hook Error occurs when property hooks are defined with incorrect syntax or invalid combinations. PHP 8.4 introduced property hooks — a way to define custom get/set behavior for properties directly in the property declaration, similar to languages like C#. Hooks can be virtual (no backing storage) or hooked (with storage).

## Common Causes

```php
<?php
// Cause 1: Missing curly braces for hook body
class User {
    public string $name {
        get => $this->name; // Error — hooks require full syntax
    }
}

// Cause 2: Hook with incompatible visibility
class Item {
    public string $name {
        private get { return $this->_name; } // Error — get can't be more restrictive
    }
}

// Cause 3: Virtual property without get hook
class Circle {
    public float $radius;
    public float $area { // Error — no get hook for virtual property
    }
}

// Cause 4: Using hooks on readonly properties
class Config {
    public readonly string $host {
        get { return $this->host; } // Error — readonly + hooks conflict
    }
}

// Cause 5: Hook with both initial value and virtual
class Mixed {
    public string $name = 'default' {
        get { return strtoupper($this->name); } // Conflict between default and hook
    }
}
?>
```

## How to Fix

### Fix 1: Use correct property hook syntax

```php
<?php
class User {
    public string $name {
        get {
            return $this->_name ?? '';
        }
        set(string $value) {
            $this->_name = trim(strtoupper($value));
        }
    }

    private string $_name;
}

$user = new User();
$user->name = 'alice';
echo $user->name; // ALICE (uppercase via set hook)
?>
```

### Fix 2: Use virtual properties (no backing storage)

```php
<?php
class Rectangle {
    public float $width;
    public float $height;

    public float $area {
        get {
            return $this->width * $this->height;
        }
    }

    public float $perimeter {
        get {
            return 2 * ($this->width + $this->height);
        }
    }

    public function __construct(float $width, float $height) {
        $this->width = $width;
        $this->height = $height;
    }
}

$rect = new Rectangle(5.0, 3.0);
echo $rect->area;      // 15.0 (virtual — computed, no storage)
echo $rect->perimeter; // 16.0
?>
```

### Fix 3: Use hooks for validation and transformation

```php
<?php
class Email {
    private string $_address;

    public string $address {
        get {
            return $this->_address;
        }
        set(string $value) {
            if (!filter_var($value, FILTER_VALIDATE_EMAIL)) {
                throw new InvalidArgumentException("Invalid email: $value");
            }
            $this->_address = strtolower($value);
        }
    }

    public function __construct(string $address) {
        $this->address = $address; // Triggers set hook
    }
}

$email = new Email('Alice@Example.COM');
echo $email->address; // alice@example.com (lowercased by set hook)
?>
```

### Fix 4: Combine hooks with asymmetric visibility

```php
<?php
class Product {
    public private(set) float $price {
        get {
            return $this->_price;
        }
        set {
            if ($value < 0) {
                throw new InvalidArgumentException('Price cannot be negative');
            }
            $this->_price = $value;
        }
    }

    private float $_price;

    public function __construct(float $price) {
        $this->price = $price;
    }
}

$product = new Product(9.99);
echo $product->price;     // 9.99
// $product->price = 5.0; // Error — private(set)
?>
```

## Examples

```php
<?php
// Property hooks with interface-like behavior
class Temperature {
    private float $_celsius;

    public float $celsius {
        get { return $this->_celsius; }
        set { $this->_celsius = $value; }
    }

    public float $fahrenheit {
        get { return $this->_celsius * 9/5 + 32; }
        set { $this->_celsius = ($value - 32) * 5/9; }
    }

    public float $kelvin {
        get { return $this->_celsius + 273.15; }
        set { $this->_celsius = $value - 273.15; }
    }

    public function __construct(float $celsius = 0.0) {
        $this->celsius = $celsius;
    }
}

$temp = new Temperature(100);
echo $temp->fahrenheit; // 212.0
$temp->fahrenheit = 32;
echo $temp->celsius;    // 0.0

// Hook with lazy initialization pattern
class Database {
    private ?Connection $_connection = null;

    public Connection $connection {
        get {
            if ($this->_connection === null) {
                $this->_connection = Connection::create();
            }
            return $this->_connection;
        }
    }
}
?>
```

## Related Errors

- [PHP 8.1 Readonly Property Error](/languages/php/php81-readonly-properties/) — Readonly vs hooks
- [PHP 8.4 Asymmetric Visibility Error](/languages/php/php84-asymmetric-visibility/) — Visibility with hooks
- [PHP 8.2 Readonly Class Error](/languages/php/php82-readonly-classes/) — Readonly classes
