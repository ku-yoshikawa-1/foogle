Readme
=======
# Set up

## git / Github

1. Understand what is git.

  If you already have experienced git, pls skip this section.
  https://medium.freecodecamp.org/what-is-git-and-how-to-use-it-c341b049ae61

2. Github Desktop

  GitHub Desktop is GUI for git & Github. If you don't wanna use `git` CUI, the application is useful for you.
  Download here -> https://desktop.github.com

3. Clone our repository

  go to [here](https://github.com/ku-yoshikawa-1/foogle) and click "clone and download" → "open in desktop".
  Our repo are cloned to your Github Desktop automatically.

4. Create your local branch

  Open Github Desktop and click "Branch"→"New Branch" on menu bar. You should name new branch what you will do in the branch.   For example, you will fix bug about`<button/>` which work as sumbit botton, the branch name is `fix_submit_button_bug`.

5. Coding

  you coding or some work in your branch. After you code, commit your code. You should name commit what you did.
  If you did several works in one commit, you should divide the commit into several commits. Remenber "one commit = one work" rule.

6. Create Pull request

  After you finish working in your branch, create "pull request". click "Branch"→"Create Pull Request".
  You will jump github web site automatically. Name your pull request and edit details. after that, click "Create Pull Request".

## docker
we use docker in order to use Flask web server.
Please download [docker desktop](https://www.docker.com/products/docker-desktop).

### create your environment
1. Move your foogle directory.
2. run 
```
docker build -t foogle:latest .
```
3. run
```
docker container run -v [YOUR CURRENT DIRECTORY ABSOLUTE PATH]:/root -p 5000:5000 foogle
```
Then, you can access to http://0.0.0.0:5000/.

## Node.js
Please Download Node.js to build your vue application.
You can download [here](https://nodejs.org/en/download/).

Then, you can use the following command in front_end directory.
```
npm run serve
```
Then, you can access to http://localhost:8080/.