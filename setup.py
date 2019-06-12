from setuptools import setup, find_packages
import io
import re
import os

with io.open('./core/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name="fire-index",
    version=version,
    author='Dayanne Fernandes',
    author_email='dayannefernandesc@gmail.com',
    packages=find_packages(exclude='tests'),
    long_description=long_description,
    description="Fire detection index engine.",
    install_requires=['click'],
    extras_require={
        'dev': ['jupyter', 'pytest', 'bandit', 'flake8']
    },
    entry_points={
        'console_scripts': [
            'findex = core.main:start',
        ],
    },
    classifiers=[
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7',
        'Topic :: Machine Learning',
    ],
    keywords=(
        'Machine Learning',
        'AI'
    )
)
