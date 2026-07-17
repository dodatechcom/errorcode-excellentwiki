---
title: "[Solution] Django Signal Handler Error"
description: "Fix Django signal handler errors. Resolve signal dispatch and handler issues."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A Django signal handler error occurs when a signal handler fails during dispatch. This can cause the entire operation to fail silently or raise an exception.

## Common Causes

- Signal handler raises an unhandled exception
- Recursive signal triggers (saving in post_save causes infinite loop)
- Signal handler not connected properly
- Using `send_robust` vs `send` incorrectly
- Signal handler accessing deleted objects

## How to Fix

### Connect Signal Handler

```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

### Avoid Recursive Saves

```python
@receiver(post_save, sender=Profile)
def update_user(sender, instance, **kwargs):
    # Use update() to avoid triggering post_save again
    User.objects.filter(pk=instance.user_id).update(last_login=now())
```

### Use send_robust for Error Handling

```python
from django.dispatch import Signal
my_signal = Signal()

# send_robust catches exceptions in handlers
responses = my_signal.send_robust(sender=MyModel, instance=obj)
```

### Check Signal Registration

```python
# In apps.py
class MyAppConfig(AppConfig):
    def ready(self):
        import myapp.signals
```

## Examples

```python
# Example 1: Recursive save
@receiver(post_save, sender=Profile)
def bad_handler(sender, instance, **kwargs):
    instance.save()  # Infinite loop!
# Fix: use User.objects.filter().update()

# Example 2: Signal not connected
# Fix: ensure AppConfig.ready() imports signals
```

## Related Errors

- [Django Transaction Error]({{< relref "/frameworks/django/django-transaction-error" >}}) — TransactionManagementError
- [Django Settings Error]({{< relref "/frameworks/django/django-settings-error" >}}) — ImproperlyConfigured
