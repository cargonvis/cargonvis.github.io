For moving new website from master branch to website branch (for deployment):

### Go to origin branch (master)
git checkout master

### Copy desired folders to different location
cp -r bs/current_version_bs/. ~

### Go to destination branch (website)
git checkout website

### Delete current website files
rm -rf css file/ form/ img/ index.html  js/ projects/

### Move folders from previously selected location
mv ~/css/ ~/file/ ~/form/ ~/img/ ~/index.html ~/js/ ~/projects/ ~/my_portfolio/

### Commit the changes
git add .
git status
git commit -m "website update"
git push
