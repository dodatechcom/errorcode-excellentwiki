---
title: "Vite Asset Import.meta.glob Error"
description: "Vite fails when using import.meta.glob for asset imports."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Vite Asset — import.meta.glob Error

This error occurs when Vite's `import.meta.glob` feature fails to import assets. The glob pattern may not match any files, or the import structure may be incorrect.

## Common Causes

- Glob pattern matches no files
- Incorrect glob syntax
- Files outside the allowed root
- Missing files in the glob directory

## How to Fix

### Check Glob Pattern

```javascript
// Correct glob pattern
const modules = import.meta.glob('./modules/**/*.ts');

// Check if pattern matches files
// ls src/modules/**/*.ts
```

### Use Correct Import Syntax

```javascript
// Named imports
const modules = import.meta.glob('./modules/*.ts', {
  import: 'default',
});

// Eager loading
const modules = import.meta.glob('./modules/*.ts', {
  eager: true,
});
```

### Fix Relative Paths

```javascript
// From src/components/App.vue
// Correct
const images = import.meta.glob('../assets/images/*.{png,jpg}');

// Wrong
const images = import.meta.glob('/assets/images/*.{png,jpg}');
```

### Handle Empty Results

```javascript
const modules = import.meta.glob('./components/*.vue', {
  eager: true,
});

// Check if any modules were found
if (Object.keys(modules).length === 0) {
  console.warn('No components found');
}
```

### Debug Glob Matches

```javascript
const modules = import.meta.glob('./features/**/*.ts');
console.log('Matched files:', Object.keys(modules));
```

## Examples

```text
[vite] Internal server error: Failed to resolve glob
  "./components/*.vue" — no matches found

[vite] Error: import.meta.glob "./assets/**/*.svg"
  could not find any files matching the pattern
```

## Related Errors

- [Vite Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — general build failure
- [Vite Asset Error]({{< relref "/tools/vite/vite-asset-error" >}}) — general asset errors
- [Vite Plugin Error]({{< relref "/tools/vite/vite-plugin-error" >}}) — plugin errors
