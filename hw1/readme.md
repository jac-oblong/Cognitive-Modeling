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

### Inverse: (starting with the effect as input parameters and trying to determine the initial conditions)

#### 1. A simple example of an inverse problem would be a metal detector. Current flows through the detector, and when a metal is nearby, its effect can be seen on the current in the detector, allowing it to predict the proximity of the metal. Input parameters would be the current flowing through the detector and the output would be the proximity of the metal (signified by a real metal detector as the beeping frequency). This problem would be simple computationally.

#### 2. Another example of an inverse problem is using the Doppler effect to determine the relative speed of an object, such as a star. Input parameters would include the light spectrum coming from the star. The model could then analyze this spectrum and determine if the light is blue-shifted, and so the star is moving closer, or red-shifted, and so the star is moving away. This problem is more computationally complex than the metal detector, but still seems to be a simple analysis.

#### 3. A third example of an inverse problem would be the process of discovering exoplanets. Various methods are used to determine the presence (and possibly more information) of exoplanets orbiting a given star. Examples include measuring the light intensity of the planet over time, and observing unexpected gravitational effects. Input parameters would include observations of the stars behavior (such as light intensity and position over time). The trends of these values can be analyzed (since we can easily observe the star but cannot observe exoplanets directly) to predict if one or more exoplanets exist orbiting the star. Due to the number of possibly bodies acting on the star (such as multiple exoplanets, other stars, and objects that pass by but don't have stable orbits), the computational complexity of this model is greater than the other two examples, especially if additional information is desired to be predicted (such as number of exoplanets, if multiple, or planet size/type).


### Forward: (starting with the initial conditions as input parameters and trying to determine the effect)

#### 1. The classic example we've been looking at in class is modeling the spread of a disease. Input parameters would involve population size, contacts within the population, the infectivity of the disease, the incubation period of the disease, and possibly more. The computational difficulty of this problem varies based on the complexity of the solution, but simple cases can be modeled using simpler formulas.

#### 2. Another, similar, example of a forward problem is modeling the growth of one or more population(s) in nature. Input parameters would involve starting populations (for each species being measured OR that has an impact on the measured species), reproductive rates (of each species), trends between species (such as if many bunnies are alive, the fox population can grow as more food is available), and more, depending on what other natural phenomenon are observed to have an impact and are chosen to be added to the model. This, again, varies based on the solution complexity, but due to the possible complexity of the network of species interacting, this seems to have a higher complexity than modeling a disease.

#### 3. A third example of a forward problem is modeling and attempting to predict the weather. Input parameters would include all sorts of current conditions, such as temperature, humidity, wind speeds, angle of the sun (time of year), location, geography of the area, and more. Weather is impossible to completely accurately predict, but general estimations can be made, especially for a certain location at a certain time. The models are most accurate early on, then get less accurate as time goes on, and it would make sense to update the current conditions occasionally to obtain a more accurate model. Therefore, modeling the weather would be the most computationally complex of the three examples.


## Problem 3 - Git & GitHub

### Part 1

The [GitHub repository](https://github.com/jac-oblong/Cognitive-Modeling) contains the
team logo, introductory notes, `environment.yml`, and the separate branches for each
team member.

### Part 2

The GitHub repo contains a pull request titled `Example of a merge conflict`. This contains
an example merge conflict and the instructions on how to resolve it.

### Part 3

1. `git restore <path>` will restore the file(s) at `<path>` to the state they are at the 
index/HEAD. For example, after editing a file in a git repo, `git restore <file>` will
discard the changes made. If the changes are staged first, `git restore --staged <file>`
will unstage the changes without discarding them. With the `--source` option, the file
can be restored from any commit.

2. `git checkout <path>` is essentially the same as `git restore` with the main exception
that `git checkout` can also work on branches. This means that to be explicit with what
to checkout, it is better to use `git checkout -- <path>`. Additionally, `git checkout`
does not allow you to choose where the restored files go, as can be done with `git
restore --worktree`.

3. `git reset` can be used to remove commits. For example, say there is repo with 4
commits: `A <- B <- C <- D`. `HEAD` is currently pointing at `D`. `git reset --soft HEAD~2`
would "eject" commits `C` and `D`, and the `HEAD`/branch would now be pointing at `B`.
`--soft` tells git to not touch the staging area of the working directory, `--mixed` will
reset the index, but not the working tree, and `--hard` will reset both.

4. `git revert` creates a new commit that will undo/revert a previous commit. For example,
say there is a repo with a file named `example.txt` that is originally empty. A new commit
is made that adds some content to that file. If that commit is reverted using `git revert`
a new commit will be made that deletes all the contents from the file, so that the file
is empty again.

### Part 4

| Command | Affects Commit History? | Affects Staging Area? | Affects Working Directory? | Typical Use Case |
| ------- | ----------------------- | --------------------- | -------------------------- | --------------- |
| `git reset` | Y | Y | Y | Removing a commit from the history. |
| `git restore` | N | Y | Y | Restoring an unstaged or staged (with `--staged`) file to the state it is at `HEAD` |
| `git rm` | N | Y | Y | Removing a file from the staging area and from the working directory. |

## Problem 4 - Python & NumPy

The python script can be found in the GitHub repo at `hw1/pi.py`. By default, it runs
the estimation of pi for multiple different numbers.

## Problem 5 - Polishing a Repo

As mentioned in the document, a Git repo cannot be inside another Git repo, so this will be submitted seperately.
