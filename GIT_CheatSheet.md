# 📝 Git Command Cheat Sheet

## 🌟 Basic Commands
| Command                          | Description                              |
|----------------------------------|-----------------------------------------|
| `git init`                       | Initialize a new Git repository          |
| `git clone <repo-url>`           | Clone an existing repository             |
| `git status`                     | Check the status of your working tree    |
| `git log`                        | View the commit history                  |
| `git diff`                       | Show changes between commits or branches |

---

## 🔄 Branching
| Command                                    | Description                              |
|--------------------------------------------|-----------------------------------------|
| `git branch`                               | List all branches                        |
| `git branch <branch-name>`                 | Create a new branch                      |
| `git checkout <branch-name>`               | Switch to another branch                 |
| `git checkout -b <branch-name>`            | Create and switch to a new branch        |
| `git branch -d <branch-name>`              | Delete a branch                          |
| `git merge <branch-name>`                  | Merge a branch into the current one      |

---

## ✅ Staging & Committing
| Command                          | Description                              |
|----------------------------------|-----------------------------------------|
| `git add <file>`                 | Stage a specific file                    |
| `git add .`                      | Stage all files                          |
| `git commit -m "commit message"` | Commit changes with a message            |
| `git commit -am "commit message"`| Stage and commit all changes             |
| `git reset <file>`               | Unstage a file                           |
| `git reset --hard`               | Discard all local changes                |

---

## 🌐 Pushing & Pulling
| Command                          | Description                              |
|----------------------------------|-----------------------------------------|
| `git push origin <branch-name>`  | Push your branch to the remote repository |
| `git pull origin <branch-name>`  | Pull changes from the remote repository   |
| `git fetch`                      | Fetch changes without merging            |

---

## 🕵️‍♂️ Inspecting
| Command                          | Description                              |
|----------------------------------|-----------------------------------------|
| `git show <commit>`              | Show details of a specific commit        |
| `git blame <file>`               | Show who last modified each line of a file |
| `git log --oneline`              | View a compressed log of commits         |

---

## 🚀 Remote Repositories
| Command                                        | Description                              |
|------------------------------------------------|-----------------------------------------|
| `git remote -v`                                | List remote connections                  |
| `git remote add origin <repo-url>`             | Add a remote repository                  |
| `git remote remove origin`                     | Remove a remote repository               |
| `git push -u origin <branch-name>`             | Push to remote and set as upstream       |

---

## ⚠️ Undoing Changes
| Command                                          | Description                              |
|--------------------------------------------------|-----------------------------------------|
| `git revert <commit>`                            | Create a new commit that undoes changes  |
| `git reset --soft <commit>`                      | Undo commits but keep changes in the staging |
| `git reset --hard <commit>`                      | Completely remove commits and changes    |
| `git checkout -- <file>`                         | Discard changes to a file                |

---

## 🌟 Useful Shortcuts
| Command                          | Description                              |
|----------------------------------|-----------------------------------------|
| `git stash`                      | Stash your changes for later             |
| `git stash apply`                | Reapply stashed changes                  |
| `git stash drop`                 | Remove stashed changes                   |
| `git cherry-pick <commit>`       | Apply the changes from a specific commit |

---