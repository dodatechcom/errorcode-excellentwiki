---
title: "React component composition errors"
description: "Errors related to poor component composition patterns in React. This includes components that are too large, have too many responsibilities, or don't follow the single responsibility principle."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["warning", "composition", "architecture", "patterns"]
severity: "warning"
solution: "Break large components into smaller, focused components. Use composition over inheritance. Implement render props or HOCs for reusable logic. Follow the single responsibility principle for components."
---

Errors related to poor component composition patterns in React. This includes components that are too large, have too many responsibilities, or don't follow the single responsibility principle.

## Solution

Break large components into smaller, focused components. Use composition over inheritance. Implement render props or HOCs for reusable logic. Follow the single responsibility principle for components.

## Code Example

```javascript
  // BAD: Component doing too much
  function UserProfile({ userId }) {
    const [user, setUser] = useState(null);
    const [posts, setPosts] = useState([]);
    const [comments, setComments] = useState([]);
    const [isEditing, setIsEditing] = useState(false);
    
    useEffect(() => {
      fetchUser(userId).then(setUser);
      fetchPosts(userId).then(setPosts);
      fetchComments(userId).then(setComments);
    }, [userId]);
    
    return (
      <div>
        {user && (
          <>
            <h1>{user.name}</h1>
            <p>{user.email}</p>
            {isEditing ? (
              <EditForm user={user} onSave={() => setIsEditing(false)} />
            ) : (
              <button onClick={() => setIsEditing(true)}>Edit</button>
            )}
            <h2>Posts</h2>
            <ul>
              {posts.map(post => (
                <li key={post.id}>{post.title}</li>
              ))}
            </ul>
            <h2>Comments</h2>
            <ul>
              {comments.map(comment => (
                <li key={comment.id}>{comment.text}</li>
              ))}
            </ul>
          </>
        )}
      </div>
    );
  }
  
  // GOOD: Composed from smaller components
  function UserProfile({ userId }) {
    return (
      <UserProfileLayout userId={userId}>
        <UserInfo />
        <UserPosts />
        <UserComments />
      </UserProfileLayout>
    );
  }
  
  function UserProfileLayout({ userId, children }) {
    const [user, setUser] = useState(null);
    
    useEffect(() => {
      fetchUser(userId).then(setUser);
    }, [userId]);
    
    if (!user) return <Loading />;
    
    return (
      <UserContext.Provider value={user}>
        <div className="profile">
          {children}
        </div>
      </UserContext.Provider>
    );
  }
  
  function UserInfo() {
    const user = useContext(UserContext);
    const [isEditing, setIsEditing] = useState(false);
    
    return (
      <div>
        <h1>{user.name}</h1>
        <p>{user.email}</p>
        {isEditing ? (
          <EditForm user={user} onSave={() => setIsEditing(false)} />
        ) : (
          <button onClick={() => setIsEditing(true)}>Edit</button>
        )}
      </div>
    );
  }
```
