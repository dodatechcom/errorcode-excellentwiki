---
title: "[Solution] Netlify Forms Not Receiving Submissions Error — Fix Form Handling"
description: "Fix Netlify forms not receiving submissions. Resolve form handling configuration, spam filtering, and submission storage issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
weight: 3
---

A Netlify forms not receiving submissions error occurs when your HTML form is configured for Netlify Forms but submissions are not being captured or stored.

## What This Error Means

Netlify automatically detects forms with the `netlify` attribute and processes submissions. When forms do not work, submissions may be silently dropped, blocked by spam filters, or not detected by Netlify's form processing.

## Why It Happens

- The form does not have the `netlify` attribute
- The form action is set to a custom URL instead of Netlify's handler
- JavaScript prevents the form from submitting normally
- The form is behind authentication
- The site has not been redeployed since adding the form
- Spam filter is blocking submissions
- Form uses file uploads which require a different setup

## How to Fix It

### Add Netlify Attribute

```html
<!-- WRONG: Missing netlify attribute -->
<form name="contact" method="POST">
  <input type="text" name="name" />
  <button type="submit">Send</button>
</form>

<!-- RIGHT: Include netlify attribute -->
<form name="contact" method="POST" netlify>
  <input type="text" name="name" />
  <button type="submit">Send</button>
</form>
```

### Use Hidden Form Path

```html
<!-- For form detection to work reliably -->
<form name="contact" method="POST" action="/success" netlify>
  <input type="hidden" name="form-name" value="contact" />
  <input type="text" name="name" />
  <input type="email" name="email" />
  <button type="submit">Send</button>
</form>
```

### Handle JavaScript Forms

```javascript
// For React/Vue/Angular forms
// Include a hidden form for Netlify detection
function ContactForm() {
  return (
    <>
      {/* Hidden form for Netlify to detect */}
      <form name="contact" netlify hidden>
        <input name="name" />
        <input name="email" />
        <input name="message" />
      </form>

      {/* Your JavaScript form */}
      <form onSubmit={handleSubmit}>
        <input name="name" onChange={handleChange} />
        <input name="email" onChange={handleChange} />
        <textarea name="message" onChange={handleChange} />
        <button type="submit">Send</button>
      </form>
    </>
  );
}

// Submit via Netlify API
async function handleSubmit(e) {
  e.preventDefault();
  await fetch('/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      'form-name': 'contact',
      ...formData,
    }).toString(),
  });
}
```

### Enable Spam Filtering

```toml
# netlify.toml
[build.processing]
  skip_processing = false

[build.processing.html]
  pretty_urls = true
```

### Test Form Detection

```bash
# Redeploy after adding the form
git push origin main

# In Netlify Dashboard:
# Forms > Verify the form appears in the list

# Or check with curl
curl -s https://your-domain.com/ | grep 'netlify'
```

### Handle File Uploads

```html
<!-- File uploads require netlify enctype -->
<form name="upload" method="POST" netlify enctype="multipart/form-data">
  <input type="file" name="file" />
  <button type="submit">Upload</button>
</form>
```

## Common Mistakes

- Not redeploying after adding the netlify attribute
- Using JavaScript `fetch` without including the form-name field
- Having multiple forms with the same name attribute
- Not including the hidden form-name input for JS submissions
- Forgetting that Netlify forms only work on published pages

## Related Pages

- [Netlify Functions Error]({{< relref "/tools/netlify/netlify-functions-error" >}}) — Serverless function error
- [Netlify Redirect Error]({{< relref "/tools/netlify/netlify-redirect-error" >}}) — Redirect rules not working
