---
title: "RecyclerView ViewHolder Error"
description: "Fix RecyclerView ViewHolder creation and binding errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
RecyclerView crashes or shows wrong data because of ViewHolder issues

## Common Causes

- ViewHolder not inflating correct layout
- onBindViewHolder accessing wrong list position
- View not properly initialized in ViewHolder constructor
- ViewHolder recycled but old data displayed

## Fixes

- Inflate correct layout in onCreateViewHolder
- Use getItem(position) instead of direct list access
- Initialize all views in ViewHolder init
- Ensure bind() completely overwrites previous data

## Code Example

```kotlin
class UserViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
    private val nameText: TextView = itemView.findViewById(R.id.nameText)
    private val avatar: ImageView = itemView.findViewById(R.id.avatar)

    fun bind(user: User) {
        nameText.text = user.name
        Glide.with(avatar.context).load(user.avatarUrl).into(avatar)
    }
}

// In adapter:
override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): UserViewHolder {
    val view = LayoutInflater.from(parent.context)
        .inflate(R.layout.item_user, parent, false)
    return UserViewHolder(view)
}

override fun onBindViewHolder(holder: UserViewHolder, position: Int) {
    holder.bind(getItem(position))  // Use ListAdapter's getItem()
}
```

# Use View Binding in ViewHolder for type safety
# Avoid findViewById in modern code
# Use getItem() not direct list access
