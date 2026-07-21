---
title: "DiffUtil Error"
description: "Fix RecyclerView DiffUtil and ListAdapter errors for efficient list updates"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
RecyclerView does not animate changes correctly after DiffUtil update

## Common Causes

- DiffUtil ItemCallback not comparing all fields
- areItemsTheSame returns wrong boolean
- areContentsTheSame comparing by reference
- ListAdapter.submitList called with same reference

## Fixes

- Compare unique IDs in areItemsTheSame
- Compare all fields in areContentsTheSame
- Use data class with proper equals()
- Submit new list instance, not mutated list

## Code Example

```kotlin
class UserDiffCallback : DiffUtil.ItemCallback<User>() {
    override fun areItemsTheSame(oldItem: User, newItem: User): Boolean {
        return oldItem.id == newItem.id
    }

    override fun areContentsTheSame(oldItem: User, newItem: User): Boolean {
        return oldItem == newItem  // Data class equals
    }
}

class UserAdapter : ListAdapter<User, UserViewHolder>(UserDiffCallback()) {
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): UserViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_user, parent, false)
        return UserViewHolder(view)
    }

    override fun onBindViewHolder(holder: UserViewHolder, position: Int) {
        holder.bind(getItem(position))
    }
}

// Update list:
adapter.submitList(newList.toList())
```

# DiffUtil enables item animations
# areItemsTheSame = same logical item
# areContentsTheSame = same content (triggers rebind)
