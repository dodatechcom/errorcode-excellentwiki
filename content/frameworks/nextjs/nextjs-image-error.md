---
title: "Next.js Image Component Error"
description: "Next.js Image component raises errors for missing images, unconfigured domains, or layout issues"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The Next.js Image component error occurs when the `<Image>` component cannot load an image, the image source is invalid, or the external image domain is not configured. These errors appear during development or build time.

## Common Causes

- External image domain not whitelisted in `next.config.js`
- Missing `width` and `height` for static imports
- Image file does not exist at the specified path
- Using `layout="fill"` without a parent with `position: relative`
- Invalid image format

## How to Fix

Configure allowed image domains:

```js
// next.config.js
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'example.com',
      },
      {
        protocol: 'https',
        hostname: '*.cdn.example.com',
      },
    ],
  },
};
```

Use the Image component correctly:

```tsx
import Image from 'next/image';

// With static import
import profilePic from '../public/profile.png';

<Image src={profilePic} alt="Profile" width={200} height={200} />

// With remote image
<Image
  src="https://example.com/photo.jpg"
  alt="Photo"
  width={500}
  height={300}
/>
```

Use `layout="fill"` properly:

```tsx
<div style={{ position: 'relative', width: '100%', height: '400px' }}>
  <Image
    src="https://example.com/hero.jpg"
    alt="Hero"
    fill
    style={{ objectFit: 'cover' }}
  />
</div>
```

Use placeholder for loading states:

```tsx
<Image
  src={imageUrl}
  alt="Product"
  width={400}
  height={300}
  placeholder="blur"
  blurDataURL="/placeholder.png"
/>
```

## Examples

```tsx
<Image src="https://unconfigured.com/photo.jpg" alt="Photo" width={100} height={100} />
```

```text
Error: Invalid src prop (https://unconfigured.com/photo.jpg) on `next/image`,
host "unconfigured.com" is not configured under images in `next.config.js`
```

## Related Errors

- [CSS Modules error]({{< relref "/frameworks/nextjs/nextjs-css-modules-error" >}})
- [Build error]({{< relref "/frameworks/nextjs/build-error" >}})
