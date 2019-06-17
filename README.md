# Static - Static website generator
![Header](http://image-missing.org/image.png)
A painless static website generator for you. Very lightweight to be easy, secure and low CPU usage alternative to Wordpress and Jekyll, without need to have database and other stuff.

Works also using IPFS

Only few commands lines to use it :

```
static new <website-name> <template>
static post <post-name>
static page <page-name>
static publish
```

A very clear and lightweight setup, exclusively for Linux users.

## Install
### Dependencies
You will need only few basic things:

* A text editor (recommended: Atom)
* Git (recommended for quickstart install)
* Linux (only Linux for the moment, but it will change...)

### Install for Linux
This is how to install this app, just run the following commands:
```
git clone http://localhost:3000/root/Static.git
cd Static/install
sudo python3.7 static.py
```

## Contribute
This is an Open Source app that YOU can contribute! Just follow these steps:

### I don’t want to code

1. Respect the CONTRIBUTING.md file
2. Create an issue and describe your problem/feature request.
3. Discuss the topic
4. Close if needed.

### I want to code!

1. make sure you respect the CONTRIBUTION file
2. Fork this repository
3. Make changes
4. Make a pull request
5. You will be notified when your code has been reviewed / merged

## Quick start

Once you installed Static just follow the following steps:
1. Run `static new <sitename> <template-name>` and follow the setup
2. Run `static page <name>` to create a page (call it index to create an HOME page)
3. Run `static post <name>` to create a post
4. Run `static publish` when you want to publish your changes!

## Credits and copyrights
Under GNU license
