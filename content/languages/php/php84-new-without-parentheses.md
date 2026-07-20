---
title: "[Solution] PHP 8.4 New Without Parentheses Error — New Instantiation Syntax Error"
description: "Fix PHP 8.4 New Without Parentheses Error by using correct new syntax, checking PHP version, and verifying class exists. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 317
---

# PHP 8.4 New Without Parentheses Error — New Instantiation Syntax Error

The New Without Parentheses Error occurs when the `new` keyword is used with incorrect syntax or in contexts where parentheses are required. PHP 8.4 may change certain instantiation behaviors. This error often appears when chaining method calls on new objects, using new in expressions, or when the class doesn't exist.

## Common Causes

```php
<?php
// Cause 1: Missing parentheses on class without constructor
class Logger {
    public function log(string $msg): void { echo $msg; }
}

$logger = new Logger; // Deprecated in PHP 8.4 (parentheses recommended)
$logger->log('hello');

// Cause 2: Chaining without parentheses on new
$result = new User->getName(); // Error — must wrap in parentheses
$result = (new User())->getName(); // Correct

// Cause 3: New in complex expression without parentheses
$obj = new MyClass + 1; // Parse error — ambiguous
$obj = (new MyClass()) + 1; // Correct

// Cause 4: Class doesn't exist
$obj = new NonExistentClass(); // Error — class not found

// Cause 5: Anonymous class without parentheses
$handler = new class { public function handle() {} }; // May need () for some uses
$handler->handle();
?>
```

## How to Fix

### Fix 1: Always use parentheses when instantiating

```php
<?php
// PHP 8.4 deprecates new without parentheses
class User {
    public function __construct(
        public string $name,
    ) {}
}

// Recommended — always use parentheses
$user = new User('Alice');

// Also for classes without explicit constructors
class Helper {}
$helper = new Helper(); // Preferred over new Helper
?>
```

### Fix 2: Wrap new in parentheses for method chaining

```php
<?php
class QueryBuilder {
    private array $conditions = [];

    public function where(string $condition): self {
        $this->conditions[] = $condition;
        return $this;
    }

    public function build(): string {
        return implode(' AND ', $this->conditions);
    }
}

// Wrong
// $query = new QueryBuilder->where('active = 1')->build();

// Correct — wrap new in parentheses
$query = (new QueryBuilder())
    ->where('active = 1')
    ->where('deleted = 0')
    ->build();
?>
```

### Fix 3: Use parentheses in complex expressions

```php
<?php
class Counter {
    private int $count = 0;

    public function increment(): self {
        $this->count++;
        return $this;
    }

    public function getCount(): int {
        return $this->count;
    }
}

// Wrong — ambiguous
// $result = new Counter + 1;

// Correct — explicit parentheses
$result = (new Counter())->increment()->getCount(); // 1

// Correct — new in array
$items = [
    (new User('Alice')),
    (new User('Bob')),
];
?>
```

### Fix 4: Verify class exists before instantiation

```php
<?php
function createInstance(string $className, mixed ...$args): object {
    if (!class_exists($className)) {
        throw new InvalidArgumentException("Class not found: $className");
    }

    return new $className(...$args);
}

$user = createInstance(User::class, 'Alice');
?>
```

## Examples

```php
<?php
// Proper instantiation patterns
class HttpClient {
    public function __construct(
        private string $baseUrl,
    ) {}

    public function get(string $path): mixed {
        return ['url' => $this->baseUrl . $path];
    }
}

// Method chaining with parentheses
$response = (new HttpClient('https://api.example.com'))
    ->get('/users');

// Anonymous class instantiation
$handler = new class {
    public function handle(string $input): string {
        return strtoupper($input);
    }
};

echo $handler->handle('hello'); // HELLO

// Factory pattern with parentheses
class LoggerFactory {
    public static function create(string $type): Logger {
        return match ($type) {
            'file'  => new FileLogger(),
            'db'    => new DatabaseLogger(),
            default => new Logger(),
        };
    }
}
?>
```

## Related Errors

- [PHP 8.0 Match Expression Error](/languages/php/php80-match-expression/) — Expression syntax errors
- [PHP 8.0 Named Argument Error](/languages/php/php80-named-argument/) — Constructor argument errors
- [PHP 8.4 Property Hook Error](/languages/php/php84-property-hooks/) — PHP 8.4 syntax features
