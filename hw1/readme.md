# Homework Assignment 1

## Problem 1 - True-False

### 1. Stochastic models will always produce the same output x given the same input parameters θ.

This is FALSE, stochastic models implement random variation, leading to different outputs even when given the same input.

### 2. In psychology, replicability refers to obtaining consistent results using the same data and analysis methods, while reproducibility refers to obtaining consistent results by conducting a new study with different data under similar conditions.

This is FALSE, these definitions are switched. Replicability, in psychology, refers to obtaining a similar result through a new study. Reproducibility, in psychology, refers to running the same experiment with the same data and achieving the smae results.

### 3. In Python, the expression 5 + "5" will result in a TypeError.

This is TRUE.

### 4. The git rebase command is used to squash commits in the history, but it cannot be used to reapply commits on top of a different base branch.

This is FALSE, a <branch> can be specified to automatically switch branches before reapplying the commits.

(NOTE: double-check)

### 5. A detached HEAD state in Git means you are no longer on any branch and cannot commit changes until you switch back to a branch.

This is TRUE.

### 6. Function arguments in Python are passed by reference, meaning that modifying a mutable object within a function will also modify it outside the function scope.

This is TRUE.

### 7. Using the is operator in Python checks for value equality, similar to the == operator.

This is FALSE, the "is" operator in Python checks if two objects are the same, which is a higher level of equality than a value equality check. For example:
```python
x = [3]
y = [3]
x == y   # this will return true, they have the same value
x is y   # this will return false, they are different objects
```

### 8. The .gitignore file in a Git repository is used to specify files that should not be tracked by Git and cannot be overridden by a user.

This is FALSE. While it is true that the .gitignore file specifies files that should not be tracked, a user CAN edit it to allow/disallow a different selection of files.

(NOTE: is this what the question is asking?)

## Problem 2 - Inverse vs Forward

## Problem 3 - Git & GitHub

## Problem 4 - Python & NumPy

## Problem 5 - Polishing a Repo

As mentioned in the document, a Git repo cannot be inside another Git repo, so this will be submitted seperately.
