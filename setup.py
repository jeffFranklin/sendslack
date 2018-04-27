from setuptools import setup


setup(name='sendslack',
      install_requires=['requests'],
      description='Send a message via stdin to a slack channel',
      py_modules='sendslack')
