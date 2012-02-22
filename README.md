Amazon Wishlist
===============

Python version of the old and buggy Perl module WWW::Amazon::Wishlist. It's written using LXML and XPaths for better readability and so far I guarantee it works fine with 2.6 in OSX.

This is my first attempt in writing a Python module so bear with me as you find something not really looking pythonic. It supports the Amazon stores in the US, UK, France, Spain, Italy, Germany, Japan and China. I'm still behind testing them all, though.

Usage
=====

It's a simple module and the code documention is self-explanatory. Take a look at the test application `basin.py`.

TODO
====

* Write a scrapper using only someone's e-mail address
* Italian store has odd author attribution with '~' that needs a look
* Handle Shift_JIS, Japanese charset that breaks titles/authors
* Normalize all returns to the same type, if possible
* Shorten the longest XPaths (minor, just prettyfication)
* Some coded tests would be good...

License
=======

All files in this repository are under GPLv2, please see the LICENSE file for details.
