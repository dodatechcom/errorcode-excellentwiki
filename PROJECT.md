# errorcode.excellentwiki.com — Project Plan

## Overview

A comprehensive error code reference website covering OS errors (Windows, Linux, macOS) and programming language errors (Python, C/C++, PHP, Java, JavaScript, etc.), plus deprecated function migration guides. Every error code includes: description, cause, solution, and **copyable code snippet** to rectify the issue.

---

## Tech Stack

| Component | Choice | Notes |
|-----------|--------|-------|
| **Generator** | Hugo v0.162.1 (already installed) | May need `extended` version for Docsy's SCSS |
| **Theme** | Docsy v0.15.0 (Google) | 2.9k stars, technical docs, dark mode, left sidebar nav |
| **Search** | PageFind | Static search, indexes after `hugo` build |
| **Copy Code** | Custom shortcode + clipboard.js | Every code block gets a one-click copy button |
| **JSON API** | Hugo outputFormats | Generates `/api/errors.json` at build time |
| **Dark Mode** | Built into Docsy | Toggle in navbar |
| **Hosting** | Cloudflare Pages | Free, fast, custom domain |

---

## Content Structure

```
content/
├── _index.md                          # Homepage
│
├── os/                                # Operating System errors
│   ├── _index.md                      # Browse by OS overview
│   ├── windows/
│   │   ├── _index.md                  # Windows errors overview
│   │   ├── 0x80004005.md             # Individual error
│   │   ├── 0x80070005.md
│   │   └── ...
│   ├── linux/
│   │   ├── _index.md                  # Linux errno errors
│   │   ├── errno-1.md                # EPERM
│   │   ├── errno-2.md                # ENOENT
│   │   └── ...
│   └── macos/
│       ├── _index.md
│       ├── -43.md                     # FNFErr (File Not Found)
│       └── ...
│
├── languages/                         # Programming language errors
│   ├── _index.md                      # Browse by language
│   ├── python/
│   │   ├── _index.md
│   │   ├── typeerror.md
│   │   ├── valueerror.md
│   │   └── ...
│   ├── c/
│   │   ├── _index.md
│   │   └── ...
│   ├── cpp/
│   ├── php/
│   ├── java/
│   └── javascript/
│
├── deprecated/                        # Deprecated function migration guides
│   ├── _index.md                      # Overview of deprecated functions
│   ├── php/
│   │   ├── _index.md
│   │   ├── ereg-to-preg-match.md
│   │   ├── split-to-explode.md
│   │   ├── each-to-foreach.md
│   │   ├── mysql-to-mysqli.md
│   │   └── ...
│   ├── python/
│   │   ├── _index.md
│   │   ├── print-statement.md
│   │   ├── raw-input-to-input.md
│   │   ├── urllib2-to-urllib.md
│   │   └── ...
│   ├── javascript/
│   │   ├── _index.md
│   │   ├── escape-unescape.md
│   │   ├── substr-to-slice.md
│   │   ├── exec-command.md
│   │   └── ...
│   └── java/
│       ├── _index.md
│       ├── thread-stop.md
│       ├── date-methods.md
│       ├── class-new-instance.md
│       └── ...
│
├── search/
│   └── index.html                     # PageFind search page
│
└── api/
    └── _index.md                      # API endpoint documentation
```

---

## Error Page Frontmatter Template

```yaml
---
title: "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
error_code: "TypeError"
platforms: []                          # taxonomy (empty for language errors)
languages: ["python"]                  # taxonomy
error_types: ["runtime"]              # taxonomy: runtime | compile | build | link | syntax
severities: ["error"]                  # taxonomy: error | warning | notice
tags: ["type", "concatenation", "operands"]
weight: 10
description: "Occurs when trying to add a number and a string without conversion"
---

## Description
This error occurs when Python tries to use the `+` operator between incompatible types...

## Common Causes
1. Forgetting to convert int to str before concatenation
2. ...

## Solution

```python
# Wrong
result = 42 + "hello"

# Correct
result = str(42) + "hello"
# or
result = f"{42}hello"
```

## See Also
- [AttributeError](/languages/python/attributeerror/)
```

---

## Hugo Taxonomies (hugo.yaml)

```yaml
taxonomies:
  platform: "platforms"      # windows, linux, macos
  language: "languages"      # python, c, cpp, php, java, javascript
  error_type: "error-types"  # runtime, compile, build, link, syntax
  severity: "severities"     # error, warning, notice
  tag: "tags"
```

This enables automatic list pages:
- `/platforms/windows/` → all Windows errors
- `/languages/python/` → all Python errors
- `/error-types/runtime/` → all runtime errors

---

## Deprecated Function Page Frontmatter Template

```yaml
---
title: "ereg() is deprecated — Use preg_match() instead"
deprecated_function: "ereg"
replacement_function: "preg_match"
languages: ["php"]
deprecated_since: "PHP 5.3"
removed_in: "PHP 7.0"
error_message: "Deprecated: Function ereg() is deprecated"
tags: ["regex", "posix", "pcre"]
weight: 10
---

## What You'll See
```
Deprecated: Function ereg() is deprecated in /path/to/file.php on line 42
```

## Why It's Deprecated
The POSIX Extended Regular Expressions (ERE) used by `ereg()` have been
replaced by PCRE (Perl-Compatible Regular Expressions)...

## Old Code (Deprecated)
```php
<?php
if (ereg("^[a-zA-Z0-9]+$", $username)) {
    echo "Valid username";
}
?>
```

## New Code (Replacement)
```php
<?php
if (preg_match("/^[a-zA-Z0-9]+$/", $username)) {
    echo "Valid username";
}
?>
```

## Migration Steps
1. Add delimiters (`/`) around pattern
2. For case-insensitive: add `i` modifier
3. For capture groups: `$regs` array starts at index 1

## Bulk Migration Script
```php
function convertEregToPreg($code) {
    // ... automated migration
}
```
```

---

## Homepage Layout

```
+------------------------------------------+
|  ERRORCODE.EXCELLENTWIKI.COM             |
|  [Search bar...........................]  |
+------------------------------------------+
|  Browse by Platform  |  Browse by Lang   |
|  +------+ +------+   | +------+ +------+ |
|  | Win  | | Linux|   | | Py   | | C/C+| |
|  +------+ +------+   | +------+ +------+ |
|  +------+            | +------+ +------+ |
|  | macOS|            | | Java | | PHP | |
|  +------+            | +------+ +------+ |
+------------------------------------------+
|  Deprecated Functions Migration Guides    |
|  PHP | Python | JavaScript | Java        |
+------------------------------------------+
|  Recently Added | Popular Errors         |
|  ...            | ...                    |
+------------------------------------------+
```

---

## Data Sources

### Operating System Errors

| Platform | Source | Count |
|----------|--------|-------|
| **Windows** | [MS-ERREF](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-erref/) (Microsoft Learn) | ~15,000+ (Win32, HRESULT, NTSTATUS) |
| **Linux** | [errno.h](https://man7.org/linux/man-pages/man3/errno.3.html) (POSIX) + kernel source | ~133 (EPERM through EHWPOISON) |
| **macOS** | [MacErrors.h](https://github.com/apple-opensource-mirror/CarbonHeaders/blob/master/MacErrors.h) + Cocoa domains | ~6,400+ (Carbon + POSIX + Cocoa) |

### Programming Language Errors

| Language | Source | Count |
|----------|--------|-------|
| **Python** | [docs.python.org/3/library/exceptions.html](https://docs.python.org/3/library/exceptions.html) | ~66 built-in exceptions |
| **C/C++** | POSIX `errno.h` + compiler errors (GCC/Clang/MSVC) | ~133 errno + thousands of compiler errors |
| **PHP** | [php.net/manual/en/language.errors.php](https://www.php.net/manual/en/language.errors.php) | ~16 error types + exception classes |
| **Java** | [Oracle Java API](https://docs.oracle.com/javase/8/docs/api/) | ~100+ (Throwable hierarchy) |
| **JavaScript/Node.js** | [Node.js docs](https://nodejs.org/api/process.html) + ECMAScript spec | ~134 Node.js codes + standard JS errors |

### Deprecated Functions Sources

| Language | Source | Count |
|----------|--------|-------|
| **PHP** | PHP migration guides (php.net) + version changelogs | ~200+ across PHP 4→8 |
| **Python** | docs.python.org/deprecations + Python 2→3 migration | ~100+ deprecated/removed APIs |
| **JavaScript** | MDN Deprecated features + Node.js DEP list | ~50 JS + 160+ Node.js DEP codes |
| **Java** | Oracle Deprecated List (per JDK version) | ~500+ across all JDK versions |
| **C/C++** | Compiler warnings + POSIX standards | ~30 commonly used deprecated C functions |

### Existing Reference Sites (cross-reference)

| Site | Coverage |
|------|----------|
| [errcodes.dev](https://www.errcodes.dev) | Linux (131 codes), PHP (23 codes), Node.js (134 codes) |
| [koingosw.com/error-codes](https://www.koingosw.com/products/macpilot/error-codes.php) | 6,398 Apple error codes database |
| [Microsoft Learn MS-ERREF](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-erref/) | Official Windows error code reference |

---

## Content Scope

### MVP Launch (~200-300 error codes + ~50 deprecated functions)

| Category | Errors | Examples |
|----------|--------|----------|
| **Windows** | 20 | 0x80004005, 0x80070005, 0x80070002, BSOD codes |
| **Linux** | 15 | errno 1-15 (EPERM, ENOENT, ESRCH, etc.) |
| **macOS** | 10 | -43 (FNFErr), -36 (ioErr), -50 (paramErr) |
| **Python** | 15 | TypeError, ValueError, KeyError, IndexError, etc. |
| **C/C++** | 10 | Segfault, malloc fail, linker errors |
| **PHP** | 10 | Parse error, Fatal error, Warning codes |
| **Java** | 10 | NPE, ClassNotFound, OutOfMemory |
| **JavaScript** | 10 | ReferenceError, TypeError, SyntaxError |

### Deprecated Functions (MVP)

| Language | Functions | Examples |
|----------|-----------|----------|
| **PHP** | 15 | ereg, eregi, split, each, mysql_*, create_function, etc. |
| **Python** | 10 | print statement, raw_input, urllib2, has_key, etc. |
| **JavaScript** | 10 | escape/unescape, substr, execCommand, var, etc. |
| **Java** | 5 | Thread.stop, Date.getYear, finalize, Class.newInstance |

### Long-term Goal

| Category | Total Exists | Target |
|----------|-------------|--------|
| Windows Win32 | ~18,000 | Top 500+ common ones |
| Windows HRESULT | ~5,000 | Top 200+ common ones |
| Windows NTSTATUS | ~3,000 | Top 100+ common ones |
| Linux errno | 133 | **All 133** |
| macOS Carbon | ~6,400 | Top 200+ common ones |
| Python | 66 | **All 66** + third-party |
| C/C++ errno | 133 | **All 133** + compiler errors |
| PHP | 16 types + ~50 exceptions | **All** + common runtime errors |
| Java | ~100+ | **All** |
| JavaScript/Node.js | 134 | **All 134** Node.js codes |
| PHP deprecated | ~200+ | **All** across versions |
| Python deprecated | ~100+ | **All** across versions |
| JS deprecated | ~210+ | **All** (MDN + Node.js) |
| Java deprecated | ~500+ | Top 200+ most-used |

---

## Implementation Steps

| Step | Task | Details |
|------|------|---------|
| 1 | Install Hugo extended (if needed) | Required for Docsy SCSS |
| 2 | Init Hugo project + install Docsy | `hugo mod init`, add Docsy module |
| 3 | Configure `hugo.yaml` | Taxonomies, outputs, params, dark mode, OG tags, GSC |
| 4 | Create content structure | Directory tree as above |
| 5 | Build custom layouts | Override Docsy templates for error pages, homepage |
| 6 | Create copy-code shortcode | `layouts/shortcodes/copycode.html` + JS |
| 7 | Add sample error codes | ~200-300 errors across OS + languages |
| 8 | Add deprecated function guides | ~50 migration guides |
| 9 | Setup PageFind search | Add search page, configure build step |
| 10 | Configure JSON API output | Add outputFormat + template |
| 11 | Customize Docsy styling | Logo, colors, homepage blocks, print styles |
| 12 | Add Schema.org JSON-LD | HowTo/FAQPage structured data per error page |
| 13 | Add Open Graph + Twitter Cards | Meta tags for social sharing |
| 14 | Enable breadcrumbs | Docsy built-in support |
| 15 | Build Quick Reference page | Filterable table of all error codes |
| 16 | Add version filter for deprecated | PHP version, Python version filters |
| 17 | Create custom 404 page | Search suggestions + popular links |
| 18 | Add accessibility features | ARIA labels, alt text, heading hierarchy |
| 19 | Test local build | `hugo server` + verify all pages |
| 20 | Setup Cloudflare Pages | Connect repo, configure build command |

### Build Pipeline

```
# Local dev
hugo server

# Production build
hugo --minify
npx pagefind --site public
```

Cloudflare Pages build command: `hugo --minify && npx pagefind --site public`

---

## SEO Requirements

### Title Rules
- Title must start with `[Solution]` as an eye-catcher
- Format: `[Solution] <Error Code> <Platform/Language> - <Brief Description>`
- Examples:
  - `[Solution] Error Code 0x80004005 Windows 11 - Unspecified Error`
  - `[Solution] TypeError: Cannot read property 'map' of undefined Node.js`
  - `[Solution] ereg() is deprecated PHP 8 - Use preg_match() Instead`
- The `[Solution]` prefix immediately tells searchers this page has a fix, not just a problem discussion

### Meta Description Rules
- Keep between 150-160 characters
- Start with action word: "Learn how to fix...", "Get the solution for...", "Resolve..."
- Include the error code/message
- Mention the platform/language
- Examples:
  - "Learn how to fix Windows error 0x80004005 (Unspecified Error). Step-by-step solution with copyable code snippets."
  - "Resolve Python TypeError: unsupported operand type(s). Copy-paste fix with explanation of common causes."
  - "Replace deprecated ereg() with preg_match() in PHP. Migration guide with before/after code examples."

### Article Content Rules
- After H1 heading, first 2 lines must be a summary paragraph
- This summary is what search engines show as snippet in results
- Summary must include: what the error is, what causes it, that the page has the solution
- Example:

```markdown
# [Solution] Error Code 0x80004005 Windows 11 - Unspecified Error

Error 0x80004005 is a generic "Unspecified Error" that occurs across Windows
when operations fail without a specific error code. This guide provides
step-by-step fixes for Windows 11 with copyable commands.
```

### SEO Checklist Per Page
- [ ] Title follows `[Solution]` format
- [ ] Meta description is 150-160 chars, action-oriented
- [ ] First 2 lines after H1 are a keyword-rich summary
- [ ] H1 is unique across entire site
- [ ] URL slug is short and descriptive (e.g., `/os/windows/0x80004005/`)
- [ ] At least one H2 heading for structure
- [ ] Internal links to related errors (See Also section)
- [ ] Code blocks have language tags for syntax highlighting

### Hugo Frontmatter SEO Fields

```yaml
---
title: "[Solution] Error 0x80004005 Windows 11 - Unspecified Error"
description: "Learn how to fix Windows error 0x80004005 (Unspecified Error). Step-by-step solution with copyable code snippets and commands."
slug: "0x80004005"
---
```

---

## Key Features

1. **Search + Filter** — Search by error code, keyword, language, or OS (PageFind)
2. **JSON API** — REST endpoint at `/api/errors.json` for tool/IDE integration
3. **Dark mode** — Developer-friendly dark theme (Docsy built-in)
4. **Copyable code snippets** — Every solution has a one-click copy button
5. **Taxonomy-based browsing** — Browse by platform, language, error type, severity
6. **Deprecated function migration** — Old code → New code with migration scripts
7. **Version-aware** — Deprecated functions tagged with version info (deprecated since / removed in)
8. **Schema.org structured data** — JSON-LD for FAQPage and HowTo triggers rich snippets in Google
9. **Open Graph + Twitter Cards** — Preview cards when shared on social media
10. **Canonical URLs** — Prevents duplicate content penalties
11. **Breadcrumbs** — UX + SEO (`Home > Python > TypeError`)
12. **Related Errors** — Cross-link similar errors to keep visitors on-site
13. **Quick Reference table** — One page listing ALL error codes in a filterable table
14. **Version filter for deprecated pages** — Filter by PHP 7, PHP 8, Python 2→3, etc.
15. **Print-friendly styles** — Devs sometimes print solutions
16. **RSS feed** — Hugo generates by default, notify readers of new errors
17. **Google Search Console verification** — Meta tag in hugo.yaml
18. **Custom 404 page** — Docsy has one, customize with search suggestions
19. **Accessibility** — ARIA labels, proper heading hierarchy, alt text

---

## Technical Implementation Details

### Schema.org JSON-LD (Per Error Page)

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "[Solution] Error 0x80004005 Windows 11 - Unspecified Error",
  "description": "Step-by-step fix for Windows error 0x80004005",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Identify the cause",
      "text": "The error occurs because..."
    },
    {
      "@type": "HowToStep",
      "name": "Apply the fix",
      "text": "Run the following command..."
    }
  ]
}
```

### Open Graph + Twitter Cards

```yaml
# In frontmatter
meta:
  og:title: "[Solution] Error 0x80004005 Windows 11"
  og:description: "Step-by-step fix with copyable code snippets"
  og:type: "article"
  og:image: "/images/og-error-0x80004005.png"
  twitter:card: "summary_large_image"
```

### Breadcrumbs

Home > OS > Windows > 0x80004005
Home > Languages > Python > TypeError
Home > Deprecated > PHP > ereg() → preg_match()

Docsy has built-in breadcrumb support — enable in params.

### Quick Reference Page

`/content/quick-reference.md` — Filterable table:

| Code | Language | Description | Severity | Link |
|------|----------|-------------|----------|------|
| 0x80004005 | Windows | Unspecified Error | Error | [→](/os/windows/0x80004005/) |
| TypeError | Python | Type mismatch | Error | [→](/languages/python/typeerror/) |
| ENOENT | Linux | No such file or directory | Error | [→](/os/linux/errno-2/) |

### RSS Feed

Hugo generates `/index.xml` by default — submit to RSS readers for new error code updates.

### Custom 404 Page

```
Page Not Found

The error code or page you're looking for doesn't exist.
Try searching: [_____________] [Search]

Popular pages:
- Windows Error Codes
- Python Errors
- PHP Deprecated Functions
```

### Google Search Console

```yaml
# hugo.yaml
params:
  gsc_verification: "YOUR_VERIFICATION_CODE"
```

### Print Styles

Add `@media print` rules to hide nav, sidebar, and footer — keep only content + code blocks.

### Accessibility

- ARIA labels on navigation elements
- Proper heading hierarchy (H1 > H2 > H3, no skipping)
- Alt text on all images
- Keyboard navigable
- Color contrast ratio 4.5:1 minimum (Docsy default)
- Screen reader friendly code blocks with `aria-label`

---

## Notes

- Sole author initially — no community contributions yet
- Data storage format to be decided later (currently using Hugo content files)
- User has more requirements to share before full implementation
- Flowcharts: Create directly in pages using Mermaid.js (Hugo has shortcodes for this)
- Images: User will generate images — provide prompt text, user supplies the image file
