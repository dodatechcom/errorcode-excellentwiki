---
title: "[Solution] Django No Reverse Match Error — How to Fix"
description: "Fix Django No reverse match errors. Resolve URL resolution and reverse lookup issues in Django."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

A Django NoReverseMatch error occurs when Django cannot find a URL pattern that matches the given name and arguments during a reverse URL lookup. This typically happens in templates, views, or when using `reverse()` and `redirect()`.

## Why It Happens

Django's URL resolver uses named patterns to generate URLs from view names and arguments. The error is triggered when the view name is misspelled, required positional or keyword arguments are missing, or the URL pattern has been changed without updating all references. It is common after refactoring URL configurations.

## Common Error Messages

```
NoReverseMatch at /home/
Reverse for 'post_detail' with arguments '(1,)' and keyword arguments '{}' not found.
```

```
NoReverseMatch: Reverse for 'user-profile' with keyword arguments '{}' not found.
1 pattern(s) tried: ['profile/(?P<pk>[0-9]+)/$']
```

```
NoReverseMatch at /
Reverse for 'login' not found. 'login' is not a valid view function or pattern name.
```

```
NoReverseMatch: Reverse for 'item-detail' with arguments '(1, 'update')' not found.
```

## How to Fix It

### 1. Use the Correct View Name

Verify that the view name in `reverse()`, `redirect()`, or `{% url %}` matches the name defined in your URL patterns:

```python
# urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('<int:pk>/', views.post_detail, name='post-detail'),
]
```

```python
# In views or forms
from django.urls import reverse

def post_detail_redirect(request, pk):
    return redirect(reverse('blog:post-detail', kwargs={'pk': pk}))
```

```html
<!-- In templates -->
<a href="{% url 'blog:post-detail' pk=post.pk %}">{{ post.title }}</a>
```

### 2. Provide Required Arguments

Ensure all URL parameters are supplied:

```python
# urls.py
path('items/<int:item_id>/edit/', views.edit_item, name='item-edit'),
path('items/<int:item_id>/delete/', views.delete_item, name='item-delete'),
```

```python
# Correct — both arguments provided
url = reverse('item-edit', kwargs={'item_id': 5})

# Correct — using positional args
url = reverse('item-edit', args=[5])

# Wrong — missing item_id
url = reverse('item-edit')  # NoReverseMatch
```

### 3. Use Namespaces Correctly

When using app namespaces, include the namespace prefix:

```python
# project/urls.py
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls', namespace='blog')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
```

```python
# Use namespaced name
reverse('blog:post-detail', kwargs={'pk': 1})

# Wrong — missing namespace
reverse('post-detail', kwargs={'pk': 1})  # NoReverseMatch
```

### 4. Debug URL Resolution

Use the shell to test reverse lookups:

```python
from django.urls import reverse, resolve

# Test reverse lookup
try:
    url = reverse('post-detail', kwargs={'pk': 1})
    print(f"URL: {url}")
except Exception as e:
    print(f"Error: {e}")

# Test forward resolution
match = resolve('/blog/1/')
print(f"View: {match.func}")
print(f"Kwargs: {match.kwargs}")
```

## Common Scenarios

**Scenario 1: Error after renaming a URL pattern.**
When you change the `name` parameter in `urlpatterns`, every reference to the old name in templates, `reverse()`, and `redirect()` must be updated. Use find-and-replace across the project.

**Scenario 2: Error with app namespaces.**
If `app_name` is defined in `urls.py` but the namespace is not included in `include()`, or if you forget to use the namespace prefix in `{% url %}`, Django will raise NoReverseMatch.

**Scenario 3: Dynamic URL generation in templates fails.**
This happens when template variables don't contain the expected values. For example, if `post.pk` is `None` in the template context, `{% url 'post-detail' pk=post.pk %}` will fail.

## Prevent It

1. **Always use namespaced URLs.** Define `app_name` in each app's `urls.py` and use the `namespace` parameter in `include()`. This prevents name collisions and makes URL references explicit.

2. **Run `python manage.py check` and `python manage.py test` regularly.** URL resolution errors are often caught by Django's system checks and test suite.

3. **Use an IDE or editor with Django URL support.** Tools like VS Code with the Django extension can validate URL names in templates and Python code, catching errors before they reach runtime.
