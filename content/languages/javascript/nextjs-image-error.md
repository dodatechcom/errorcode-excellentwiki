---
title: "[Solution] Next.js Image Component Error Fix"
description: "Fix Next.js Image component errors with unconfigured external images, missing width/height, and image optimization issues."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Next.js Image Component Error

This error occurs when using the `next/image` component with unconfigured external images, missing required props, or invalid image sources.

## What This Error Means

Common error messages:

- `Error: Invalid src prop on next/image, ... hostname is not configured`
- `Error: Image with src "..." must be "width" and "height"`
- `Unhandled Runtime Error: Error occurred prerendering page`

The `next/image` component requires external image domains to be configured and images to have proper dimensions.

## Common Causes

```jsx
// Cause 1: Unconfigured external domain
import Image from 'next/image';
<Image src="https://external-site.com/image.jpg" width={500} height={300} />
// Error: hostname is not configured

// Cause 2: Missing width/height on non-static images
<Image src="/photo.jpg" /> // needs width and height

// Cause 3: Invalid image source
<Image src="not-a-url" width={100} height={100} />

// Cause 4: Dynamic imports with Image
const DynamicImage = dynamic(() => import('next/image'));
```

## How to Fix

### Fix 1: Configure allowed image domains

```javascript
// next.config.js
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'external-site.com',
      },
      {
        protocol: 'https',
        hostname: '**.example.com', // wildcard subdomain
      },
    ],
  },
};
```

### Fix 2: Use fill instead of fixed dimensions

```jsx
// For responsive images
<div style={{ position: 'relative', width: '100%', height: '300px' }}>
  <Image
    src="/photo.jpg"
    fill
    alt="Photo"
    style={{ objectFit: 'contain' }}
  />
</div>
```

### Fix 3: Provide width and height

```jsx
<Image
  src="/photo.jpg"
  width={800}
  height={600}
  alt="Description"
/>
```

### Fix 4: Use loader for unoptimized images

```jsx
const customLoader = ({ src }) => src;

<Image
  loader={customLoader}
  src="https://external-site.com/image.jpg"
  width={500}
  height={300}
  unoptimized
/>
```

## Examples

```jsx
// This triggers error
function Gallery() {
  return (
    <Image
      src="https://external-site.com/photo.jpg"
      alt="Gallery photo"
      // Missing width and height
    />
  );
}

// Fix
function Gallery() {
  return (
    <Image
      src="https://external-site.com/photo.jpg"
      alt="Gallery photo"
      width={800}
      height={600}
    />
  );
}
```

## Related Errors

- [Next.js Build Error]({{< relref "/languages/javascript/nextjs-build-error" >}}) — build failed
- [Next.js Hydration]({{< relref "/languages/javascript/nextjs-hydration" >}}) — hydration mismatch
- [Next.js App Router]({{< relref "/languages/javascript/nextjs-app-router" >}}) — App Router error
