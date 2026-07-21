---
title: "[Solution] Perl END Block Error"
description: "Fix Perl END block errors including execution order issues and die handling within END blocks."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

END block errors occur when multiple END blocks execute in unexpected order, or when die is called within an END block causing secondary failures.

## Common Causes

- Multiple END blocks executing in reverse order
- die inside END block causing global destruction errors
- END block modifying global state
- Missing cleanup in END blocks

## How to Fix

### 1. Order END blocks correctly

```perl
# END blocks execute in reverse declaration order
END { print "Last END\n" }
END { print "First END\n" }  # runs first
```

### 2. Handle errors gracefully in END

```perl
END {
    eval {
        close $log_fh if $log_fh;
    };
    warn "Cleanup error: $@" if $@;
}
```

## Examples

```perl
use strict;
use warnings;

my $fh;

END {
    if ($fh) {
        close $fh;
        print "File closed in END block\n";
    }
}

open($fh, '>', 'temp.txt') or die "Cannot open";
print $fh "data\n";
```

## Related Errors

- [Die error](/languages/perl/die-error)
- [File not found](/languages/perl/perl-file-not-found)
- [Runtime error](/languages/perl/perl-runtime-error)
