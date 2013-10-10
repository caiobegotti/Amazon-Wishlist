from os import path
from setuptools import setup

file = open(path.join(path.dirname(__file__), 'README.markdown'), 'r')
README = file.read()
file.close()

setup(name = 'amazon-wishlist',
      version = '0.5.1',
      description = 'Query and visualize Amazon wishlists information (e.g. total cost, items etc)',
      url = 'https://github.com/caio1982/amazon-wishlist',
      install_requires = ['pytest', 'lxml', 'BeautifulSoup'],
      py_modules = ['amazonwish.amazonwish', 'amazonwish.config'],
      license = 'GNU General Public License v2 (GPLv2)',
      keywords = 'amazon wishlist xpath lxml scrapping',
      author = 'Caio Begotti',
      author_email = 'caio1982@gmail.com',
      include_package_data = True,
      long_description = README,
      classifiers = [
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Programming Language :: Python',
          'Operating System :: POSIX',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: MacOS :: MacOS X',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
          'Topic :: Internet'])
