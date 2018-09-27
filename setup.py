
#!/usr/bin/env python

from distutils.core import setup

setup(name='spotiman',
    version='0.1.0',
    description='High level wrapper around spotipy',
    author='Yigit Dallilar',
    author_email='yigit.dallilar@gmail.com',
    packages=['spotiman'],
    package_dir={'spotiman': 'src/spotiman'},
    scripts=['scripts/spotiman_simple_curses']
)
