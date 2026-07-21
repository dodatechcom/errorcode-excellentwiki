---
title: "[Solution] Perl Chdir Error"
description: "Fix Perl chdir errors when changing working directory including path not found and permission issues."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Chdir errors occur when Perl chdir() fails due to non-existent directory, permission denied, or incorrect path specification.

## Common Causes

- Directory does not exist
- Permission denied on target directory
- Path contains invalid characters
- chdir without checking return value

## How to Fix

### 1. Check return value

```perl
# WRONG: Not checking chdir
chdir('/some/dir');

# CORRECT: Check and report error
chdir('/some/dir') or die "Cannot chdir: $!";
```

### 2. Use File::Spec for portable paths

```perl
use File::Spec;
my $dir = File::Spec->catdir('home', 'user', 'project');
chdir($dir) or die "Cannot chdir to $dir: $!";
```

## Examples

```perl
use strict;
use warnings;
use Cwd;

my $start = cwd();
print "Starting in: $start\n";

chdir('/tmp') or die "Cannot chdir: $!";
print "Now in: " . cwd() . "\n";

chdir($start) or die "Cannot return: $!";
print "Back in: " . cwd() . "\n";
```

## Related Errors

- [File not found](/languages/perl/perl-file-not-found)
- [Permission denied](/languages/perl/perl-permission-denied)
- [Runtime error](/languages/perl/perl-runtime-error)
