#Find last ok commit with git log
git rebase --exec 'git commit --amend --no-edit -n -S' -i a66a6f7
git push github-uio main --force