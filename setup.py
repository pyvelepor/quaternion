try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Quaternion',
    version='0.0.0',
    description='Quaternion library',
    author='Calvin Robinson',
    url='https://github.com/crobinsonut/quaternion',
    packages=[
        'quaternion',
        'quaternion.test',
    ],
    package_dir={
        '' : 'src',
    },
    data_files=[
        ('', ['readme', 'setup.py']),
    ],
)
