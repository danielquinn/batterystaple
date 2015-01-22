isaac
=====

A password checker uses the natural rainbow table that is Google search for
validation.

Installation
------------

You can install it from PyPi::

    $ pip install isaac


Usage
-----

Command Line
............

Running it from the command line will generate a report::

    $ isaac <password>

So to use our favourite example::

    $ isaac 'correct horse battery staple'

      Report for: correct horse battery staple
      MD5: FAIL
      SHA1: FAIL
      SHA256: FAIL

But for something a little less well-known::

    $ isaac 'carpentry esteem reeks disdainful'

      Report for: carpentry esteem reeks disdainful
      MD5: OK
      SHA1: OK
      SHA256: OK


Python
......

You can use ``isaac`` from within Python too::

    from isaac.password import Password

    my_password = Password("correct horse battery staple")
    my_password.check_rainbows()         # False
    my_password.check_rainbow("md5")     # False
    my_password.check_rainbow("sha1")    # False
    my_password.check_rainbow("sha256")  # False

    my_password = Password("carpentry esteem reeks disdainful")
    my_password.check_rainbows()         # True
    my_password.check_rainbow("md5")     # True
    my_password.check_rainbow("sha1")    # True
    my_password.check_rainbow("sha256")  # True

    my_password = Password("1qazxsw2")
    my_password.check_rainbows()         # False
    my_password.check_rainbow("md5")     # False
    my_password.check_rainbow("sha1")    # False
    my_password.check_rainbow("sha256")  # False

Colophon
--------

But why "Isaac"?  The idea here is that we're going for rainbow tables, and who
better to name this after than the person who discovered and documented the
visual spectrum?  Isaac Newton was a really smart guy.
