---
title: "[Solution] Perl Template Toolkit Parse Error Fix"
description: "Fix Perl Template Toolkit parsing and rendering errors. Learn why TT templates fail and how to debug template syntax and variables."
languages: ["perl"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Perl Template Toolkit error occurs when the TT engine fails to parse or render a template file. These errors include syntax issues in TT directives, undefined variables, missing INCLUDE files, and invalid PROCESS directives. TT provides detailed error messages including the template file and line number.

## Why It Happens

- Unclosed TT directives (`[%` without `%]`)
- Invalid variable syntax or method calls in templates
- INCLUDE or PROCESS references files that do not exist
- Template variables are not passed from the code
- FILTER or FUNCTION is not registered
- Template file encoding mismatches
- Recursive INCLUDE loops

## How to Fix It

### Fix unclosed TT directives

```html
<!-- WRONG: Unclosed directive -->
[% FOREACH item IN items %]
<li>[% item.name</li>
[% END %]

<!-- CORRECT: Close all directives -->
[% FOREACH item IN items %]
<li>[% item.name %]</li>
[% END %]
```

### Ensure all variables are passed to the template

```perl
# WRONG: Template expects variables not provided
my $tt = Template->new({ INCLUDE_PATH => '/templates' });
$tt->process('page.tt');  # $title not available

# CORRECT: Pass all required variables
my $tt = Template->new({ INCLUDE_PATH => '/templates' });
$tt->process('page.tt', {
    title => 'My Page',
    items => \@data,
});
```

### Check INCLUDE file paths

```perl
# CORRECT: Verify template search paths
my $tt = Template->new({
    INCLUDE_PATH => '/templates:/views:/partials',
    PRE_PROCESS  => 'config.tt',
});

# Test file existence
my $file = 'header.tt';
my $full_path = $tt->file($file);
warn "Template not found: $file" unless $full_path;
```

### Handle undefined variables gracefully

```html
<!-- WRONG: Variable may be undefined -->
<p>[% user.email %]</p>

<!-- CORRECT: Use default or check -->
<p>[% user.email || 'No email' %]</p>

<!-- Or use TT's default filter -->
<p>[% user.email | default('No email') %]</p>
```

### Use TRY/CATCH in templates

```html
<!-- CORRECT: Handle errors within templates -->
[% TRY %]
[% INCLUDE risky_partial.tt %]
[% CATCH %]
<p>Error loading partial: [% error.info %]</p>
[% END %]
```

### Debug template compilation

```perl
# CORRECT: Test template compilation
use Template;

my $tt = Template->new({ DEBUG => 1 });

# Check for parse errors
my $output;
unless ($tt->process('template.tt', {}, \$output)) {
    die "Template error: " . $tt->error();
}
```

## Common Mistakes

- Forgetting that TT variables are case-sensitive
- Not understanding that `[% INCLUDE %>` clones the context while `[% PROCESS %>` shares it
- Using Perl code directly in templates instead of using TT directives
- Not pre-compiling templates for production environments
- Forgetting that `[% FILTER %]` applies to the rest of the block

## Related Pages

- [Perl Mojolicious Error V2](perl-mojolicious-error-v2) - Mojolicious template error
- [Perl Dancer Error V2](perl-dancer-error-v2) - Dancer route error
- [Perl Runtime Error](perl-runtime-error) - general runtime issue
- [Perl Module Not Found](perl-module-not-found-v2) - module not found
