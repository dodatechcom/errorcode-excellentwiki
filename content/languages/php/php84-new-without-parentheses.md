---
title: "[Solution] PHP New Without Parentheses Error Fix"
description: "Fix 'new without parentheses' errors in PHP 8.4. Learn correct object instantiation syntax and edge cases."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "php84", "instantiation", "syntax-error", "fatal-error"]
severity: "error"
---

# New Without Parentheses Error

## Error Message

```
Fatal error: Uncaught Error: Cannot use 'new' without parentheses when calling __invoke on an object in /path/to/file.php:10
```

## Common Causes

- Using the new expression result directly to call a method without parentheses in PHP 8.4
- Chaining method calls on a new expression without proper parenthesization
- Using 'new ClassName::method()' instead of '(new ClassName())->method()' for static-like calls
- Mixing new expressions with null-safe operator in ambiguous syntax

## Solutions

### Solution 1: Use parentheses when chaining on new expressions

PHP 8.4 requires explicit parentheses when performing method calls on new expression results.

```php
<?php
// WRONG: Method call on new without parentheses
class Factory {
    public function create(): Product {
        // In PHP 8.4, this requires parentheses
        return new Product()->withName('Widget');
    }
}

// CORRECT: Parenthesize the new expression
class Product {
    private string $name = '';

    public function withName(string $name): self {
        $clone = clone $this;
        $clone->name = $name;
        return $clone;
    }

    public function getName(): string {
        return $this->name;
    }
}

$product = (new Product())->withName('Widget');
echo $product->getName(); // 'Widget'
?>
```

### Solution 2: Assign new expressions to variables before chaining

Store the new object in a variable first, then call methods — avoids ambiguity and improves readability.

```php
<?php
class Request {
    private string $method = 'GET';
    private string $url = '';

    public function method(string $m): self {
        $clone = clone $this;
        $clone->method = $m;
        return $clone;
    }

    public function url(string $u): self {
        $clone = clone $this;
        $clone->url = $u;
        return $clone;
    }

    public function send(): string {
        return "{$this->method} {$this->url}";
    }
}

// Store in a variable, then chain
$request = new Request();
$result = $request->method('POST')->url('/api/users')->send();
echo $result; // 'POST /api/users'
?>
```

### Solution 3: Use static factory methods instead of chaining new

Static factory methods on the class itself avoid the parentheses issue entirely.

```php
<?php
class HttpClient {
    private string $baseUrl;
    private string $method;
    private array $headers;

    private function __construct(string $baseUrl) {
        $this->baseUrl = $baseUrl;
        $this->method = 'GET';
        $this->headers = [];
    }

    public static function to(string $url): self {
        return new self($url);
    }

    public function post(): self {
        $clone = clone $this;
        $clone->method = 'POST';
        return $clone;
    }

    public function withHeader(string $key, string $value): self {
        $clone = clone $this;
        $clone->headers[$key] = $value;
        return $clone;
    }

    public function toArray(): array {
        return [
            'url'     => $this->baseUrl,
            'method'  => $this->method,
            'headers' => $this->headers,
        ];
    }
}

$config = HttpClient::to('https://api.example.com')
    ->post()
    ->withHeader('Content-Type', 'application/json')
    ->toArray();

print_r($config);
?>
```

## Prevention Tips

- Always wrap new expressions in parentheses when chaining methods: (new Foo())->bar()
- Static factory methods like ClassName::create() are often cleaner than new+chain patterns
- Use IDE auto-formatting to catch ambiguous new expression syntax before running code
- Review upgrade guides when moving to PHP 8.4 — new expression syntax rules have changed

## Related Errors

- [PHP Typed Property Error]({{< relref "/languages/php/php80-typed-property-error" >}})
- [PHP Parse Error]({{< relref "/languages/php/parse-error" >}})
- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}})
