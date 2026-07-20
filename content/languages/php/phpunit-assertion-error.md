---
title: "[Solution] PHPUnit Assertion Failure Fix"
description: "Fix PHPUnit assertion failures. Check expected vs actual values, use proper assertions, debug test data."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1115
---

# PHPUnit Assertion Failure

PHPUnit assertion failures occur when the expected value in a test doesn't match the actual value produced by the code. These are the most common type of test failure and usually indicate either a bug in the code under test or an incorrect expectation in the test.

## Common Causes

```php
<?php
// Cause 1: Wrong expected value in assertion
$this->assertEquals(10, calculateTotal([1, 2, 3])); // Actual: 6

// Cause 2: Type mismatch with assertEquals
$this->assertEquals("100", 100); // Fails: string vs int
// assertEquals does loose comparison, butassertSame fails on type

// Cause 3: Array structure mismatch
$this->assertEquals(
    ['a' => 1, 'b' => 2],
    ['a' => 1, 'c' => 2] // Different key
);

// Cause 4: Float precision issues
$this->assertEquals(0.3, 0.1 + 0.2); // Fails due to float precision

// Cause 5: Object comparison instead of value comparison
$this->assertEquals($expectedObj, $actualObj); // Compares properties, may miss
```

## How to Fix

### Fix 1: Use the correct assertion for the comparison type

```php
<?php
// For strict comparison (same value AND type)
$this->assertSame(6, calculateTotal([1, 2, 3]));

// For loose comparison (value only)
$this->assertEquals(6, calculateTotal([1, 2, 3]));

// For float comparisons with tolerance
$this->assertEqualsWithDelta(0.3, 0.1 + 0.2, 0.0001);

// For boolean checks
$this->assertTrue(isValid($input));
$this->assertFalse(isEmpty($data));

// For null checks
$this->assertNull($result);
$this->assertNotNull($result);
```

### Fix 2: Check expected vs actual with better diagnostics

```php
<?php
// Add message to assertion for debugging
$this->assertEquals(
    $expected,
    $actual,
    "Failed asserting that actual value matches expected"
);

// Or use var_dump before assertion in debugging
var_dump($actual);
$this->assertEquals($expected, $actual);

// Use assertSame for precise comparison
$this->assertSame($expected, $actual); // Fails if types differ
```

### Fix 3: Handle array comparison properly

```php
<?php
// For exact array match
$this->assertSame(
    ['name' => 'John', 'age' => 30],
    $user->toArray()
);

// For subset matching
$this->assertArrayHasKey('name', $array);
$this->assertArraySubset(['name' => 'John'], $array); // PHPUnit < 9

// For array count
$this->assertCount(3, $array);
$this->assertEmpty($array);

// For specific element values
$this->assertContains('expected', $array);
$this->assertNotContains('unwanted', $array);
```

### Fix 4: Handle float precision correctly

```php
<?php
// Bad: direct float equality
$this->assertEquals(0.3, 0.1 + 0.2); // Unreliable

// Good: use delta for float comparison
$this->assertEqualsWithDelta(0.3, 0.1 + 0.2, 0.0001);

// Or round before comparing
$this->assertEquals(
    round(0.3, 10),
    round(0.1 + 0.2, 10)
);

// For monetary values, compare as integers (cents)
$this->assertEquals(30, (int) round($price * 100));
```

### Fix 5: Debug failing assertions

```php
<?php
// Method 1: Use assertThat with custom message
$this->assertThat(
    $result,
    $this->equalTo($expected),
    "Result should match expected value for input: " . var_export($input, true)
);

// Method 2: Temporarily skip and investigate
// $this->markTestSkipped('Investigating failure');
// var_dump($result);

// Method 3: Use data providers to isolate failure
/**
 * @dataProvider additionProvider
 */
public function testAddition(int $a, int $b, int $expected): void
{
    $this->assertSame($expected, $a + $b);
}

public function additionProvider(): array
{
    return [
        'basic' => [1, 2, 3],
        'zero'  => [0, 0, 0],
        'negative' => [-1, -2, -3],
    ];
}
```

## Examples

```php
<?php
// Assertion examples for common scenarios

class ShoppingCartTest extends TestCase
{
    public function testCalculateSubtotal(): void
    {
        $cart = new ShoppingCart();
        $cart->addItem(new Item('Widget', 9.99, 3));

        $this->assertEqualsWithDelta(29.97, $cart->getSubtotal(), 0.01);
    }

    public function testItemStructure(): void
    {
        $item = new Item('Widget', 9.99, 3);

        $this->assertSame('Widget', $item->getName());
        $this->assertSame(9.99, $item->getPrice());
        $this->assertSame(3, $item->getQuantity());
    }

    public function testCartContainsItem(): void
    {
        $cart = new ShoppingCart();
        $cart->addItem(new Item('Widget', 9.99, 3));

        $this->assertCount(1, $cart->getItems());
        $this->assertContains('Widget', array_map(
            fn($i) => $i->getName(),
            $cart->getItems()
        ));
    }

    public function testEmptyCartTotal(): void
    {
        $cart = new ShoppingCart();

        $this->assertEmpty($cart->getItems());
        $this->assertEqualsWithDelta(0.0, $cart->getSubtotal(), 0.001);
    }
}
```

## Related Errors

- [PHPUnit Error]({{< relref "/languages/php/phpunit-error" >}}) — general test failures
- [PHPUnit Mock Error]({{< relref "/languages/php/phpunit-mock-error" >}}) — mock object issues
- [PHPUnit Deprecated]({{< relref "/languages/php/phpunit-deprecated" >}}) — deprecated features
