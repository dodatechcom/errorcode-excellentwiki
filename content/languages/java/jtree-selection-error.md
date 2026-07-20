---
title: "[Solution] Java JTree — Selection Error"
description: "Fix JTree selection errors by checking TreeSelectionModel, handling selection events, and verifying TreePath validity."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 27
---

# JTree — Selection Error

Errors related to `JTree` selection occur when the `TreeSelectionModel` is misconfigured, selection paths are invalid, or selection event handling causes unexpected behavior.

## Description

`JTree` uses a `TreeSelectionModel` to manage which nodes are selected. Errors arise when invalid `TreePath` objects are used, when selection mode is incompatible with the operation, or when `TreeSelectionListener` modifies the selection during notification causing `IllegalStateException`.

Common message variants:

- `NullPointerException: TreePath is null`
- `IllegalStateException: Invalid tree path — node not in tree`
- `IllegalArgumentException: unsupported selection mode`
- `ConcurrentModificationException during selection event handling`
- `IllegalStateException: path not found in tree model`

## Common Causes

```java
// Cause 1: Null TreePath passed to setSelectionPath
tree.setSelectionPath(null);  // NullPointerException

// Cause 2: TreePath to node not in the model
TreePath path = new TreePath(new Object[]{root, nodeA, nodeB});
tree.setSelectionPath(path);  // IllegalArgumentException — node not in tree

// Cause 3: Modifying selection inside TreeSelectionListener
tree.addTreeSelectionListener(e -> {
    tree.clearSelection();  // Re-entrant — IllegalStateException
});

// Cause 4: Wrong selection mode for multi-selection
tree.getSelectionModel().setSelectionMode(
    TreeSelectionModel.SINGLE_TREE_SELECTION);
tree.setSelectionPaths(new TreePath[]{path1, path2});  // Only first path set

// Cause 5: Accessing selected node when nothing selected
TreePath selected = tree.getSelectionPath();
selected.getPathComponent(0);  // NPE — nothing selected
```

## Solutions

### Fix 1: Validate TreePath before selection

```java
import javax.swing.tree.TreePath;

public class SafeTreeSelection {
    private final javax.swing.JTree tree;

    public SafeTreeSelection(javax.swing.JTree tree) {
        this.tree = tree;
    }

    public void selectNode(Object node) {
        TreePath path = findPathForNode(node);
        if (path != null) {
            tree.setSelectionPath(path);
            tree.scrollPathToVisible(path);
        }
    }

    private TreePath findPathForNode(Object node) {
        javax.swing.tree.DefaultTreeModel model =
            (javax.swing.tree.DefaultTreeModel) tree.getModel();
        javax.swing.tree.TreeNode rootNode =
            (javax.swing.tree.TreeNode) model.getRoot();
        return findPath(rootNode, node);
    }

    private TreePath findPath(javax.swing.tree.TreeNode current, Object target) {
        if (current.toString().equals(target.toString())) {
            return new TreePath(
                ((javax.swing.tree.DefaultMutableTreeNode) current).getPath());
        }
        for (int i = 0; i < current.getChildCount(); i++) {
            TreePath result = findPath(current.getChildAt(i), target);
            if (result != null) {
                return result;
            }
        }
        return null;
    }
}
```

### Fix 2: Check selection before accessing selected node

```java
import javax.swing.JTree;
import javax.swing.tree.TreePath;
import javax.swing.tree.DefaultMutableTreeNode;

public class SafeSelectionAccess {
    public static DefaultMutableTreeNode getSelectedNode(JTree tree) {
        TreePath path = tree.getSelectionPath();
        if (path == null) {
            return null;
        }
        Object lastPath = path.getLastPathComponent();
        if (lastPath instanceof DefaultMutableTreeNode) {
            return (DefaultMutableTreeNode) lastPath;
        }
        return null;
    }

    public static void handleSelection(JTree tree) {
        DefaultMutableTreeNode node = getSelectedNode(tree);
        if (node != null) {
            System.out.println("Selected: " + node.getUserObject());
        }
    }
}
```

### Fix 3: Use correct selection mode

```java
import javax.swing.JTree;
import javax.swing.tree.TreeSelectionModel;

public class TreeSelectionMode {
    public static void configureSelectionMode(JTree tree, boolean allowMulti) {
        if (allowMulti) {
            tree.getSelectionModel().setSelectionMode(
                TreeSelectionModel.DISCONTIGUOUS_TREE_SELECTION);
        } else {
            tree.getSelectionModel().setSelectionMode(
                TreeSelectionModel.SINGLE_TREE_SELECTION);
        }
    }
}
```

### Fix 4: Avoid modifying selection inside listener

```java
import javax.swing.JTree;
import javax.swing.event.TreeSelectionEvent;
import javax.swing.event.TreeSelectionListener;
import javax.swing.tree.TreePath;

public class SafeSelectionListener implements TreeSelectionListener {
    private final JTree tree;
    private boolean updating = false;

    public SafeSelectionListener(JTree tree) {
        this.tree = tree;
    }

    @Override
    public void valueChanged(TreeSelectionEvent e) {
        if (updating) {
            return;
        }
        updating = true;
        try {
            TreePath path = tree.getSelectionPath();
            if (path != null) {
                handleNodeSelected(path);
            }
        } finally {
            updating = false;
        }
    }

    private void handleNodeSelected(TreePath path) {
        Object node = path.getLastPathComponent();
        System.out.println("Selected: " + node);
    }
}
```

### Fix 5: Expand and select with path validation

```java
import javax.swing.JTree;
import javax.swing.tree.TreePath;
import javax.swing.tree.DefaultMutableTreeNode;

public class TreeExpander {
    public static void selectAndExpand(JTree tree, TreePath path) {
        if (path == null) {
            return;
        }

        // Expand all parent paths
        for (int i = 0; i < path.getPathCount() - 1; i++) {
            TreePath parentPath = path.getParentPath();
            tree.expandPath(path);
            if (parentPath == null) break;
            path = parentPath;
        }

        // Select and scroll to the target node
        tree.setSelectionPath(path);
        tree.scrollPathToVisible(path);
    }

    public static void expandAll(JTree tree) {
        for (int row = 0; row < tree.getRowCount(); row++) {
            tree.expandRow(row);
        }
    }
}
```

## Prevention Checklist

- Always check `tree.getSelectionPath()` for null before accessing selected nodes.
- Use `findPathForNode()` to create valid `TreePath` objects.
- Set `TreeSelectionModel` to the correct mode (`SINGLE` or `DISCONTIGUOUSOUS`).
- Use a boolean flag to prevent re-entrant selection event handling.
- Scroll the tree to the selected node with `scrollPathToVisible()` after selection.
- Expand parent nodes before selecting deep children.

## Related Errors

- [NullPointerException](../nullpointerexception) — null TreePath or no selection.
- [IllegalArgumentException](../illegalargumentexception) — invalid selection mode.
- [IllegalStateException](../illegalstateexception) — modifying selection during event.
- [IndexOutOfBoundsException](../indexoutofboundsexception) — row index out of range.
