from setuptools import setup, find_packages
import os

BASE_DIR = os.path.realpath(os.path.dirname(__file__))
VERSION = '2.1.1'
PACKAGE_NAME = 'harlogger'
PACKAGES = [p for p in find_packages() if not p.startswith('tests')]


def parse_requirements():
    reqs = []
    if os.path.isfile(os.path.join(BASE_DIR, 'requirements.txt')):
        with open(os.path.join(BASE_DIR, 'requirements.txt'), 'r') as fd:
            for line in fd.readlines():
                line = line.strip()
                if line:
                    reqs.append(line)
    return reqs


def get_description():
    with open(os.path.join(BASE_DIR, 'README.md'), 'r') as fh:
        return fh.read()


if __name__ == '__main__':
    setup(
        version=VERSION,
        name=PACKAGE_NAME,
        description='Simple utility for sniffing decrypted HTTP/HTTPS traffic on an iDevice',
        long_description=get_description(),
        long_description_content_type='text/markdown',
        cmdclass={},
        packages=PACKAGES,
        author='DoronZ',
        install_requires=parse_requirements(),
        entry_points={
            'console_scripts': ['harlogger=harlogger.__main__:cli',
                                ],
        },
        classifiers=[
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
        ],
        url='https://github.com/doronz88/cfprefsmon',
        project_urls={
            'pymobiledevice3': 'https://github.com/doronz88/cfprefsmon'
        },
        tests_require=['pytest'],
    )
