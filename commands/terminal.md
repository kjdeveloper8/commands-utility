### Terminal Commands (mac) 👩🏻‍💻

Install pkgs
```shell 
brew install <pkg_name>
```

List out installed pkg
```shell
brew info --installed --json |grep '<pkg_name>'
```

print tree (`brew install tree` if needed)
```shell
tree -I "node_modules|bower_components" | sed 's/├/\+/g; s/─/-/g; s/└/\\/g'
```

brew search pkg 
```zsh
brew search postgresql | grep -E '^postgresql(@.*)?$'
```

brew info
```zsh
brew info <pkg>
```

change directory
```zsh
cd
```

list directory
```zsh
ls
```

copy
```zsh
# copy file 
cp <filename> <dir-path>
# copy contents of a folder to a new folder (V: for verbose)
ditto -V <directory> <new-directory> 
```

move
```zsh
mv <filename> <move-to-path>
```

create empty/blank file
```zsh
touch <filename>
# multiple empty file
touch <filename1> <filename2> <filename3>
```

directory
```zsh
# make directory
mkdir <dir-name>
# remove if not empty or nested
rmdir -r <dir-name> 
# rename
mv <old-filename> <new-filename>
```

get one line description of command
```zsh
whatis <cmd-name>
```

count file and folder within subdirectory
```zsh
find <path> -type f | wc -l
```
