from setuptools import setup, find_packages

setup(
  name='walletconnect-push',
  version="0.7.11",
  install_requires=[
    'aiohttp',
    'uvloop',
  ],
  packages=find_packages(),
  entry_points={
    'console_scripts': ['walletconnect-push=walletconnect_push:main',]
  },
)
