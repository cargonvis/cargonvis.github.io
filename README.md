For moving new website from master branch to website branch (for deployment):

### Go to website branch
git checkout website

### Delete current website files
rm -rf css file/ form/ img/ index.html  js/ projects/

### Bring folder with current version from master branch
git checkout master -- bs/current_version_bs/

# Commit the changes
git add .
git status
git commit -m "website update"
git push
