from setuptools import setup

setup(name='pyrot',
      version='0.1',
      description='3D rotation representations and conversions',
      url='https://github.com/serycjon/pyrot',
      author='Jonas Serych',
      author_email='jonas.serych@gmail.com',
      license='MIT',
      packages=['pyrot'],
      install_requires=[
          'numpy'
          ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
