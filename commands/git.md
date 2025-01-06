### Git Commands 👩🏻‍💻

Git config set uname and pwd
```shell
git config --global user.name "kj"
git config --global user.email "kj@email.com"
# set credentials (mac)
git config --global credential.helper osxkeychain
```
after any push, pull, clone cmd prompt appears for setting uname and pwd then set uname and pwd (your git auth token)

Git clone
```shell
git clone <repo>
```

Git add
```shell
git add <file_or_dir> 
# add all
git add .
# add untracted 
git add -u
```

Git commit
```shell
git commit -m "commit message"
```

Git push
```shell
# git push <remote> <branch>
git push origin main
```

Git pull
```shell
# rebase if wanted merge commit
git pull --rebase <remote>
```

Git fetch
```shell
# use <branch> if needed
git fetch <remote> <branch>
```

Git merge
```shell
git merge <new-feature>
```

Git branch
```shell
# navigate to branch
git checkout <branch_name>
# create new branch and switch to it
git checkout -b <new_branch_name>
# list out branch
git branch -r
# delete remote
git push -d <remote_name> <branchname>   
# delete local
git branch -d <branchname>               
```

Git status
```shell
git status
```

Git stash: saved working dir locally
```shell
# stash untracted files or dir
git stash -u
# stash last changes
git stash pop
# with id
git stash pop stash@{2}
# apply stash chages
git stash apply
# stash list
git stash list
# save 
git stash save "message"
# show diff (-p to see full detail)
git stash show
# drop particular stash with id
git stash drop stash@{1}
# clear stash
git stash clear
```

