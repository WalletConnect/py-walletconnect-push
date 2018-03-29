from setuptools import setup, find_packages

setup(
  name='wallet-connect-push',
  version="0.1",
  install_requires=[
    'aiohttp',
    'uvloop',
  ],
  packages=find_packages(),
  entry_points={
    'console_scripts': ['wallet-connect-push=wallet_connect_push:main',]
  },
)
