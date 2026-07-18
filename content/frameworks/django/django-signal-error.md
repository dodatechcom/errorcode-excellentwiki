---
title: "[Solution] Django Signal Handler Error — How to Fix"
description: "Fix Django signal handler errors. Resolve signal connection issues, dispatch failures, and async signal problems."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

A Django signal handler error occurs when a signal is not connected properly, the handler raises an exception, or the signal is dispatched before the receiver is ready. Signals in Django rely on correct imports and connection timing.

## Why It Happens

Django signals use a publish-subscribe pattern where senders dispatch signals and receivers handle them. Errors occur when the `receiver` decorator is used on the wrong function, when signal connections are made before the app is fully loaded, when handlers raise unhandled exceptions, or when signal modules are imported too early in the startup process.

## Common Error Messages

```
TypeError: post_save() got an unexpected keyword argument 'signal'
```

```
AttributeError: 'AppRegistryNotReady: Models aren't loaded yet.'
```

```
signal.post_save.connect receiver not callable
```

```
RuntimeError: signal handler raised an exception
```

## How to Fix It

### 1. Use the @receiver Decorator Correctly

Always import `receiver` from `django.dispatch` and connect to the correct signal:

```python
# signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
```

### 2. Import Signals in App Config

Connect signals in the app's `AppConfig.ready()` method to ensure proper loading:

```python
# apps.py
from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        import blog.signals  # noqa: F401
```

### 3. Handle Exceptions in Signal Handlers

Always wrap handler logic in try-except blocks to prevent signal failures from breaking the main operation:

```python
@receiver(post_save, sender=Article)
def update_search_index(sender, instance, created, **kwargs):
    try:
        if created:
            SearchIndex.add(instance)
        else:
            SearchIndex.update(instance)
    except SearchIndexError as e:
        logger.error(f"Failed to update search index for {instance}: {e}")
        # Optionally queue for retry
```

### 4. Use Proper Signal Arguments

Signal handlers must accept `sender` and `**kwargs`:

```python
@receiver(post_save, sender=Order)
def process_order(sender, instance, created, raw, using, **kwargs):
    """
    sender: The model class (Order)
    instance: The actual Order instance
    created: Boolean — True if a new record was inserted
    raw: Boolean — True if saved with raw=True (loaddata)
    using: Database alias being used
    """
    if not created or raw:
        return  # Only process new, non-raw saves

    OrderProcessor.process(instance)
```

## Common Scenarios

**Scenario 1: Signal handler runs but doesn't affect the database.**
This happens when the handler modifies objects without calling `save()`, or when it operates on a different database alias. Ensure `using=instance._state.db` is passed to queries if using multiple databases.

**Scenario 2: Signal causes infinite loop.**
When a signal handler saves the same model that triggered it, it creates a recursive loop. Use a flag or check to prevent re-entry:

```python
@receiver(post_save, sender=Profile)
def update_profile_timestamp(sender, instance, **kwargs):
    if not hasattr(instance, '_updating'):
        instance._updating = True
        instance.last_synced = timezone.now()
        instance.save(update_fields=['last_synced'])
```

**Scenario 3: Signals not firing in tests.**
Django's test runner wraps each test in a transaction that is rolled back. Signals fire but their effects are lost. Use `TransactionTestCase` instead of `TestCase` when testing signal behavior.

## Prevent It

1. **Keep signal handlers thin.** Move complex logic to service functions and call them from the handler. This makes testing and debugging easier.

2. **Always import signals in `AppConfig.ready()`.** This ensures handlers are connected exactly once and only after all models are loaded.

3. **Test signal handlers independently.** Write unit tests that directly call the handler function rather than relying on signal dispatch, which gives you more control over test scenarios.
