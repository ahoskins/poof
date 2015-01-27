# poof
Quickly open "your setup" from the command line.  Some examples of setup's:
- Web development
- Writing
- Music
- Android development
- Note-taking

Poof automates the process of starting up applications that comprise these setups.  It's designed for Mac OS X, and currently does not work on other platforms.

# installation
1. clone this repo
2. `$ pip install .`

Now `$ poof` should be available at the command line.

# usage
A setup is known as a **space**.  An application within the space is known an **application**.

### first, create a new space:
    $ poof space <space-name>

### add an application to the space:
    $ poof add <space-name> <application-name>

You can add as many applications to a space as you'd like.  When you add an application, the script will check for a close match in `/Applications/`.  So clearly, this won't cover all possible executables you'd like to launch, but it will cover most all traditional applications.

### startup a space:
    $ poof start <space-name>

This will launch all application in that space.

If you need to, you can either delete the entire space or a single application in the space.

### delete an application from a space:
    $ poof delete <space-name> <application-name>

### delete an entire space:
    $ poof delete <space-name>
    
### if you're a lost puppy:
    $ poof help
    
# underlying form
As mentioned above, this will only work on OS X.  This is because it launches applications out of `/Applications/`.   

Poof stores the data in a simple JSON file at $HOME/.poof.  This is the only place any data is stored - and messing with this file is not advised.







