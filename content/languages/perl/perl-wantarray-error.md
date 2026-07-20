---
title: "[Solution] Perl wantarray Context Error Fix"
description: "Fix Perl wantarray context errors. Learn how to properly handle scalar, list, and void context in subroutines."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1040
---

## What This Error Means

A wantarray context error occurs when a subroutine behaves differently based on the calling context (void, scalar, or list) and the context detection or return values are wrong.

## Common Causes

- Not returning appropriate values for each context type
- Using wantarray incorrectly or not at all when context matters
- Returning a list in scalar context when a count is expected
- Void context producing unwanted side effects
- Chaining functions that expect specific context

## How to Fix

```perl
# WRONG: Ignoring context
sub get_data {
    my @data = (1, 2, 3, 4, 5);
    return @data;  # Always returns list
}
my $count = get_data();  # Gets 5 (last element), not count!

# CORRECT: Use wantarray to return appropriately
sub get_data {
    my @data = (1, 2, 3, 4, 5);
    return wantarray ? @data : scalar(@data);
}
```

```perl
# WRONG: Void context not handled
sub log_message {
    my $msg = shift;
    # Doing work even in void context is fine, but:
    return "Logged: $msg";  # Returns unexpected value
}

# CORRECT: Return nothing in void context
sub log_message {
    my $msg = shift;
    print LOG "INFO: $msg\n";
    return if defined wantarray;  # Return if not void
    return "Logged: $msg";
}
```

```perl
# WRONG: Context-sensitive returns for debugging
sub get_user {
    my $id = shift;
    return { id => $id, name => "User$id" } if wantarray;
    return "User$id";  # Inconsistent return types
}

# CORRECT: Document and return consistent types
sub get_user {
    my $id = shift;
    return wantarray
        ? { id => $id, name => "User$id" }
        : "User$id";
}
```

## Examples

```perl
sub fetch_records {
    my $query = shift;
    my @results = get_from_db($query);
    if (wantarray) {
        return @results;
    } elsif (defined wantarray) {
        return scalar @results;
    } else {
        # Void context - do nothing extra
        return;
    }
}

# Usage:
my @all = fetch_records("SELECT * FROM t");  # List of rows
my $cnt = fetch_records("SELECT * FROM t");  # Count of rows
fetch_records("SELECT * FROM t");            # Void - nothing
```

## Related Errors

- [Perl runtime error](perl-runtime-error) - runtime issue
- [Perl undefined value](perl-undefined-value) - undefined value
- [Perl list error](perl-list-error) - list issue
