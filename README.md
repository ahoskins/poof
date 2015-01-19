# poof
Quickly open "your setups" from the command line.  Some examples of setup's:
- Web development
- Writing
- Music
- Android development
- Note-taking

# usage
A single setup is known as a **space**.  An application within the space is known as, well, an **application**.

### first, create a new space:
    $ poof space <space-name>

### add an application to the space:
    $ poof add <space-name> <application-name>

You can add as many applications to a space as want.

### start running a space:
    $ poof start <space-name>

This will launch all application that space.

If you make a mistake or want to modify something, you can either delete the entire space or a single application in the space.

### delete an application from a space:
    $ poof delete <space-name> <application-name>

### delete an entire space:
    $ poof delete <space-name>
    
# underlying form
At the moment, this will only work on OS X.  

Poof stores the data in a JSON file at $HOME/.poof, for the curious.



