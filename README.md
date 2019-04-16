# Python skeleton app

A very simple Python skeleton app for use with Python 3.

- Change the `CoolPackageName` folder to the name of your project/package.
- Change `cool_file_name.py` to a meaningful filename.
- Change `test_cool_file_name.py` to the filename chosen above. Be sure to let that file name start with `test_` though! That way, py.test can automagically detect and run the tests within.

Need some extra information? Check [Jean-Paul Calderone's](http://as.ynchrono.us/2007/12/filesystem-structure-of-python-project_21.html) well explained blog post for how to structure your Python projects.

## Requirements

- Python 3
- PyPI for Python 3 (`pip`)
- Possibly [Virtualenv](https://virtualenv.pypa.io/en/stable/userguide/) to avoid dependency collisions between projects

## Installation

### Windows / macOS / Linux

```shell
$ git clone $(this.repo)
$ cd $(this.repo)
$ pip install -r requirements.txt
$ pytest --cov=.
```

### Vagrant

Alternatively, you could create a virtual machine with the accompanying Vagrantfile:

```shell
$ git clone $(this.repo)
$ vagrant plugin install vagrant-vbguest
$ vagrant up
$ vagrant ssh
$ cd /code
$ pytest --cov=.
```
