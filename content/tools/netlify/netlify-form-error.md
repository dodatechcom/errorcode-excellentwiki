---
title: "[Solution] Netlify Form Submission Not Received Error — How to Fix"
description: "Fix Netlify form submissions not being received. Resolve form detection failures, spam filtering, and submission handling issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Netlify form submission not received error occurs when your HTML form is properly configured for Netlify Forms but submissions are not captured, stored, or appear in the dashboard.

## What This Error Means

Netlify automatically detects forms with the `netlify` attribute during the build process and sets up form handling. When submissions are not received, it usually means the form was not detected, JavaScript intercepted the submission, or spam filtering is blocking entries.

## Why It Happens

- The form does not have the `netlify` attribute on the `<form>` tag
- JavaScript prevents the default form submission (e.g., `e.preventDefault()`)
- The form is behind authentication that Netlify's crawler cannot access
- The site was not redeployed after adding the form
- Spam filter is categorizing submissions as spam
- The form action points to a custom URL instead of Netlify's handler
- Multiple forms share the same `name` attribute
- The form is rendered by JavaScript after page load (SPA)

## Common Error Messages

- `Form not detected` — The build did not find a form with the netlify attribute
- `Submission not found` — The form submission could not be processed
- `Spam submission blocked` — The submission was flagged by spam protection
- `Netlify Forms requires a redeploy` — Form was added but site not redeployed

## How to Fix It

### Ensure Proper Form Configuration

```html
<!-- Basic Netlify form -->
<form name="contact" method="POST" netlify>
  <input type="hidden" name="form-name" value="contact" />
  <input type="text" name="name" placeholder="Name" required />
  <input type="email" name="email" placeholder="Email" required />
  <textarea name="message" placeholder="Message" required></textarea>
  <button type="submit">Send</button>
</form>
```

### Fix JavaScript-Intercepted Forms

```javascript
// React/Vue form — add hidden form for Netlify detection
function ContactForm() {
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Use fetch to submit to Netlify's handler
    const response = await fetch('/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        'form-name': 'contact',
        name: formData.name,
        email: formData.email,
        message: formData.message,
      }).toString(),
    });

    if (response.ok) {
      setSubmitted(true);
    }
  };

  return (
    <>
      {/* Hidden form for Netlify detection */}
      <form name="contact" netlify hidden>
        <input name="name" />
        <input name="email" />
        <input name="message" />
      </form>

      {/* Your React form */}
      <form onSubmit={handleSubmit}>
        <input name="name" onChange={handleChange} />
        <input name="email" onChange={handleChange} />
        <textarea name="message" onChange={handleChange} />
        <button type="submit">Send</button>
      </form>
    </>
  );
}
```

### Enable Spam Filtering

```html
<!-- Add honeypot field to catch bots -->
<form name="contact" method="POST" netlify netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="contact" />
  <p hidden>
    <label>Don't fill this out: <input name="bot-field" /></label>
  </p>
  <input type="text" name="name" required />
  <input type="email" name="email" required />
  <textarea name="message" required></textarea>
  <button type="submit">Send</button>
</form>
```

### Verify Form Detection

```bash
# Redeploy after adding forms
git push origin main

# Check the deployed HTML for form detection
curl -s https://your-domain.com/ | grep -i 'netlify'

# In Netlify Dashboard: Forms > Verify form appears in list
# If the form is not listed, the netlify attribute may be missing
```

### Handle File Upload Forms

```html
<!-- File upload forms require specific configuration -->
<form name="upload" method="POST" netlify enctype="multipart/form-data">
  <input type="hidden" name="form-name" value="upload" />
  <input type="file" name="file" />
  <button type="submit">Upload</button>
</form>
```

### Check Form Limits

```bash
# Netlify forms have these limits:
# - Free: 100 submissions/month, 100 MB storage
# - Pro: 25,000 submissions/month, 10 GB storage
# - Business: 100,000 submissions/month, 100 GB storage

# Check current usage via API
curl -X GET "https://api.netlify.com/api/v1/sites/SITE_ID/forms" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" | jq '.[] | {name, submission_count}'
```

### Test Form Submissions

```bash
# Test form submission via curl
curl -X POST https://your-domain.com/ \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "form-name=contact&name=Test+User&email=test@example.com&message=Hello"

# Check Netlify Dashboard for the submission
# Dashboard > Forms > Submissions
```

## Common Scenarios

- **SPA form detection:** A single-page application renders the form with JavaScript after page load. Netlify's build-time crawler cannot detect dynamically rendered forms.
- **Form behind login:** The form is on a protected page, and Netlify's crawler cannot access it during the build. The form is never registered.
- **Duplicate form names:** Two forms share the same `name` attribute. Only one form is registered, and submissions from the other are lost.

## Prevent It

1. Always include a hidden `form-name` input field matching the `name` attribute on the form tag
2. Verify form detection in the Netlify Dashboard after each deployment before relying on form submissions
3. Use the `netlify-honeypot` attribute with a hidden honeypot field to reduce spam without impacting legitimate users

## Related Pages

- [Netlify Form Error]({{< relref "/tools/netlify/netlify-form-error" >}}) — Form handling issues
- [Netlify Identity Error]({{< relref "/tools/netlify/netlify-identity-error" >}}) — Identity auth failed
