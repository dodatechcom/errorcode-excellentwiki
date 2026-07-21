---
title: "[Solution] Deprecated Function Migration: short tags to full PHP tags"
description: "Migrate from deprecated short PHP tags to full <?php tags."
deprecated_function: "<? ... ?>"
replacement_function: "<?php ... ?>"
languages: ["php"]
deprecated_since: "PHP 7.0+"
---

# [Solution] Deprecated Function Migration: short tags to full PHP tags

The `<? ... ?>` has been deprecated in favor of `<?php ... ?>`.

## Migration Guide

Short open tags (<?) are not portable and may be disabled. Always use <?php for compatibility.

## Before (Deprecated)

```php
<? echo $name; ?>
<? echo "Hello"; ?>
```

## After (Modern)

```php
<?php echo $name; ?>
<?php echo "Hello"; ?>

// Or short echo tag (always enabled)
<?= $name ?>
```

## Key Differences

- <?php is always enabled
- <? depends on short_open_tag ini setting
- <?= is always available since PHP 5.4
- Use <?= for template output
