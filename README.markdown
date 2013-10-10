Amazon Wishlist
===============
Python improved version of the old, buggy Perl module WWW::Amazon::Wishlist.

Amazon-Wishlist lets you retrieve all information of your wishlist from Amazon stores which have that feature (stores which are Kindle-only do not). It comes with two sample applications to search and list data. It's also quite useful if you want to know the total cost of your Amazon wishlist. It's written using LXML and XPaths for better speed and readability.

Currently supported Amazon stores:
* United States
* United Kingdom
* Canada
* France
* Spain
* Italy
* Germany
* Japan
* China
* India
* Mexico (not live, Kindle-only)
* Brazil (not live, Kindle-only)

This is my first attempt in writing a Python module so bear with me as you find something not really looking pythonic. Patches are welcome in that sense!

Usage
=====

It's a simple module and the code documention is self-explanatory. Take a look at the test application `basin.py` at https://github.com/caio1982/amazon-basin. You may also try the sample applications shipped with the module, namely `profile.py` and `search.py`, both in the binaries directory.

Also you can try the built-in documentation with `python -c 'from amazonwish import amazonwish; help(amazonwish)'`.

TODO
====

* Real preventive error handling, that's web scrapping dude
* Write more py.test codes, specially for non-US stores and Unicode checks
* Get item titles even though they are not available (XPath bug?)

License
=======

All files in this repository are under GPLv2, please see the LICENSE file for details.
