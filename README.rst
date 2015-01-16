batterystaple
=============

A password checker that follows [XKCD's sage advice](http://xkcd.com/936/) and
does some rainbow table checks on top of that.

Installation
------------

You can install it from PyPi::

    $ pip install batterystaple


Usage
-----

Command Line
............

Running it from the command line will generate a report::

    $ batterystaple <password>


Python
......

You can use ``batterystaple`` from within Python too::

    from batterystaple.password import Password

    my_password = Password("correct horse battery staple")
    my_password.check_length()
    # True

    my_password.check_dictionary()
    # True

    my_password.check_rainbows()
    # False, because the md5 hash of that password is listed in Google


