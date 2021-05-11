from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='varstate',
  version='0.0.1',
  description='Python Package For Managing Data ReactJS State-Like.',
  long_description_content_type="text/markdown",
  long_description=open('README.md').read(),
  url='https://github.com/5elenay/varstate/', 
  author='5elenay',
  author_email='',
  license='GNU General Public License v3 (GPLv3)', 
  project_urls={
      "Bug Tracker": "https://github.com/5elenay/varstate/issues",
  },
  classifiers=classifiers,
  keywords=["state", "python"], 
  packages=find_packages(),
  install_requires=[] 
)