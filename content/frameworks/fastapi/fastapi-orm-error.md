---
title: "[Solution] FastAPI ORM Error -- How to Fix"
description: "Fix FastAPI ORM errors. Resolve object-relational mapping issues, session management, and model query problems."
frameworks: ["fastapi"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

A FastAPI ORM error occurs when the object-relational mapping fails due to incorrect model definitions or session lifecycle issues.

## Why It Happens

ORM errors happen due to detached objects, expired attributes, missing session context, or incorrect configurations.

## Common Error Messages

```
DetachedInstanceError: Instance is not bound to a Session
```

```
AttributeError: 'User' object has no attribute 'posts'
```

```
InvalidRequestError: Session's objects have been modified
```

```
sqlalchemy.orm.exc.UnmappedClassError
```

## How to Fix It

### 1. Manage ORM Object Lifecycle

Keep objects within session context.

```python
# Access before closing
user = db.query(User).first()
print(user.email)  # Works
db.close()
```

### 2. Use Eager Loading in Queries

Load related objects within the same query.

```python
@app.get('/users/{user_id}')
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).options(
        joinedload(User.profile),
        selectinload(User.posts)
    ).filter(User.id == user_id).first()
```

### 3. Refresh Objects After Modification

Expire and refresh after changes.

```python
@app.put('/users/{user_id}')
async def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user
```

### 4. Use Pydantic Models for Serialization

Convert ORM to Pydantic.

```python
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

@app.get('/users/{user_id}', response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == user_id).first()
```

## Common Scenarios

**Scenario 1: DetachedInstanceError on relationships.**
Use eager loading.

**Scenario 2: Stale data after update.**
Call `db.refresh(obj)` after commit.

**Scenario 3: ORM object not serializable.**
Use Pydantic with `orm_mode = True`.

## Prevent It

1. **Keep sessions short-lived.**
Create and dispose per request.

2. **Use eager loading by default.**
Load relationships you'll access.

3. **Write model tests.**
Test ORM operations with sessions.

