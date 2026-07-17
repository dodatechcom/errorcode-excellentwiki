---
title: "FieldError: cannot resolve keyword"
description: "Django ORM raises FieldError when a query references a field or related field that does not exist"
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Django's ORM encounters a field name in a query that does not exist on the model, or when a related field lookup references a nonexistent relationship.

## Common Causes

- Typo in the field name in `.filter()` or `.order_by()`
- Referencing a related field without the correct `related_name`
- Using a field from a related model without double underscores
- Querying a model that has not been migrated yet

## How to Fix

1. Check the model definition for the correct field name:

```python
class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# Correct
Article.objects.filter(author__email="test@example.com")

# Wrong — field does not exist
Article.objects.filter(auther__email="test@example.com")
```

2. Use `select_related` or `prefetch_related` for related field lookups:

```python
Article.objects.select_related('author').filter(author__email="test@example.com")
```

3. Verify the migration is applied:

```bash
python manage.py migrate
```

4. Check available fields dynamically:

```python
Article._meta.get_fields()
```

## Examples

```python
Article.objects.filter(authors__name="Alice")
# django.core.exceptions.FieldError: Cannot resolve keyword 'authors' into field.
```

```text
FieldError: Cannot resolve keyword 'authors' into field. Choices are: author, id, title
```

## Related Errors

- [Migration error]({{< relref "/frameworks/django/migration-error" >}})
