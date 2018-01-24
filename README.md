## Onboarding Link Generator

**A command line tool to create personalized patchwork invite pages for your friends!**

# Background

Within this repository is a tool you can run to quickly whip up personalized patchwork invite  pages for your friends.  These pages include GIFs for how to download and use patchwork, a pub invite key with
instructions on what to do with it, and some channels that you recommend they
check out.

The tool generates a styled HTML page, that you can then host on your own
website.  If you don't have a website, we provide a tutorial at the end of this
on how to quickly spin one up, using beaker browser and hashbase!  

Our intention with generating a page, but not hosting it for you, is to give you more
power with the invites you send out.  Not only can you make the pages on your
own time, and not require anyone's approval, but you can also further customize
the page as you see fit.  If you don't like the greeting I use, go ahead and change it!  If you want to change how the page looks completely, you can do that too(with a few limitations).  There's a tutorial on how to do this at the bottom of the page too.

Scuttlebutt values personal autonomy and subjectivity, the delight of multiple
voices describing the same thing in their own unique ways.  This onboarding
generator  is my attempt to honor these values through even the smallest
tools.  

Also, if I'm being honest (and I AM), I wanted to use this generator as a way
to introduce you to some other cool tools like git, python, the beaker browser,
and hashbase.  All of them are powerful, but could be overwhelming without some
reason to use them.  The onboarding tool can be that reason.  You will use all of these tools for the generator, but without having to do _much_ with them.   it's the code
equivalent of playing "Heart and Soul" on the piano before you learn anything else, just so you know  how
pleasant the piano keys and melody feel.

# Summary of Use 

I'll offer quick instructions first, followed by detailed instructions.  Dont' worry if the
quick instructions don't make sense (_yet_), I'll explain each part after.

**Quick barebones instructions for the solarpunk in a rush!**
*(to use this tool you will need python3)*

1. clone the repo from git-ssb and enter the onboarding-link-generator directory.
`git clone ssb://%XpYR3HjkbEL40CQhuGpgZ5P55zGJ1p9aI1L1A3jfVag=.sha256 onboarding-link-generator `
`cd onboarding-link-generator`
*There are three key areas in this repo you'll interact with:

* the link generator called 'onboarding-tool.py'
* the invites directory, where all the onboarding links are stored (for you to then move to your own site)

* contact-info.ini, a config sheet for you to put in your personal details so you don't have to fill them out each time.*

2. request an invite key from a pub that you follow, or generate one yourself
   (if you're a pub owner)

3. From within the Onboarding-Link-Generator directory, invoke the generator with
`python3 onboarding-tool.py`

4. Answer all the questions it gives you. 

5. When the questions are done, a new folder will be made for you, within the 'invites' subdirectory.  This folder will be named after your friend.  Move it to your website, then give that link to your friend!


**Details for the Easygoing Solarpunk**

The onboarding link generator lets you create a static page for each of the
friends you want to invite.  This page includes steps on installing patchwork,
the pub you would like them to join, an invite code for this pub, and other
good details for them to confidently join the 'verse.

The page comes already styled, and already equipped with handy to-do GIFs.  In other words, you don't need to style up the page yourself, you just need to personalize it with your friend's details.

This personalization is done through a set of questions asked by onboarding-tool.py, and so the most crucial part is making sure you can access and run this script!

And so!  To properly run this script you'll need:

*  Access to the command line, and some basic familiarity with it.  If both are new to you, I've written a quick introduction to the command line and the small set of commands you'd need for this onboarding tool.  [Read the guide here!](command-line-introduction)
* Python 3.  You won't need to know python for this tool.  You'll just need to know how to check if your computer _has_ python3, and how to tell python3 to run the tool.  If you don't know what Python is, or how to check if you have Python3, then I wrote a small introduction and the steps for installation.  [Read that guide here!](python-introduction)
* Basic knowledge of git, and git-ssb. This is mostly so you know how to _get_ this cool onboarding tool.  If this is your first interaction with git, I wrote up a small ode/tutorial and that can be read [here](git-tutorial) 

These three requirements are used mostly for downloading and initially running the tool, once you are using the tool, it's a quick, guided process.  Reading through the guides, and installing everything, will likely take less than 30 mninutes.  But the skills learned will last you _a lifetime_, and can act as a nice introduction to a whole world of good skills, so that's convenient.

Go ahead and read through the guides then come back here.  Each one opens in a new window.  If you feel on top of it all, then let's keep going!

You create these pages by invoking the generator within the command line, and answering the
questions it presents.  When you move through the whole process, a new directory is made on your
computer, named after your friend.  This directory includes two files, an index.html file and
a stylesheet.css file.  Both are already filled out, and so you simply move this folder to where you
host your site, and now have a handy link to give your friend: mysite.com/friends-name/

``` 
Insider Tip: At the bottom of this repo  is a link to a video showing how to use the tool and host a site on
hashbase
```

# Screen Shots 

**The Command Line Tooli** !
[the command line tool](resources/tool-walkthrough.gif) 

**The Generated Invite Page** 
![Page Opening](resources/page-screenshot-1.png)

![The Pub Link](resources/page-screenshot-2.png)

# Usage

``` 
The Tool Requires Python 3
```

**Clone this Repo to your Computer** 
```
git clone ssb://%XpYR3HjkbEL40CQhuGpgZ5P55zGJ1p9aI1L1A3jfVag=.sha256 onboarding-link-generator
``` 

**Navigate to the repo's directory** 
``` 
cd onboarding-link-generator 
``` 

There are two important areas within this directory: onboarding-tool.py and invites/.  You'll invoke the generation through onboarding-tool.py and your finished site will live within the invites/ subdirectory.

**Invoke the Generator**
```
python3 onboarding-tool.py
```
**Run through the Questions**
These are pretty straightforward.  You will want to make sure you invite them to a pub you are following, and invite them with an active pub invite link.  This can be given to you by the pub owner (which may be you!) through whichever process they prefer.  For the final channels, you can write the channel plus a description of it, if you wanna get fancy.

**Find, then move, your new site**
When the tool is done you'll have a new directory within invites called 'friends-name'.  This has the index.html file and the stylesheet.  Simply move this entire directory to wherever you host your site.  Below is a link to a video showing how to do this using hashbase.

**Save Time in the Future with the 'contact-info.ini' file**
In the root directory of the repo is a file called 'contact-info.ini'.  This has three sections you can fill out with your own details.  Then, these details are automatically filled out in the questions.  It's useful so you don't have to type in yr pub key each time.  Fill in each one with whatever you like (or leave it blank if you wanna type it anew each time) but please don't remove any of the contacts.

**[How to Easily Host Invite Pages on Hashbase: A Video!](https://vimeo.com/243558425)**

