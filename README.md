This purpose of this project is to demonstrate a way to set up
python projects.

In particular, I wanted to demonstrate:

1. How to have one package depend on a sibling package.
2. Where to put the tests for each package and how to run
   them.

##What I learned

This project is structured as such:

    Pystructure/ # Project folder
        lemmatizer/ # Python package
            __init__.py
            lemmatokenizer.py # A module within the lemmatizer package
            sample_run.py # Script to run the LemmaTokenizer
            tests/
                lemmatokenizer_test.py
            subpackage/
              __init__.py
        dashboard/ # Another python package
            dashboard.py # file that defines the flask app
            tests/
                dashboard_test.py
        run_app.py  # script to run the app defined in the dashboard package

### What is a module?
It is just a python file and any objects or functions it defines are in its namespace. It can
also contain a script section which will be run with the command 

    $ python module.py

### What is a package?
According to the documentation,
"Packages are a way of structuring Python’s module namespace,"
which means that it make it easier to reference a particular package, its modules, 
and subpackages in other code.
A package is any folder with an __init__.py file in it. Then any module contained within it
can be included in another package using dot notation.

For example, to include the LemmaTokenizer object from lemmatizer/lemmatokenizer in
dashboard.py, which is in lemmatizer's sibling package, use this import statement:

    from lemmatizer.lemmatokenizer import LemmaTokenizer

This is called an absolute import because it uses the top-package name lemmatizer. There are
also relative imports, but I wouldn't recommend using them because they don't allow such
flexibility if you want to rearrange your project structure.

If you were to import the LemmaTokenizer from another module within lemmatizer such as
sample_run.py, you could just use the import statement:

    from lemmatokenizer import LemmaTokenizer 

To understand how python recognizes the name that is imported, see the next section.

### Scripts
When you run a script from the command line, any modules or packages imported in that script
must be found in the list of directories given by the variable sys.path. Which directories
are added to sys.path?

1. The directory containing the script.
2. the environment variable PYTHONPATH (like PATH)
3. the directory containing the default python packages (like unittest or datetime)

This is very important, because let's say the script run_app.py was in dashboard/ , not in the
main project folder, you will get an error that lemmatokenizer is not recognized as a module.
To understand this, let's see what would be in sys.path if we used
Pystructure/dashboard/run_app.py instead of Pystructure/run_app.py

The directory dashboard/ will be added to sys.path so all of dashboard's modules and subpackages will be
recognized (NOT lemmatizer and its modules). Unless you've manually added lemmatizer/ to PYTHONPATH, it won't be there either.

Therefore lemmatizer.lemmatokenizer would never be added to the namespace so it won't be
recognized.

Therefore, if module A in a package needs a module from a sibling package, any script that
imports module A must be run in the parent directory of the sibling packages.
For example, here run_app.py is found in the main Pystructure folder, which contains sibling
packages lemmatizer and dashboard.

### Tests
Tests can be run in a few different ways, and that determines where you want to put them.
Because any method of running tests uses scripts to do so, any option must consider the rules
for running scripts as described above.

A few options I've explored:

1. Make unittest TestCases and then run them at with unittest.main() at the bottom of each
   test module. Then they are just scripts which should be handled as such when running them.
   With this in mind, each package must have its own test/ folder where each
   module only tests the functions and objects found in that package.

2. Use the nose test runner, which is much smarter at detecting tests and doesn't require
   that you make a script to run each test. You can read documentation about what tests need
   to look like to be detected, but they can just be unittest TestCases. And with the
   detection provided by nose, you have more flexibility over where to put your tests. You
   could have test/ directories for each subpackage or one large test/ directory for the
   entire project. Nose provides a script called nosetests which must be run from the main
   project directory, NOT from a package. If run from the main project directory, it will
   make sure to add all the appropriate directories to the sys.path for modules to be
   recognized in the imports.

## Installation/Usage

    $ make install
    
To open the web interface at localhost:5000 :

    $ python run_app.py

To run the tests:

    $ nosetests

## References

Some web pages I found useful while creating this project:

The python documentation on modules, packages, and scripts:
http://docs.python.org/2/tutorial/modules.html

A great article from Jeff Knupp -- I took a look at the source code he provided as an example:
http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/

This post pushed me to use nose as a test runner:
http://schettino72.wordpress.com/2008/01/19/11/



