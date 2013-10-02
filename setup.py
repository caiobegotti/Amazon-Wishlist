from os import path
from setuptools import setup

def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()

setup(name='amazon-wishlist',
      version='0.2',
      description='Python version of the old and buggy Perl module WWW::Amazon::Wishlist',
      author='Caio Begotti',
      author_email='caio1982@gmail.com',
      url='https://github.com/caio1982/amazon-wishlist',
      install_requires=['pytest', 'lxml', 'BeautifulSoup'],
      long_description=read('README.markdown'),
      py_modules=['amazonwish.amazonwish', 'amazonwish.config'],
      license='GNU General Public License v2 (GPLv2)',
      keywords='amazon wishlist xpath scrapping',
      classifiers=[
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
