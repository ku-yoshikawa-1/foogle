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

### SET UP
You do the following at first time.
1. In Terminal, go to your foogle directory using "cd" command.

If you dont know where is your foogle directory, pls do the following.

Open Github Desktop -> Click "Repository" in Header bar -> Click "Open in Terminal".
In the terminal, type "pwd" + Enter. You can get the foogle direcory path.

2. run to initialize docker containers.
```
docker-compose up
```
Then, you can access to http://0.0.0.0:5000/.

### START & STOP
After you do setup, you can stop & restart the containers.
```
docker-compose stop
docker-compose start
```
When you check the containers,
```
docker-compose ps
```
When you delete all containers in docker-compose,
```
docker-compose down
```
### LOGIN IN MYSQL
IF you want to login mysql server,
```
docker exec -it mysql bash
```
And then,
```
mysql -u root -p
```
password is "admin".

## Node.js
Please Download Node.js to build your vue application.
You can download from [here](https://nodejs.org/en/download/).

Then, you can use the following command in front_end directory.
```
npm i && npm run serve
```
Then, you can access to http://localhost:8080/.


## Database
4 tables
product_info(product_id, product_name, category_name, type(ENUM('F', 'V', 'M')), pna1, pna2, pna3, cna1, cna2, cna3)
14 vegetable, 16 fruit and 3 meat types
product_id(primary) and product_name are unique. For example Kyoto tomato
category and type are not null. catergory(tomato), type(V)
pna1-3, cna1-3 are alternative writing like　ほうれんそう　and　ほうれん草

shop_info(shop_id(primary), shop_name, latitude, longitude, brand, shop_description)
contains real data about 20 supermarkets that have website that contains sale info and sell veg, fruit and table
shop_id(primary) and shop_name are unique. For example Fresco Kitashirakawa
latitude and longitude are not null.
brand(Fresco)

user(user_id(primary), password(default='psw'), first_name, last_name, gender(enum('F', 'M')), occupation(ENUM('student', 'part-time', 'full-time', 'elder', 'jobless')), tr_mode(ENUM('bicycle', 'walking', 'car')))
1000 fake users
half user only have user_name and password, other half have all data

bargain_info(product_name(references product_info), shop_name(references shop_info), price, end_time, price_peritem, pack_ll, pack_ul, pack_size(ENUM('S', 'M', 'L')), item_size(ENUM('S', 'M', 'L')), pack_type(ENUM('pack_countable', 'pack_notcountable', 'single_item', 'pack_weight')))
~5000 bargain information data
pack_ll and pack_ul are pack lower limit and upper limit when pack_type is pack_noncountable
end_time set to august 18, 2019

## Jupyter notebook file for generating data
pip_install sql_alchemy
you should alter this line
engine = create_engine('mysql://admin:83946066@localhost/db')
engine = create_engine('mysql://user:password@localhost/db')








