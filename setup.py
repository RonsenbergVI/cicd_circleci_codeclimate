# MIT License

# Copyright (c) 2021 Rene Jean Corneille

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from setuptools import setup
from configparser import ConfigParser



def get_version_info(config_path):
	"""
	Gets version information from a .cfg file
	"""
	config=ConfigParser()
	config.read(config_path)
	MAJOR=config['version']['major']
	MINOR=config['version']['minor']
	MICRO=config['version']['micro']

	ISRELEASED = True
	
	VERSION = '%s.%s.%s' % (MAJOR, MINOR, MICRO)

	return VERSION, ISRELEASED


def setup_package():

    config_path = os.path.join(os.path.dirname(__file__), 'setup.cfg')

    _version, _ = get_version_info(config_path)

    setup(name = 'package-medium-post',
        version = str(_version),
        description = 'prints time in command.',
        author = 'Rene-Jean Corneille',
        author_email = 'corneille.r.j@gmail.com',
        license = 'MIT',
        packages=['package_name'],
        url = 'https://github.com/RonsenbergVI/cicd_circleci_codeclimate.git',
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
        ],
        install_requires=[
            'Click',
        ],
        entry_points='''
            [console_scripts]
            clock=package_name:main
        ''',
        include_package_data=True
        )

if __name__ == "__main__":
    setup_package()