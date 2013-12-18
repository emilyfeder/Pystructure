all: install

install:
	sudo pip install virtualenv
	virtualenv venv
	venv/bin/pip install nltk
	venv/bin/python -m nltk.downloader wordnet
	venv/bin/pip install nose
	venv/bin/pip install Flask
	venv/bin/pip install Hamlish-Jinja
	venv/bin/pip install WebTest
