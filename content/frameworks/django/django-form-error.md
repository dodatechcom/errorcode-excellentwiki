---
title: "[Solution] Django Form Validation Error"
description: "Fix Django form validation errors. Resolve form.is_valid() failures."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["form", "validation", "clean", "is_valid", "django"]
weight: 5
---

A Django form validation error occurs when `form.is_valid()` returns False due to invalid input data. The form contains errors that must be resolved before processing.

## Common Causes

- Required fields are missing or empty
- Data does not match field validators (email, URL, etc.)
- Custom `clean_<field>()` methods raise ValidationError
- Data type mismatches (string where integer expected)
- File upload validation failed

## How to Fix

### Check Form Errors

```python
if not form.is_valid():
    print(form.errors)
    # {'email': ['Enter a valid email address.']}
```

### Display Errors in Template

```html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Submit</button>
</form>
```

### Custom Validation

```python
class MyForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered")
        return email
```

### Validate Single Field

```python
form = MyForm(data={'email': 'invalid'})
form.is_valid()
print(form.errors)
```

## Examples

```python
# Example 1: Missing required field
form = RegistrationForm(data={'username': ''})
form.is_valid()  # False
form.errors  # {'username': ['This field is required.']}

# Example 2: Custom validation
def clean_age(self):
    age = self.cleaned_data.get('age')
    if age < 0:
        raise forms.ValidationError("Age cannot be negative")
    return age
```

## Related Errors

- [Django Template Error]({{< relref "/frameworks/django/django-template-error" >}}) — template rendering error
- [Django CSRF Error]({{< relref "/frameworks/django/django-csrf-error" >}}) — CSRF verification failed
