timetravelpdb
=============

Enhances the Python Debugger to add the ability to travel back in time.

Have you ever been using PDB to step through a program and suddenly
realize you wish you could jump back in time and know what a variable
used to contain?

This version of PDB adds the ability to jump back in time to the
state of your program as it was in the past.  You can examine
variables and even continue execution from that point forward (though
that is dangerous because it may harm the time space continuum.)

For a demo, watch this YouTube video: https://youtu.be/7sYigEBdG00

How it works:

As you know, time is the 4th dimension.  Every moment is another
universe.  Pretty trippy, eh?

TTPDB simply records a pointer to the current universe before
displaying the input prompt.  As you step through your program,
each step records a pointer to the past universes.  The last 100
pointers are remembered.  You can jump into any of those universes.
Once in those universes you can examine variables.  Heck you can
do anything you want because you are really in that universe.

Once you are done with that universe you can "pop up" back to the
universe you left thanks to our time portal technology.


Q:  When I'm in another universe, can I run the code?
A:  Yes. However if you modify anything outside of your python
    process there's a chance you will create a hole in the time-space
    continuum and destroy the universe.


Q:  Can I use the "record universe" function while in another universe?
A:  Of course!  In fact, while in those past universes do a "ulist"
    to see the universes recorded so far.  You'll notice that there
    are fewer items on the list. That's because when you were in that
    moment of time, the others hadn't been recorded yet.  Stepping
    through the program will now make a new branch of history.  You
    can jump between those universes, pop up back to where you came
    from, and so on.   It can be a little confusing but, heck, time
    travel always is.


Q:  Why did you release this on April Fools Day?
A:  Seemed like a good idea at the time.


Q:  Is this to promote your "Time Management for System Administrators" book?
A:  This one?  http://everythingsysadmin.com/books.html
    No, not at all. It's to promote my next book which won't be
    out until October 2014: The Practice of Cloud Administration.
    http://everythingsysadmin.com/2014/03/sneak-preview.html
    Oh, and it certainly isn't promoting my
    RFC April Fools book: http://rfchumor.com/


Q:  Are you really traveling back in time?
A:  No.   Everyone knows it isn't possible to actually travel
    back in time.  All we have of the past is our memories.  What
    this does is use a feature of the Unix kernel that has been
    there since the 1970s to record a snapshot of absolutely
    everything about the process and jump between these memories.
    This feature is greatly misunderstood by most Unix users.

The truth is that we can't go back in time.  It would be nice if
we could.  But we can't.  
Instead we have our old memories and that has to be good enough.
And, to be honest, what most of us need more than the abilty to
travel back in time is the ability to let go of the past.
