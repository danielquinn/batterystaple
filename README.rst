issac
=============

A password checker uses the natural rainbow table that is Google search for
validation.

Installation
------------

You can install it from PyPi::

    $ pip install issac


Usage
-----

Command Line
............

Running it from the command line will generate a report::

    $ issac <password>

So to use our favourite example::

    $ issac 'correct horse battery staple'

      Report for: correct horse battery staple
      MD5: FAIL
      SHA1: FAIL
      SHA256: FAIL

But for something a little less well-known::

    $ issac 'carpentry esteem reeks disdainful'

      Report for: carpentry esteem reeks disdainful
      MD5: OK
      SHA1: OK
      SHA256: OK


Python
......

You can use ``issac`` from within Python too::

    from issac.password import Password

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




