---
title: "ValidationError: form validation failed"
description: "Django raises ValidationError when form data does not meet the validation constraints"
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["forms", "validation", "clean", "input"]
weight: 5
---

This error occurs when Django form validation fails because the submitted data does not match the field constraints. Django's form system automatically validates fields based on their type and configuration.

## Common Causes

- Missing required fields
- Invalid email format, URL, or integer type
- Custom `clean_*` methods raising `ValidationError`
- Form data does not match model field constraints

## How to Fix

1. Add proper error handling in the view:

```python
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the data
            pass
        else:
            # Re-render form with errors
            return render(request, "register.html", {"form": form})
    return render(request, "register.html", {"form": RegistrationForm()})
```

2. Define custom clean methods with proper validation:

```python
from django import forms

class RegistrationForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use")
        return email
```

3. Display errors in the template:

```html
<form method="post">
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

## Examples

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

form = ContactForm(data={"name": "", "email": "invalid"})
form.is_valid()  # False
form.errors
# {'name': ['This field is required.'], 'email': ['Enter a valid email address.']}
```

## Related Errors

- [FieldError]({{< relref "/frameworks/django/orm-error" >}})
