---
title: "Flask-Admin Error"
description: "Flask-Admin raises errors related to admin panel configuration, model views, and authentication"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Flask-Admin errors occur when the admin panel encounters issues with model registration, view configuration, or permission handling. These errors typically manifest during admin panel initialization or when performing CRUD operations through the admin interface.

## Common Causes

- Model not registered with admin view
- Missing or incorrect column definitions
- Authentication not configured for admin access
- Custom view not inheriting from `ModelView`
- Database session issues in admin operations

## How to Fix

Set up admin with proper model views:

```python
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

admin = Admin(app, name='My Admin', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
```

Secure admin with authentication:

```python
from flask_admin import AdminIndexView, expose
from flask_login import current_user

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated or not current_user.is_admin:
            return redirect(url_for('login'))
        return super().index()

admin = Admin(app, name='Admin', index_view=MyAdminIndexView())
```

Customize model views:

```python
class UserAdmin(ModelView):
    column_list = ['id', 'username', 'email', 'created_at']
    column_searchable_list = ['username', 'email']
    column_filters = ['is_admin']
    form_columns = ['username', 'email', 'is_admin']

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.created_at = datetime.utcnow()

admin.add_view(UserAdmin(User, db.session))
```

## Examples

```python
admin = Admin(app)
admin.add_view(ModelView(User, db.session))
# User model must have __tablename__ defined
```

```text
sqlalchemy.exc.InvalidRequestError: When initializing mapper ... failed to locate a mapped class for ...
```

## Related Errors

- [SQLAlchemy error]({{< relref "/frameworks/flask/sqlalchemy-error" >}})
- [Login error]({{< relref "/frameworks/flask/flask-login-error" >}})
