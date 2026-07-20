---
title: "[Solution] PHPUnit Test Failure Fix"
description: "Fix PHPUnit test failures. Check assertion logic, verify test setup, handle mock objects, debug test output."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1113
---

# PHPUnit Test Failure

PHPUnit test failures occur when test assertions don't match expected values, test setup is incorrect, or the code under test produces unexpected results. These failures appear as assertion errors or unexpected exceptions during test execution.

## Common Causes

```php
<?php
// Cause 1: Assertion value doesn't match expected result
$this->assertEquals(5, calculateTotal($items)); // Expected 5, got 6

// Cause 2: Test depends on external state (database, file system)
$user = UserRepository::find(1); // Database not seeded
$this->assertNotNull($user);

// Cause 3: Test order dependency
// Test B depends on Test A's side effects
public function testCreateUser() { /* creates user */ }
public function testDeleteUser() { /* assumes user exists from testCreate */ }

// Cause 4: Mock not configured correctly
$mock = $this->createMock(Service::class);
$mock->method('getData')->willReturn(null);
$result = $mock->getData();
$this->assertNotNull($result); // Fails: mock returns null

// Cause 5: Code throws unexpected exception
$this->assertTrue(processData($invalidInput)); // Exception thrown instead of bool
```

## How to Fix

### Fix 1: Verify assertion expectations match actual behavior

```php
<?php
// Debug: var_dump or print_r the actual value
$result = calculateTotal([1, 2, 3]);
var_dump($result); // int(6)
$this->assertEquals(6, $result); // Fix the expected value

// Use more specific assertions
$this->assertSame(6, $result);      // Strict type + value
$this->assertIsInt($result);        // Type check
$this->assertGreaterThan(0, $result); // Range check
```

### Fix 2: Use proper test isolation with setUp/tearDown

```php
<?php
class UserServiceTest extends TestCase
{
    private Database $db;

    protected function setUp(): void
    {
        $this->db = new Database();
        $this->db->beginTransaction(); // Wrap in transaction
    }

    protected function tearDown(): void
    {
        $this->db->rollBack(); // Undo all changes
    }

    public function testCreateUser(): void
    {
        $user = $this->db->createUser(['name' => 'Test']);
        $this->assertNotNull($user);
        $this->assertEquals('Test', $user->name);
    }
}
```

### Fix 3: Remove test order dependencies

```php
<?php
// Bad: tests depend on execution order
public function testCreate(): void {
    $this->assertTrue(User::create(['name' => 'John']));
}
public function testFind(): void {
    $user = User::find(1); // Depends on testCreate
    $this->assertNotNull($user);
}

// Good: each test is self-contained
public function testCreateAndFind(): void {
    $created = User::create(['name' => 'John']);
    $this->assertTrue($created);

    $found = User::find(1);
    $this->assertNotNull($found);
    $this->assertEquals('John', $found->name);
}

// Or use data providers for separate scenarios
/**
 * @dataProvider userProvider
 */
public function testUserWorkflow(array $userData, string $expectedName): void
{
    $user = User::create($userData);
    $this->assertEquals($expectedName, $user->name);
}

public function userProvider(): array
{
    return [
        [['name' => 'John'], 'John'],
        [['name' => 'Jane'], 'Jane'],
    ];
}
```

### Fix 4: Configure mocks correctly

```php
<?php
// Bad: mock not returning expected value
$mock = $this->createMock(Service::class);
$mock->method('getData')->willReturn(null);
$this->assertEquals('expected', $mock->getData()); // Fails

// Good: configure mock to return expected type
$mock = $this->createMock(Service::class);
$mock->expects($this->once())
    ->method('getData')
    ->willReturn(['key' => 'value']);

$result = $mock->getData();
$this->assertEquals('value', $result['key']);
```

### Fix 5: Debug test failures with verbose output

```bash
# Run with verbose output
vendor/bin/phpunit --verbose

# Run specific test
vendor/bin/phpunit --filter testCreateUser

# Output with colors and details
vendor/bin/phpunit --colors=always --display-errors

# Generate coverage report
vendor/bin/phpunit --coverage-html=coverage/
```

## Examples

```php
<?php
// Complete test example with proper patterns

class OrderServiceTest extends TestCase
{
    private OrderService $service;

    protected function setUp(): void
    {
        parent::setUp();
        $this->service = new OrderService();
    }

    public function testCalculateTotalWithValidItems(): void
    {
        $items = [
            ['price' => 10.00, 'quantity' => 2],
            ['price' => 5.50, 'quantity' => 1],
        ];

        $total = $this->service->calculateTotal($items);

        $this->assertEqualsWithDelta(25.50, $total, 0.001);
        $this->assertIsFloat($total);
    }

    public function testCalculateTotalWithEmptyItems(): void
    {
        $total = $this->service->calculateTotal([]);

        $this->assertEquals(0.0, $total);
    }

    public function testThrowsOnInvalidItem(): void
    {
        $this->expectException(\InvalidArgumentException::class);
        $this->expectExceptionMessage('Invalid item data');

        $this->service->calculateTotal([['invalid']]);
    }
}
```

## Related Errors

- [PHPUnit Assertion Error]({{< relref "/languages/php/phpunit-assertion-error" >}}) — assertion failures
- [PHPUnit Mock Error]({{< relref "/languages/php/phpunit-mock-error" >}}) — mock object issues
- [PHPUnit Deprecated]({{< relref "/languages/php/phpunit-deprecated" >}}) — deprecated PHPUnit features
