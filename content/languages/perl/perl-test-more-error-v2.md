---
title: "[Solution] Perl Test More Assertion Failed Fix"
description: "Fix Perl Test::More assertion failures. Learn why test assertions fail and how to write correct Perl tests with Test::More."
languages: ["perl"]
severities: ["error"]
error-types: ["test-error"]
weight: 5
---

## What This Error Means

A Perl Test::More assertion failure occurs when a test function like `is`, `ok`, `like`, or `cmp_ok` does not match the expected result. Test::More is the standard Perl testing framework, and assertion failures indicate that the code under test is not behaving as expected.

## Why It Happens

- The function under test returns an unexpected value
- Test expectations are outdated after code changes
- Floating-point comparison fails due to precision
- The test does not account for side effects or order dependencies
- A mock or stub is not configured correctly
- The test assumes a specific system state (locale, time, files)
- `plan` count does not match the number of tests run

## How to Fix It

### Use correct comparison functions

```perl
# WRONG: Using ok() for detailed comparison
use Test::More;
ok(get_name() eq "Alice");  # no diagnostic on failure

# CORRECT: Use is() for exact comparison
use Test::More;
is(get_name(), "Alice", "get_name returns Alice");
```

### Handle floating-point comparisons

```perl
# WRONG: Exact comparison fails for floats
use Test::More;
is(calculate(), 3.14159, "pi calculation");  # may fail

# CORRECT: Use cmp_ok with tolerance or within()
use Test::More;
cmp_ok(abs(calculate() - 3.14159), '<', 0.0001, "pi calculation");

# Or use Test::Number::Delta
use Test::Number::Delta;
delta_within(calculate(), 3.14159, 0.0001, "pi calculation");
```

### Plan tests correctly

```perl
# WRONG: Plan does not match test count
use Test::More tests => 5;
is(1, 1, "one equals one");
is(2, 2, "two equals two");
# Only 2 tests but planned 5

# CORRECT: Use done_testing if count is dynamic
use Test::More;
is(1, 1, "one equals one");
is(2, 2, "two equals two");
done_testing();
```

### Test error conditions properly

```perl
# WRONG: Testing for errors without capturing them
use Test::More;
eval { risky_operation() };
ok(!$@, "no error");  # unclear what failed

# CORRECT: Use lives_ok or capture error details
use Test::More;
use Test::Exception;

lives_ok { risky_operation() } "risky_operation succeeds";

# Or test specific error
throws_ok { risky_operation() }
    qr/expected error message/,
    "correct error thrown";
```

### Isolate tests from external state

```perl
# WRONG: Test depends on system time
use Test::More;
use POSIX qw(strftime);
is(strftime("%Y", localtime), "2025", "current year");

# CORRECT: Mock time or test relative values
use Test::More;
use Test::MockTime qw(set_fixed_time restore_time);

set_fixed_time("2025-01-15T00:00:00");
is(strftime("%Y", localtime), "2025", "current year");
restore_time();
```

### Use subtests for complex test suites

```perl
# CORRECT: Use subtests for related assertions
use Test::More;

subtest "user creation" => sub {
    my $user = create_user("Alice");
    ok(defined $user, "user created");
    is($user->name, "Alice", "name is Alice");
};

subtest "user deletion" => sub {
    my $user = create_user("Bob");
    ok(delete_user($user->id), "user deleted");
    ok(!defined find_user($user->id), "user not found");
};
```

## Common Mistakes

- Using `ok()` when `is()` or `is_deeply()` would give better diagnostics
- Not including a test description string for every assertion
- Forgetting `done_testing()` when not using `tests => N`
- Writing tests that depend on execution order
- Not cleaning up test data in the test file

## Related Pages

- [Perl Runtime Error](perl-runtime-error) - general runtime issue
- [Perl Compilation Error](perl-compilation-error) - compile error
- [Perl Module Not Found](perl-module-not-found-v2) - module not found
- [Perl Uninitialized Warning](perl-uninitialized-warning) - undef value
