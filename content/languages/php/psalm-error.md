---
title: "[Solution] Psalm Static Analysis Error Fix"
description: "Fix Psalm static analysis errors. Add type annotations, fix reported issues, use Psalm baseline, configure suppression."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1111
---

# Psalm Static Analysis Error

Psalm static analysis errors indicate type inconsistencies, missing annotations, or code patterns that Psalm identifies as potentially incorrect. Psalm focuses on type safety and provides detailed error messages with suggestions for fixes. These errors help catch bugs before runtime.

## Common Causes

```php
<?php
// Cause 1: Missing type annotations
function calculate($a, $b) { // Psalm: missing param types
    return $a + $b;
}

// Cause 2: Invalid type assignment
function getItems(): array {
    $items = null; // Psalm: assigning null to array
    return $items;
}

// Cause 3: Undefined class method
$user = findUser(1);
$user->getName(); // Psalm: possibly null
$user->nonExistent(); // Psalm: method does not exist

// Cause 4: Invalid argument type
function process(string $input): void {}
process(123); // Psalm: expects string, int given

// Cause 5: Missing return type
function getValue($key) { // Psalm: missing return type
    return $this->data[$key];
}
```

## How to Fix

### Fix 1: Add comprehensive type annotations

```php
<?php
// Bad: no types
function calculate($a, $b) {
    return $a + $b;
}

// Good: PHPDoc with Psalm types
/**
 * @param int|float $a
 * @param int|float $b
 * @return int|float
 */
function calculate(int|float $a, int|float $b): int|float
{
    return $a + $b;
}

// Or with native types
function calculate(float $a, float $b): float
{
    return $a + $b;
}
```

### Fix 2: Handle nullable and union types

```php
<?php
// Bad: not handling null
function processUser(User $user): string {
    return $user->profile->bio; // Psalm: $user->profile might be null
}

// Good: handle nullable properly
function processUser(User $user): string
{
    if ($user->profile === null) {
        return '';
    }
    return $user->profile->bio ?? '';
}

// Or use Psalm's @psalm-assert
/**
 * @psalm-assert non-empty-list<int> $list
 */
function validateList(array $list): void
{
    if (empty($list)) {
        throw new \InvalidArgumentException('List cannot be empty');
    }
}
```

### Fix 3: Create a Psalm baseline for existing errors

```bash
# Generate baseline for existing errors
psalm --set-baseline=psalm-baseline.xml

# The baseline file captures current errors
# Only new errors will be reported

# Update baseline as you fix errors
psalm --set-baseline=psalm-baseline.xml --update-baseline
```

```xml
<!-- psalm-baseline.xml -->
<?xml version="1.0"?>
<files>
    <file src="src/OldCode.php">
        <MixedArgument occurrences="2"/>
        <PossiblyNullArgument occurrences="1"/>
    </file>
</files>
```

### Fix 4: Configure Psalm suppression

```xml
<!-- psalm.xml -->
<?xml version="1.0"?>
<psalm
    errorLevel="4"
    resolveFromConfigFile="true"
>
    <projectFiles>
        <directory name="src"/>
        <ignoreFiles>
            <directory name="vendor"/>
        </ignoreFiles>
    </projectFiles>

    <issueHandlers>
        <MixedArgument>
            <errorLevel type="suppress">
                <file name="src/Legacy/old-file.php"/>
            </errorLevel>
        </MixedArgument>
    </issueHandlers>
</psalm>
```

### Fix 5: Run Psalm with specific error types

```bash
# Show only specific issue types
psalm --show-info=true --show-warnings=true src/

# Filter by error type
psalm --filter="MixedArgument" src/

# Output JSON for CI integration
psalm --output-format=json src/

# Auto-fix what Psalm can
psalm --auto-fix src/
```

## Examples

```php
<?php
// Psalm-annotated code

/**
 * @psalm-type UserData = array{name: string, age: int, email: string}
 * @param int $userId
 * @return UserData|null
 */
function getUserData(int $userId): ?array
{
    $raw = $db->query("SELECT * FROM users WHERE id = ?", [$userId]);
    if ($raw === null) {
        return null;
    }

    /**
     * @var UserData $data
     */
    $data = $raw->fetch_assoc();

    return $data;
}

// Usage with Psalm type checking
$user = getUserData(1);
if ($user === null) {
    throw new \RuntimeException("User not found");
}

// Psalm knows $user is UserData here
echo $user['name'];
```

## Related Errors

- [PHPStan Error]({{< relref "/languages/php/php-stan-error" >}}) — PHPStan analysis errors
- [TypeError]({{< relref "/languages/php/typeerror" >}}) — type errors at runtime
- [Rector Error]({{< relref "/languages/php/rector-error" >}}) — automated refactoring
