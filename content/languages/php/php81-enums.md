---
title: "[Solution] PHP 8.1 Enum Error — Invalid Enum Usage or Definition"
description: "Fix PHP 8.1 Enum Error by implementing enums correctly, checking cases, and using proper methods. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 306
---

# PHP 8.1 Enum Error — Invalid Enum Usage or Definition

An Enum Error occurs when enum definitions are invalid, enum cases are used incorrectly, or enums are compared using wrong methods. PHP 8.1 introduced native enumerations (enums) — a special kind of class with a fixed set of named values (cases). Enums can be basic (unit enums) or backed (with string or int values).

## Common Causes

```php
<?php
// Cause 1: Trying to instantiate an enum with new
enum Status { case Active; case Inactive; }
$status = new Status(); // Error — enums cannot be instantiated

// Cause 2: Using wrong comparison method
$status = Status::Active;
if ($status == 'Active') { } // Won't work — enums aren't strings
if ($status === Status::Active) { } // Correct

// Cause 3: Invalid enum value assignment
enum Color: string {
    case Red = 'red';
    case Green = 'green';
}
Color::Red->value = 'crimson'; // Error — readonly property

// Cause 4: Missing backing type for enum that needs it
enum Status {
    case Active;
    case Inactive;
}
echo Status::Active->value; // Error — no backing value

// Cause 5: Duplicate enum case values
enum Role: string {
    case Admin = 'admin';
    case User = 'admin'; // Error — duplicate value
}
?>
```

## How to Fix

### Fix 1: Use static access instead of instantiation

```php
<?php
enum Status {
    case Active;
    case Inactive;
    case Pending;
}

// Wrong
// $status = new Status();

// Correct — access via static properties
$status = Status::Active;
$all = Status::cases(); // [Status::Active, Status::Inactive, Status::Pending]
?>
```

### Fix 2: Use `===` for comparison and `->value` for backed enums

```php
<?php
enum Color: string {
    case Red = 'red';
    case Green = 'green';
    case Blue = 'blue';
}

$color = Color::Red;

// Correct comparison
if ($color === Color::Red) { /* ... */ }

// Get backing value
$value = $color->value; // 'red'

// Get name
$name = $color->name; // 'Red'
?>
```

### Fix 3: Use `from()` and `tryFrom()` for creating enums from values

```php
<?php
enum Status: string {
    case Active = 'active';
    case Inactive = 'inactive';
    case Pending = 'pending';
}

// from() throws ValueError if value doesn't match
$status = Status::from('active');

// tryFrom() returns null if value doesn't match
$status = Status::tryFrom('unknown'); // null
?>
```

### Fix 4: Implement methods and interfaces on enums

```php
<?php
enum Color: string {
    case Red = 'red';
    case Green = 'green';
    case Blue = 'blue';

    public function label(): string {
        return match($this) {
            self::Red   => 'Red Color',
            self::Green => 'Green Color',
            self::Blue  => 'Blue Color',
        };
    }

    public static function fromHex(string $hex): self {
        return match($hex) {
            '#ff0000' => self::Red,
            '#00ff00' => self::Green,
            '#0000ff' => self::Blue,
            default   => throw new ValueError("Unknown hex: $hex"),
        };
    }
}

echo Color::Red->label(); // 'Red Color'
?>
```

## Examples

```php
<?php
// Backed enum with integer values
enum TicketPriority: int {
    case Low = 1;
    case Medium = 5;
    case High = 10;
    case Critical = 100;
}

function comparePriorities(TicketPriority $a, TicketPriority $b): string {
    return $a->value > $b->value
        ? $a->name . ' is higher'
        : $b->name . ' is higher';
}

// Implementing an interface with enums
interface HasLabel {
    public function label(): string;
}

enum Season: string implements HasLabel {
    case Spring = 'spring';
    case Summer = 'summer';
    case Autumn = 'autumn';
    case Winter = 'winter';

    public function label(): string {
        return ucfirst($this->value);
    }
}

echo Season::Summer->label(); // 'Summer'
?>
```

## Related Errors

- [PHP 8.0 Match Expression Error](/languages/php/php80-match-expression/) — Non-exhaustive match with enums
- [PHP 8.1 Readonly Property Error](/languages/php/php81-readonly-properties/) — Enums are inherently readonly
- [PHP 8.1 Fibers Error](/languages/php/php81-fibers/) — Fiber-related errors
