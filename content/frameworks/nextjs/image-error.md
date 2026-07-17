---
title: "Image optimization error"
description: "Next.js Image component fails to optimize or serve the image"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when the Next.js `Image` component fails to load or optimize an image, either due to an invalid source, missing loader configuration, or domain restrictions.

## Common Causes

- Image `src` points to a domain not allowed in `next.config.js`
- Missing `width` and `height` for static imports
- Using an unsupported image format
- `loader` not configured for external images

## How to Fix

1. Allow external image domains in `next.config.js`:

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      { protocol: 'https', hostname: 'images.example.com' }
    ]
  }
};
module.exports = nextConfig;
```

2. Provide `width` and `height` for static images:

```tsx
import Image from 'next/image';

<Image src="/hero.png" width={800} height={400} alt="Hero" />
```

3. Use a custom loader for non-standard image sources:

```tsx
import Image from 'next/image';

const customLoader = ({ src }) => src;

<Image loader={customLoader} src="https://example.com/pic.jpg" width={200} height={200} />
```

## Examples

```tsx
<Image
  src="https://external-site.com/image.jpg"
  width={400}
  height={300}
  alt="Photo"
/>
```

```text
Error: Invalid src prop (https://external-site.com/image.jpg) on `next/image`,
hostname "external-site.com" is not configured under images in next.config.js
```

## Related Errors

- [Environment variable error]({{< relref "/frameworks/nextjs/env-error" >}})
