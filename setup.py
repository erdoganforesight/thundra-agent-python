import codecs
import os.path

import re
import subprocess
import sys

from setuptools import setup, find_packages


def get_git_revision_short_hash():
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version_from_file(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")
 

def get_version():
    _hash = abs(hash(get_git_revision_short_hash())) % (10 ** 8)
    _version = get_version_from_file('catchpoint/_version.py')
    print("hasan", _version, _hash)
    release_version = _version + '.a.' + str(_hash)
    print(release_version)
    return release_version
        
    
setup(name='cccc',
      version=get_version(),
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
