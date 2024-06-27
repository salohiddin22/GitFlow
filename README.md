# This is a flow of creating & managing repos in GitHub

## Part 1: Creating and setting-up a new repo


### Step #1
Create a new repo from your Web-based GitHub account.

### Step #2

Clone your online repository on your local machine by. 
```
git clone git@github.com:username/Repo-Name.git

```

And enter the repo directory in your local machine by. 

```
cd Repo-Name/
```

Here you can create/bring any files you want.

### Step #3
```
git status  (to show all the updated files)

git add <file name> <file name>  (if you wanna add one or more files)
git add *  (if you wanna add all files)
git status

git restore --staged *  (to reverse all the changes you made) 

git commit -m "text of the msg"
```

### Step #3.x

If there is an error appers regarding your account when you do "git commit", watch [this video](https://youtu.be/3wAaPNxgLHI?si=Yarxhgsj25RTkMHI) on how to create and add SHH for GitHub.


### Step #4
```
git status
git push  (to push the changes to your online repo)
git status
```

And the last step: check if your online repo is synced up.


## Part 2:  Updating existing filesfiles & creating branches

### Step#1
Check the branch & create new one by
```
git branch
git checkout -b NewBranch
git branch
```

### Step#2: You can make changes now. After changing

```
git status
git diff <file name>
git push --set-upstream origin NewBranch 
git add <file name>
git commit -m "text of the msg"
git push
```

### Step#3: Visit GitHub and merge the branches, and delete that NewBranch. Then on you terminal

```
git checkout main
git pull (to make sure you are up-to-date with main branch)
git branch -d NewBranch (to delete the unnecessary branch on your local)
git status
```


### GitHub tutorial resources:

1. [Git & GitHub repo set-up for beginners](https://youtu.be/jTHhMSxQTNI?si=dyrvXEz_c0iR-hky)
2. [The git flow](https://youtu.be/zTgXYR4PZ04?si=u3kfzdwt7Q7TRJoU)
3. [Create and Add SSH Key to GitHub in Ubuntu](https://youtu.be/3wAaPNxgLHI?si=Yarxhgsj25RTkMHI)
