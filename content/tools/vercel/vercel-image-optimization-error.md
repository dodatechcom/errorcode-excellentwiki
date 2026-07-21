---
title: "[Solution] Vercel Image Optimization Error"
description: "Fix Vercel image optimization errors when Next.js Image component fails."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel Image Optimization Error

Vercel image optimization fails to process images.

```
Error: Invalid src prop on next/image
```

## Common Causes

- Image domain not configured
- External image URL not accessible
- Image format not supported
- Missing next.config.js configuration
- Image size exceeds limits

## How to Fix

### Configure Image Domains

```javascript
// next.config.js
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**.example.com',
      },
    ],
    formats: ['image/avif', 'image/webp'],
  },
};
```

### Use Local Images

```typescript
import Image from 'next/image';

// Static import
import photo from '../public/photo.jpg';

export default function Page() {
  return <Image src={photo} alt="Photo" width={500} height={300} />;
}
```

### Handle External Images

```typescript
// For external images, configure allowed domains
<Image
  src="https://cdn.example.com/photo.jpg"
  alt="Photo"
  width={800}
  height={600}
  unoptimized  // Skip optimization if needed
/>
```

### Check Image URL

```bash
# Test image URL accessibility
curl -I https://cdn.example.com/photo.jpg
```

### Disable Optimization

```javascript
// next.config.js
module.exports = {
  images: {
    unoptimized: true  // Disable for all images
  }
};
```

## Examples

```typescript
// Proper Image usage
import Image from 'next/image';

export default function Gallery() {
  const images = [
    { src: '/photo1.jpg', alt: 'Photo 1' },
    { src: '/photo2.jpg', alt: 'Photo 2' },
  ];

  return (
    <div>
      {images.map((img) => (
        <Image
          key={img.src}
          src={img.src}
          alt={img.alt}
          width={400}
          height={300}
          priority
        />
      ))}
    </div>
  );
}
```
