---
title: "[Solution] Django TemplateDoesNotExist Error — How to Fix"
description: "Fix Django TemplateDoesNotExist errors. Resolve template not found issues with proper directory configuration."
frameworks: ["django"]
error-types: ["configuration-error"]
severities: ["error"]
weight: 5
comments: true
---

A Django TemplateDoesNotExist error occurs when the template engine cannot locate a template file at the specified path. This is one of the most common Django errors and usually indicates a configuration or naming issue in the template lookup process.

## Why It Happens

Django searches for templates in directories defined by the `DIRS` and `APP_DIRS` settings. The error arises when the template filename is misspelled, the template directory is not configured, the app is not included in `INSTALLED_APPS`, or when using multiple template engines with conflicting configurations.

## Common Error Messages

```
TemplateDoesNotExist: home.html
```

```
TemplateDoesNotExist: accounts/login.html
```

```
TemplateDoesNotExist at /profile/
Registration/login.html
```

```
TemplateSyntaxError: Invalid block tag on line 5: 'endfor'
```

## How to Fix It

### 1. Configure Template Directories

Set up the `TEMPLATES` setting with the correct `DIRS` path:

```python
# settings.py
import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 2. Verify App Is in INSTALLED_APPS

When `APP_DIRS` is `True`, Django looks for templates inside each app's `templates/` folder:

```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Your app must be listed here
]
```

### 3. Use Correct Template Path in Views

Ensure the path in `render()` matches the actual file location:

```python
# If template is at: templates/blog/post_list.html
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

# If template is at: myapp/templates/myapp/detail.html
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myapp/detail.html', {'post': post})
```

### 4. Debug Template Loading

Add a template tag to see which directories Django searches:

```html
<!-- Add to any template to debug -->
{% load template_debug %}
{% template_debug %}
```

Or use the shell to check template loading:

```python
from django.template.loader import get_template
try:
    t = get_template('home.html')
    print(f"Template found: {t.origin}")
except Exception as e:
    print(f"Error: {e}")
```

## Common Scenarios

**Scenario 1: Template works in development but not in production.**
This typically occurs because the `templates/` directory is not included in the deployment package. Ensure your deployment configuration includes all template directories, or use `APP_DIRS` with properly installed apps.

**Scenario 2: Template extends a base template that cannot be found.**
When using `{% extends "base.html" %}`, Django looks for `base.html` using the same template loading rules. If `base.html` is in a different directory, use the full path: `{% extends "core/base.html" %}`.

**Scenario 3: Using Jinja2 backend but templates have Django syntax.**
If you have configured a Jinja2 backend but templates use Django template tags like `{% if %}`, they will fail. Ensure the correct backend is used or maintain separate template directories.

## Prevent It

1. **Create a `templates/` directory at the project root** and set `DIRS` to point to it. Keep all project-level templates there, and use app-level `templates/` directories for app-specific templates.

2. **Use consistent naming conventions.** Adopt a pattern like `app_name/template_name.html` for all templates to avoid path confusion.

3. **Run `python manage.py check` after template changes.** This command validates your configuration and can catch some template-related issues before they reach runtime.
