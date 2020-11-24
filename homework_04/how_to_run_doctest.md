## How to run docktest:
* If you read this, you probably have installed python,
if not,\
you can install latest python version [here](https://www.python.org/downloads/) \
_(also you can install IDE "PyCharm EDU" by following another instructions [from here](https://www.jetbrains.com/help/pycharm/installation-guide.html))._
* Then, open file `task_4_doctest.py`.
* Now, there are two ways:
     * Write in terminal:
`import doctest` then `doctest.testmod()`.
    * Past follow strings at the document and run.\
     `if __name__ == "__main__":` \
        `import doctest` \
        `doctest.testmod()`

* if you won't get any message, all's OK, tests were passed.
