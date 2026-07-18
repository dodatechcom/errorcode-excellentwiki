---
title: "[Solution] Perl Glob Iterator Exhausted Error Fix"
description: "Fix Perl 'Glob iterator exhausted' errors. Learn why File::Glob fails and how to handle file pattern matching safely in Perl."
languages: ["perl"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

The Perl `Glob iterator exhausted` error occurs when `File::Glob` or the `<*>` glob operator encounters too many matches or hits internal limits during pattern expansion. This typically happens with very large directory listings or recursive glob patterns.

## Why It Happens

- The glob pattern matches an extremely large number of files
- Recursive glob patterns create excessive iterations
- The `GLOB_LIMIT` is exceeded (default 65536 matches on some systems)
- A glob pattern is too broad (e.g., `/**/*`)
- The system runs out of file handles during directory traversal
- Memory is exhausted from building the result list

## How to Fix It

### Use File::Glob with explicit limits

```perl
# WRONG: Unbounded glob may exhaust iterator
my @files = <*.{txt,log,csv,xml,json,html,css,js}>;  # many matches

# CORRECT: Use File::Glob with flags
use File::Glob ':bsd_glob';
use Errno qw(EDQUOT);

my @files = bsd_glob("*.{txt,log}", GLOB_NOSORT | GLOB_NOCHECK);
```

### Use File::Find for recursive traversal

```perl
# WRONG: Recursive glob pattern
my @all_files = <**/*>;  # may exhaust iterator

# CORRECT: Use File::Find for reliable recursive traversal
use File::Find;

my @all_files;
find(sub {
    push @all_files, $File::Find::name if -f;
}, '/path/to/search');
```

### Process files in batches

```perl
# CORRECT: Process glob results incrementally
use File::Glob ':bsd_glob';

my $iter = bsd_globIter("*.log");
while (my $file = $iter->()) {
    process_file($file);
}
```

### Limit glob scope with specific patterns

```perl
# WRONG: Very broad pattern
my @files = </var/**/*>;  # huge directory tree

# CORRECT: Use specific patterns
my @files = </var/log/*.log>;  # specific directory and extension
my @recent = </var/log/syslog.*>;  # even more specific
```

### Handle glob errors with eval

```perl
# CORRECT: Catch glob errors
use File::Glob ':bsd_glob';

my @files;
eval {
    @files = bsd_glob($pattern, GLOB_NOSORT);
};
if ($@) {
    if ($@ =~ /Glob iterator exhausted/) {
        warn "Too many matches for pattern: $pattern";
        # Fall back to directory reading
        opendir(my $dh, $dir) or die;
        @files = grep { /$regex/ } readdir($dh);
        closedir($dh);
    } else {
        die $@;
    }
}
```

### Use DirHandle for manual directory iteration

```perl
# CORRECT: Manual iteration for large directories
use DirHandle;

my $dh = DirHandle->new("/var/log") or die "Cannot open: $!";
while (defined(my $file = $dh->read)) {
    next if $file =~ /^\./;
    process_file("/var/log/$file");
}
$dh->close;
```

## Common Mistakes

- Not knowing that `<**/*>` creates a recursive glob which can be very slow
- Using glob in void context without checking for errors
- Not closing directory handles opened by glob
- Assuming glob results are sorted (they may not be)
- Using glob with user-supplied patterns without sanitization

## Related Pages

- [Perl File Test Error](perl-file-test-error) - file test operator error
- [Perl File Not Found](perl-file-not-found-v2) - file not found
- [Perl I/O Error](perl-io-error) - file I/O error
- [Perl Uninitialized Warning](perl-uninitialized-warning) - undef value
