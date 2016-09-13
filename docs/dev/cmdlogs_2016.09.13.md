$ git clone https://github.com/icode-live/lean-website.git
Cloning into 'lean-website'...
remote: Counting objects: 4, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (4/4), done.
Checking connectivity... done.

$ cd lean-website/

vim .git/config

```
[alias]
    co = checkout
```

$ git co -b development
Switched to a new branch 'development'

$ git merge master
Already up-to-date.

$ git status
On branch development
nothing to commit, working directory clean

vim .gitignore

```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# SQLite3 database files:
*.db
*.sqlite3
*.sqlite

# Logs:
*.log

# Environment variables
# *.env

# Django stuff:
*.mo
*.pot

# Linux
*~
*.swp
*.swo
```

$ git status

On branch development
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.gitignore
	docs/

nothing added to commit but untracked files present (use "git add" to track)

# lean-website

```
$ pyvenv-3.5 lean-icode
$ source lean-icode/bin/activate

$ pip install -U pip wheel
Collecting pip
  Using cached pip-8.1.2-py2.py3-none-any.whl
Collecting wheel
  Downloading wheel-0.29.0-py2.py3-none-any.whl (66kB)
    100% |████████████████████████████████| 71kB 807kB/s
Installing collected packages: pip, wheel
  Found existing installation: pip 8.1.1
    Uninstalling pip-8.1.1:
      Successfully uninstalled pip-8.1.1
Successfully installed pip-8.1.2 wheel-0.29.0
(lean-icode) tac@yoshiki ~/Work/icode/requirements $ pip install -U neovim
Collecting neovim
  Using cached neovim-0.1.9.tar.gz
Collecting msgpack-python>=0.4.0 (from neovim)
  Using cached msgpack-python-0.4.8.tar.gz
Collecting greenlet (from neovim)
  Using cached greenlet-0.4.10-cp35-cp35m-manylinux1_x86_64.whl
Building wheels for collected packages: neovim, msgpack-python
  Running setup.py bdist_wheel for neovim ... done
  Stored in directory: /home/tac/.cache/pip/wheels/39/bf/62/94c635c222901de1fe04db7127422f786d82e1359436fbf0e2
  Running setup.py bdist_wheel for msgpack-python ... done
  Stored in directory: /home/tac/.cache/pip/wheels/2c/e7/e7/9031652a69d594665c5ca25e41d0fb3faa024e730b590e4402
Successfully built neovim msgpack-python
Installing collected packages: msgpack-python, greenlet, neovim
Successfully installed greenlet-0.4.10 msgpack-python-0.4.8 neovim-0.1.9


$ pip install -r lean-dev.txt
Collecting Django==1.10.1 (from -r lean-base.txt (line 1))
  Using cached Django-1.10.1-py2.py3-none-any.whl

...

Successfully built django-environ Markdown MarkupSafe django-behave pytest-twisted pytest-bdd pycrypto parse-type sqlparse coverage glob2 Mako
Installing collected packages: Django, six, django-environ, Markdown, MarkupSafe, ecdsa, pycrypto, paramiko, Pillow, parse, parse-type, behave, selenium, django-behave, sqlparse, django-debug-toolbar, py, pytest, pytest-catchlog, coverage, pytest-cov, pytest-django, decorator, pytest-twisted, glob2, Mako, pytest-bdd
Successfully installed Django-1.10.1 Mako-1.0.4 Markdown-2.6.6 MarkupSafe-0.23 Pillow-3.3.1 behave-1.2.5 coverage-4.2 decorator-4.0.10 django-behave-0.1.5 django-debug-toolbar-1.5 django-environ-0.4.0 ecdsa-0.13 glob2-0.4.1 paramiko-1.17.2 parse-1.6.6 parse-type-0.3.4 py-1.4.31 pycrypto-2.6.1 pytest-3.0.2 pytest-bdd-2.17.1 pytest-catchlog-1.2.2 pytest-cov-2.3.1 pytest-django-3.0.0 pytest-twisted-1.5 selenium-2.53.6 six-1.10.0 sqlparse-0.2.1


```
