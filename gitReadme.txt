git status
git commit -m "first commit"

This is only necesary when you create a new repository

git remote add origin https://github.com/AlexVillarreal/KamboRefactory.git
git push -u origin master

https://docs.djangoproject.com/en/2.1/intro/tutorial05/
python manage.py startapp polls
Dependencies
pymongo

************************************
git status
git add -A
git commit -m "new update!"
git push -u origin master
************************************

https://stackoverflow.com/questions/2514270/
how-to-check-for-changes-on-remote-origin-git-repository

You could git fetch origin to update the remote branch in your repository to point to the latest version. For a diff against the remote:
git diff origin/master
Yes, you can use caret notation as well.

If you want to accept the remote changes:

git merge origin/master

branck checkout commit

Print out the history of your commits, showing where your branck pointers are and how your history has diverged.

git log --oneline --decorate --graph --all



