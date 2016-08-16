# Copyright (c) 2016 Calvin Ference
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

help:
	@echo "Make Targets:"
	@echo "	build - builds a distribution"
	@echo "	build-deb - builds distribution as debian package"
	@echo "	build-rpi - builds distribution for Raspbian Package"
	@echo "	clean - Cleans the local directory of build artifacts"
	@echo "	create-virtenv - Creates a Python 2.7 virtual environement"
	@echo "	activate - Activates the virtenv"
	@echo "	deactivate - Deactivates the virtenv"
	@echo "	help - Prints this very helpful message"
	@echo "	init - Installs required python librairies"
	@echo "	install - This will install the package on the system"
	@echo "	install-dep - Install system dependencies"
	@echo "	test - Run the test suits"

init:
	sudo pip install -r requirements.txt

clean:
	sudo rm -rf build dist venvpy27 *.egg-info

create-virtenv:
	virtualenv --python=/usr/bin/python venvpy27

activate:
	source venvpy27/bin/activate

build:
	@echo "---BUILDING DISTRIBUTION---"
	sudo python setup.py bdist

build-rpi:
	@echo "Not implemented"

build-deb:
	@echo "Not implemented"

install-dep:
	sudo apt-get install -y python-nose python-pip virtualenv

test:
	nosetests tests

install:
	sudo python setup.py install

all:
	help
