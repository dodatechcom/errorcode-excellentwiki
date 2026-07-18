---
title: "[Solution] Rails Asset Pipeline Error — How to Fix"
description: "Fix Rails asset pipeline errors. Resolve Sprockets compilation failures, missing assets, and precompilation issues."
frameworks: ["rails"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
comments: true
---

A Rails asset pipeline error occurs when Sprockets fails to compile, find, or serve static assets like CSS, JavaScript, and images.

## Why It Happens

Asset pipeline errors stem from missing asset files, incorrect require paths, configuration issues, or compilation failures. Common during upgrades or when adding new asset directories.

## Common Error Messages

```
Sprockets::FileNotFound: couldn't find file 'application.js'
```

```
Sprockets::CircularDependencyError: detected circular reference
```

```
AssetNotPrecompiled: Asset 'application.css' is not precompiled
```

```
ActionView::MissingTemplate: Missing asset manifest
```

## How to Fix It

### 1. Check Asset Manifest Files

Verify `app/assets/config/manifest.js` includes all asset directories.

```javascript
// app/assets/config/manifest.js
//= link_tree ../images
//= link_directory ../javascripts .js
//= link_directory ../stylesheets .css
```

### 2. Precompile Assets Before Deploy

Run precompilation to generate optimized files.

```bash
RAILS_ENV=production rails assets:precompile
```

### 3. Fix Circular Dependencies

Refactor JavaScript modules to remove circular references.

```javascript
// Use a shared module instead of circular require
export function formatDate(date) { ... }
```

### 4. Clear Sprockets Cache

Clear cached manifests when compilation issues persist.

```bash
rm -rf tmp/cache/assets
rails assets:clobber
rails assets:precompile
```

## Common Scenarios

**Scenario 1: After upgrading Rails, assets return 404.**
Check if you switched from Sprockets to Propshaft.

**Scenario 2: New JavaScript file not found.**
Add the file to `app/assets/config/manifest.js`.

**Scenario 3: Production fails during precompile.**
Run `rails assets:precompile` locally first.

## Prevent It

1. **Run `rails assets:precompile` in CI.**
Catch errors before deployment.

2. **Use fingerprinting in production.**
Enable `config.assets.digest = true` for cache busting.

3. **Keep asset directories organized.**
Place assets in the correct directories under `app/assets/`.

