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

So to use our favourite example::

    $ batterystaple 'correct horse battery staple'

      Report for: correct horse battery staple
      Length: OK
      Dictionary: OK
      Rainbows:
        MD5: FAIL
        SHA1: FAIL
        SHA256: FAIL

But for something a little less well-known::

    $ batterystaple 'carpentry esteem reeks disdainful'

      Report for: carpentry esteem reeks disdainful
      Length: OK
      Dictionary: OK
      Rainbows:
        MD5: OK
        SHA1: OK
        SHA256: OK


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


