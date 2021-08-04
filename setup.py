import setuptools, codecs, os.path

# get __version__ from a file
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

# setuptools configuration
setuptools.setup(
    name='nvautoinstall',
    description='A CLI tool which lets you install proprietary NVIDIA drivers and much more',
    long_description='A CLI tool which lets you install proprietary NVIDIA drivers and much more',
    url='https://github.com/t0xic0der/nvidia-auto-installer-for-fedora',
    author='Akashdeep Dhar',
    author_email='t0xic0der@fedoraproject.org',
    maintainer='Akashdeep Dhar',
    maintainer_email='t0xic0der@fedoraproject.org',
    license='GPLv3',
    # extract version from source
    version=get_version("src/nvautoinstall/__init__.py"),
    # tell distutils packages are under src directory
    package_dir={
      '': 'src',
    },
    packages=setuptools.find_packages('src'),
    install_requires=[
      'click',
      'distro',
    ],
    # automatically create console scripts
    entry_points={
      'console_scripts': ['nvautoinstall=nvautoinstall.MainFunction:clim'],
    },
    classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Intended Audience :: End Users/Desktop',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Natural Language :: English',
      'Programming Language :: Python :: 3',
      'Operating System :: POSIX :: Linux',
      'Topic :: System :: Hardware :: Hardware Drivers',
      'Topic :: Utilities',
    ],
)
