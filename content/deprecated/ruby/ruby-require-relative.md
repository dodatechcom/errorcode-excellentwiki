---
title: "[Solution] Deprecated Function Migration: require to require_relative"
description: "Migrate from deprecated require with relative paths to require_relative."
deprecated_function: "require './file'"
replacement_function: "require_relative 'file'"
languages: ["ruby"]
deprecated_since: "Ruby 1.9+"
---

# [Solution] Deprecated Function Migration: require to require_relative

The `require './file'` has been deprecated in favor of `require_relative 'file'`.

## Migration Guide

require_relative is explicit about relative paths

require with relative paths depends on working directory.

## Before (Deprecated)

```ruby
require './lib/helper'
```

## After (Modern)

```ruby
require_relative 'lib/helper'
```

## Key Differences

- require_relative uses caller's directory
- require depends on $LOAD_PATH
