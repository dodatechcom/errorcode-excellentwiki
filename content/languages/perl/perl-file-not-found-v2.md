---
title: "[Solution] Perl No Such File or Directory Error"
description: "Fix Perl file not found errors. Handle missing files, incorrect paths, and permission issues in file operations."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["file", "not-found", "path", "open", "permission", "perl"]
weight: 5
---

## What This Error Means

The error `No such file or directory` occurs when Perl tries to open, read, or write a file that doesn't exist at the specified path.

## Common Causes

- File path does not exist
- Incorrect relative path
- Working directory changed
- File permissions prevent access
- Filename typo

## How to Fix

```perl
# WRONG: No file existence check
open(my $fh, '<', $filename) or die "Error: $!";  # May fail

# CORRECT: Check file exists first
use File::Basename;
use Cwd 'abs_path';

if (-e $filename) {
    open(my $fh, '<', $filename) or die "Cannot open: $!";
} else {
    die "File not found: $filename";
}
```

```perl
# WRONG: Wrong path separator
my $path = "data\results.csv";  # Backslash issues on Windows

# CORRECT: Use File::Spec for cross-platform
use File::Spec;
my $path = File::Spec->catfile('data', 'results.csv');
```

```perl
# WRONG: Relative path assumption
open(my $fh, '<', 'data.txt');  # Fails if working dir changed

# CORRECT: Use absolute path or check working directory
use Cwd 'cwd';
print "Current dir: " . cwd() . "\n";
open(my $fh, '<', 'data.txt') or die "Cannot open data.txt from " . cwd();
```

## Examples

```perl
# Example 1: Safe file open wrapper
sub safe_open {
    my ($mode, $file) = @_;
    open(my $fh, $mode, $file)
        or die "Cannot open '$file' (mode $mode): $!";
    return $fh;
}

# Example 2: Find file in multiple locations
sub find_file {
    my $filename = shift;
    my @search_paths = ('./data', './config', '/etc/myapp');
    
    for my $dir (@search_paths) {
        my $full = "$dir/$filename";
        return $full if -f $full;
    }
    die "File '$filename' not found in any search path";
}

# Example 3: Create file if not exists
use Fcntl qw(:flock);
unless (-e $file) {
    open(my $fh, '>', $file) or die "Cannot create: $!";
    close($fh);
}
```

## Related Errors

- [perl-module-not-found]({{< relref "/languages/perl/perl-module-not-found" >}}) — module not found
- [perl-undefined-value]({{< relref "/languages/perl/perl-undefined-value" >}}) — undefined value
- [perl-socket-error]({{< relref "/languages/perl/perl-socket-error" >}}) — socket error
