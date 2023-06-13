import codecs
import os.path

import re
import subprocess
import sys

from setuptools import setup, find_packages
#from catchpoint import vv

_PEP386_SHORT_VERSION_RE = r'\d+(?:\.\d+)+(?:(?:[abc]|rc)\d+(?:\.\d+)*)?'
_PEP386_VERSION_RE = r'^%s(?:\.post\d+)?(?:\.dev\d+)?$' % (
    _PEP386_SHORT_VERSION_RE)
_GIT_DESCRIPTION_RE = r'^v{0,1}(?P<ver>%s)-(?P<commits>\d+)-g(?P<sha>[\da-f]+)$' % (
    _PEP386_SHORT_VERSION_RE)


from subprocess import Popen, PIPE


def call_git_describe(abbrev):
    try:
        p = Popen(['git', 'describe', '--abbrev=%d' % abbrev],
                  stdout=PIPE, stderr=PIPE)
        p.stderr.close()
        print("aaaaaaaaaaaa1")
        lines = p.stdout.readlines()
        print("aaaaaaaaaaaa1", lines)
        line = lines[0]
        print("aaaaaaaaaaaa3", line)
        return line.strip()

    except:
        print("aaaaaaaaaaaa4")
        return None


def is_dirty():
    try:
        p = Popen(["git", "diff-index", "--name-only", "HEAD"],
                  stdout=PIPE, stderr=PIPE)
        p.stderr.close()
        lines = p.stdout.readlines()
        return len(lines) > 0
    except:
        return False

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

        
        

def read_git_version():
    print("deneme")
    try:
        print("deneme3")
        proc = subprocess.Popen(('git', 'describe', '--long', '--tags'),
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("deneme4")
        data, _ = proc.communicate()
        print("deneme5")
        if proc.returncode:
            print("deneme6")
            return
        print("deneme7")
    except:
        print("error1")
        return
      

def get_git_version(abbrev=7):
    # Read in the version that's currently in RELEASE-VERSION.

    release_version = get_version('catchpoint/_version.py')
    print("deneme0", release_version)

    # First try to get the current version using “git describe”.
    version = call_git_describe(abbrev)
    print("deneme1", version)
    if is_dirty():
        version += "-dirty"

    # If that doesn't work, fall back on the value that's in
    # RELEASE-VERSION.

    if version is None:
        version = release_version

    # If we still don't have anything, that's an error.

    if version is None:
        raise ValueError("Cannot find the version number!")

    # If the current version is different from what's in the
    # RELEASE-VERSION file, update the file to be current.

    if version != release_version:
        write_release_version(version)

    # Finally, return the current version.

    return version


def gg():
    print('burada')
    get_git_version()
    return '2.3.4'
        
setup(name='cccc',
      version=gg(),
      description='cccc Python agent',
      long_description='cccc Python agent',
      url='https://github.com/thundra-agent-python',
      author='cccc',
      author_email='python@cccc.io',
      python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*',
      packages=find_packages(exclude=('tests', 'tests.*',)),
      install_requires=['requests>=2.16.0', 'opentracing>=2.0', 'wrapt>=1.10.11', 'simplejson', 'enum-compat',
                        'jsonpickle==1.3', 'websocket-client', 'python-dateutil', 'GitPython>=3.1.18', 'fastcounter>=1.1.0', 'pympler'],
      zip_safe=True,
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
      ],
      )
