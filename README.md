Amazon Wishlist
===============

Python version of the old and buggy Perl module WWW::Amazon::Wishlist. It's written using LXML and XPaths for better readability and so far I guarantee it works fine with 2.6 in OSX.

This is my first attempt in writing a Python module so bear with me as you find something not really looking pythonic. It supports the Amazon stores in the US, UK, France, Spain, Italy, Germany, Japan, China, Brazil and India. I'm still behind testing them all, though.

Usage
=====

It's a simple module and the code documention is self-explanatory. Take a look at the test application `basin.py`.

Also you can try the built-in documentation with `python -c 'from amazonwish import amazonwish; help(amazonwish)'`.

TODO
====

* Optimize Wishlist.authors(), too hackish
* Real preventive error handling, that's web scrapping dude
* Write more py.test codes, specially for non-US stores
* Get item titles even though they are not available (xpath bugs?)

License
=======

All files in this repository are under GPLv2, please see the LICENSE file for details.
