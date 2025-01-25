# Homework Assignment 1

## Problem 1 - True-False

## Problem 2 - Inverse vs Forward

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

## Problem 4 - Python & NumPy

## Problem 5 - Polishing a Repo
