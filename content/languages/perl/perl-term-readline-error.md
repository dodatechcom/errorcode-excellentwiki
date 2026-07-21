---
title: "[Solution] Perl Term::ReadLine Error"
description: "Fix Perl Term::ReadLine errors when implementing interactive command-line input with history and completion."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Term::ReadLine errors occur when the terminal input module is incorrectly configured or when readlines fails on non-terminal input.

## Common Causes

- Term::ReadLine not available or misconfigured
- readlines on non-interactive input (pipe)
- History not properly initialized
- Completion function not returning correct format

## How to Fix

### 1. Check if terminal is interactive

```perl
use Term::ReadLine;

# WRONG: Assuming interactive
my $term = Term::ReadLine->new('program');
my $input = $term->readline('Enter: ');

# CORRECT: Check STDIN
if (-t STDIN) {
    my $term = Term::ReadLine->new('program');
    my $input = $term->readline('Enter: ');
} else {
    $input = <STDIN>;
}
```

### 2. Initialize history properly

```perl
my $term = Term::ReadLine->new('program');
$term->Attribs->{attempted_completion_function} = sub {
    my ($text, $line, $start, $end) = @_;
    return ($text, qw(alpha bravo charlie));
};
```

## Examples

```perl
use strict;
use warnings;
use Term::ReadLine;

my $term = Term::ReadLine->new('Interactive Demo');
while (defined(my $input = $term->readline('command> '))) {
    last if $input eq 'quit';
    print "You typed: $input\n";
}
```

## Related Errors

- [Runtime error](/languages/perl/perl-runtime-error)
- [Module not found](/languages/perl/perl-module-not-found)
- [Compilation error](/languages/perl/perl-compilation-error)
