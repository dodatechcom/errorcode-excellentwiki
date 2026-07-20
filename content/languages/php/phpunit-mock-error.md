---
title: "[Solution] PHPUnit Mock Object Error Fix"
description: "Fix PHPUnit mock object errors. Verify method signatures, check return types, use proper mocking patterns."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1114
---

# PHPUnit Mock Object Error

PHPUnit mock object errors occur when mocks are configured incorrectly, method signatures don't match the original class, return type expectations are violated, or mock configurations conflict. These errors typically manifest during test setup or when the mock is invoked.

## Common Causes

```php
<?php
// Cause 1: Mocking a method that doesn't exist
$mock = $this->createMock(Service::class);
$mock->method('nonExistentMethod'); // Error: method not found

// Cause 2: Wrong return type from mock
$mock = $this->createMock(Service::class);
$mock->method('getData')->willReturn('string');
// But method signature says getData(): array

// Cause 3: Mocking final class
final class LockedService { }
$mock = $this->createMock(LockedService::class); // Error: cannot mock final

// Cause 4: Expecting more calls than configured
$mock->expects($this->exactly(2))->method('save');
$mock->save(); // Only called once — test fails

// Cause 5: Mocking static methods
Service::staticMethod(); // Cannot mock static methods with createMock
```

## How to Fix

### Fix 1: Verify method exists before mocking

```php
<?php
// Check the class interface before mocking
$reflection = new ReflectionClass(Service::class);
$methods = array_map(fn($m) => $m->getName(), $reflection->getMethods());
// Verify 'getData' is in $methods before mocking

// Good: mock only methods that exist
$mock = $this->createMock(Service::class);
$mock->method('getData')->willReturn(['key' => 'value']);
```

### Fix 2: Match mock return type to method signature

```php
<?php
// Bad: return type mismatch
interface DataProvider
{
    public function getData(): array;
}

$mock = $this->createMock(DataProvider::class);
$mock->method('getData')->willReturn('string'); // Wrong: expects array

// Good: return correct type
$mock->method('getData')->willReturn(['key' => 'value']);

// For nullable returns
$mock->method('findUser')->willReturn(null);

// For void methods, don't configure return
$mock->method('save')->willReturn(null); // PHPUnit ignores this for void
```

### Fix 3: Handle final classes with alternatives

```php
<?php
// Bad: cannot mock final class
final class LockedService { }
$mock = $this->createMock(LockedService::class);

// Good: create a concrete test double
class FakeLockedService extends LockedService
{
    // Extend the final class in test context (only works if you own the code)
}

// Better: refactor to use interfaces
interface ServiceInterface { public function getData(): array; }
final class LockedService implements ServiceInterface { }

$mock = $this->createMock(ServiceInterface::class); // Mock the interface
```

### Fix 4: Configure call count expectations correctly

```php
<?php
// Bad: expecting 2 calls but only 1 happens
$mock->expects($this->exactly(2))->method('save');
$this->service->process(); // Only calls save once

// Good: match expectations to actual behavior
$mock->expects($this->once())->method('save');

// Or use atLeast for flexible counts
$mock->expects($this->atLeastOnce())->method('save');

// Or use any() if count doesn't matter
$mock->expects($this->any())->method('log');
```

### Fix 5: Use proper mocking patterns for complex scenarios

```php
<?php
// Bad: trying to mock static methods
Service::staticMethod();

// Good: refactor static methods to instance methods
class UserService
{
    public function find(int $id): ?User
    {
        return $this->db->query("SELECT * FROM users WHERE id = ?", [$id]);
    }
}

// Mock the class, not the static method
$mock = $this->createMock(UserService::class);
$mock->method('find')->willReturn(new User(['name' => 'Test']));

// Or use Mockery for static method mocking (if available)
// \Mockery::mock('overload:' . Service::class);
```

## Examples

```php
<?php
// Complete mock example

class NotificationServiceTest extends TestCase
{
    public function testSendEmailUsesMailer(): void
    {
        // Create mock with return type matching
        $mailer = $this->createMock(Mailer::class);
        $mailer->expects($this->once())
            ->method('send')
            ->with(
                $this->callback(fn($email) => str_contains($email, '@'))
            )
            ->willReturn(true);

        // Inject mock into service
        $service = new NotificationService($mailer);

        $result = $service->sendWelcomeEmail('user@example.com');

        $this->assertTrue($result);
    }

    public function testHandlesMailFailure(): void
    {
        $mailer = $this->createMock(Mailer::class);
        $mailer->method('send')->willReturn(false);

        $service = new NotificationService($mailer);
        $result = $service->sendWelcomeEmail('user@example.com');

        $this->assertFalse($result);
    }
}
```

## Related Errors

- [PHPUnit Error]({{< relref "/languages/php/phpunit-error" >}}) — general test failures
- [PHPUnit Assertion Error]({{< relref "/languages/php/phpunit-assertion-error" >}}) — assertion issues
- [PHPUnit Deprecated]({{< relref "/languages/php/phpunit-deprecated" >}}) — deprecated features
