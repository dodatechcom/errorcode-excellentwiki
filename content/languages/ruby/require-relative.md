---
title: "[Solution] Ruby LoadError with require_relative — File Path Fix"
description: "Fix Ruby LoadError when using require_relative. Ensure correct relative paths from the current file's location."
languages: ["ruby"]
severities: ["error"]
error_types: ["load"]
tags: ["loaderror", "require_relative", "path", "relative"]
weight: 80
---

# LoadError with require_relative — File Path Fix

A `LoadError` with `require_relative` occurs when the relative path doesn't resolve to an existing file from the current file's directory.

## Description

`require_relative` resolves paths relative to the file containing the call, not the current working directory. This is different from `require`, which uses `$LOAD_PATH`.

Common scenarios:

- **Wrong relative path** — incorrect number of `../` levels.
- **Running from different directory** — path assumes specific location.
- **File structure changed** — files moved but requires not updated.
- **Capitalization mismatch** — `MyFile` vs `myfile` on case-sensitive systems.

## Common Causes

```ruby
# Cause 1: Wrong number of parent directory references
# File: app/models/user.rb
require_relative '../helper'  # LoadError if helper is in lib/, not app/

# Cause 2: Confusing require with require_relative
require_relative 'nokogiri'  # LoadError — this is a gem, not a local file

# Cause 3: File moved but require not updated
# Original: lib/utils.rb
# Moved to: lib/helpers/utils.rb
require_relative 'utils'  # LoadError after move

# Cause 4: Running script from wrong directory
# File: app/services/user_service.rb
require_relative '../../config/database'  # Depends on running from project root
```

## Solutions

### Fix 1: Verify the relative path

```ruby
# File: app/models/user.rb
# To require app/services/user_service.rb:

# Wrong
require_relative 'services/user_service'

# Correct — go up from models/ to app/, then into services/
require_relative '../services/user_service'
```

### Fix 2: Use absolute paths as fallback

```ruby
# Debug: see what path is being resolved
path = File.expand_path('../services/user_service', __FILE__)
puts path  # Shows the full path Ruby is looking for
require_relative path
```

### Fix 3: Use __dir__ for clarity

```ruby
# __FILE__ is the current file, __dir__ is its directory
# These are equivalent:
require_relative '../config/database'
require File.join(__dir__, '..', 'config', 'database')
```

### Fix 4: Organize with a loader file

```ruby
# lib/app_loader.rb
require_relative 'config/database'
require_relative 'services/user_service'
require_relative 'models/user'

# main.rb
require_relative 'lib/app_loader'
```

## Related Errors

- [LoadError](load-error) — general load error.
- [NameError](name-error) — undefined constant after failed require.
- [SyntaxError](syntax-error) — syntax error in loaded file.
