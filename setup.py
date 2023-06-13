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
    try:
        proc = subprocess.Popen(('git', 'describe', '--long', '--tags'),
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        data, _ = proc.communicate()
        if proc.returncode:
            return
        print(data)
        ver = data.splitlines()[0].strip()
        print(ver)
        
    except:
        return

    if not ver:
        return
    m = re.search(_GIT_DESCRIPTION_RE, ver)
    if not m:
        sys.stderr.write('version: git description (%s) is invalid, '
                         'ignoring\n' % (ver,))
        return

    commits = int(m.group('commits'))
    if not commits:
        return m.group('ver')
    else:
        return '%s.post%d+g%s' % (
            m.group('ver'), commits, m.group('sha'))        
 

gg():
    read_git_version()
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
