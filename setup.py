from setuptools import setup, find_packages

version = '1.1'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(name='poi.maildefaults',
      version=version,
      description="Simple setting of mail-in defaults for Plone Poi Trackers",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: BSD License",
          "Programming Language :: Python :: 2.7",
          "Framework :: Zope2",
          "Framework :: Plone :: 4.1",
          "Framework :: Plone :: 4.2",
          "Framework :: Plone :: 4.3",
          "Framework :: Plone :: 5.0",
      ],
      keywords='',
      author='',
      author_email='',
      url='https://github.com/sixfeetup/poi.maildefaults/',
      license='bsd',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['poi'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'Plone>=4.1',
          'poi.receivemail>=1.12.2',
          'Products.Poi>=3.0',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
