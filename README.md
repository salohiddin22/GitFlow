# This is flow of creating & managing repos in GitHub
### Step #1
Create new repo from your Web-based GitHub account

### Step #2

Clone your online repository on your local machine by 
```
git clone git@github.com:salohiddin22/PCA-analysis.git

```

And enter the repo directory in your local machine by cd PCA-analysis/

Create/bring any files as you want

### Step #3
```
git status  > shows all the updated files

git add <file name> <file name>  (if you wanna add one or more files)
git add *  (if you wanna add all files)
git status

git restore --staged *  (reverses all the changes you made) 

git commit -m "text of the msg"
```

### Step #3.x

If there is error regarding your account appers when git commit watch [this video](https://youtu.be/3wAaPNxgLHI?si=Yarxhgsj25RTkMHI) on how to create and add SHH for GitHub


### Step #4
```
git status
git push > to push the changes to your online repo

and last step check your online repo is it's synced up.

git status
```

## This step is for updating files/creating branches

### Step#1
CHeck the branch & create new one by
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
git commit -m "msg"
git push
```

### Step#3: Visit GitHub and merge the branches, then on you terminal

```
git checkout main
git pull
git branch -d NewBranch
git status
```


### GitHub tutorial resources:

1. [Git & GitHub repo set-up for beginners](https://youtu.be/jTHhMSxQTNI?si=dyrvXEz_c0iR-hky)
2. [The git flow](https://youtu.be/zTgXYR4PZ04?si=u3kfzdwt7Q7TRJoU)

# added this line