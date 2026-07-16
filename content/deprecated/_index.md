---
title: "Deprecated Functions — Migration Guides for PHP, Python, JS, Java"
description: "Migration guides for deprecated functions in PHP, Python, JavaScript, and Java. Old code → New code with copyable replacement snippets."
---

Deprecated functions are still present in the language but will be removed in a future version — or already have been. Continuing to use them risks sudden breakage after an upgrade and makes your code harder to maintain.

This section provides side-by-side migration guides: what the old function did, why it was removed, and the modern replacement code you can copy and paste directly into your project.

{{< columns >}}

## PHP

PHP has removed hundreds of functions across the 5.x → 7.x → 8.x transitions, including `ereg`, `split`, `each`, `mysql_*`, and more.

[View PHP Deprecations →](/deprecated/php/)

<--->

## Python

Python 3 broke backward compatibility with many Python 2 constructs — `print` statement, `raw_input`, `urllib2`, `ConfigParser`, and others.

[View Python Deprecations →](/deprecated/python/)

<--->

## JavaScript

Web APIs and ECMAScript features deprecated by MDN and TC39 — `escape`, `substr`, `document.execCommand`, `with` statement, and more.

[View JavaScript Deprecations →](/deprecated/javascript/)

{{< /columns >}}

{{< columns >}}

## Java

JDK deprecations from `Thread.stop()` and `Date` constructors to the `finalize()` method and `SecurityManager`.

[View Java Deprecations →](/deprecated/java/)

{{< /columns >}}

## General Migration Advice

1. **Check your deprecation warnings** — enable deprecation warnings in development (`-Xlint:deprecation` for Java, `DeprecationWarning` for Python, `E_DEPRECATED` for PHP).
2. **Search-and-replace with a test safety net** — write a test that exercises the deprecated code path first, then replace and verify the test still passes.
3. **Pin your minimum language version** — document the lowest version your project supports so contributors know what constructs are safe to use.
