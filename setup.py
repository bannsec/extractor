# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path, system
from setuptools.command.install import install
from setuptools.command.develop import develop

here = path.abspath(path.dirname(__file__))

#with open(path.join(here, 'README.md'), encoding='utf-8') as f:
#    long_description = f.read()
long_description = "See website for more info."

def fix_setuptools():
    """Work around bugs in setuptools.                                                                                                                                                        

    Some versions of setuptools are broken and raise SandboxViolation for normal                                                                                                              
    operations in a virtualenv. We therefore disable the sandbox to avoid these                                                                                                               
    issues.                                                                                                                                                                                   
    """
    try:
        from setuptools.sandbox import DirectorySandbox
        def violation(operation, *args, **_):
            print("SandboxViolation: %s" % (args,))

        DirectorySandbox._violation = violation
    except ImportError:
        pass

# Fix bugs in setuptools.
fix_setuptools()

class CustomInstallCommand(install):
    """Hack to install github version of PyEasyArchive"""
    def run(self):
        system("pip install https://github.com/dsoprea/PyEasyArchive/tarball/master")
        install.run(self)


class CustomDevelopCommand(develop):
    """Hack to install github version of PyEasyArchive"""
    def run(self):
        system("pip install https://github.com/dsoprea/PyEasyArchive/tarball/master")
        develop.run(self)



setup(
    name='extract',

    version='0.0.1',

    description='Universal unpacker/unarchiver/extractor',

    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/owlz/extract',

    # Author details
    author='Michael Bann',
    author_email='self@bannsecurity.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: End Users/Desktop',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console'
    ],

    keywords='unpack unarchive extract',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['rarfile','python-magic'],

    entry_points={
        'console_scripts': [
            'extract = extract.extract:main',
        ],
    },

    cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDevelopCommand,
    },

)

