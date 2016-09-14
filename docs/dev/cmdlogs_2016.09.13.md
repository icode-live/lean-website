git config --global push.default simple

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

$ git push --set-upstream origin development

$ git config --global credential.helper cache
so we only type credential once


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

$ git add -A
(lean-icode) tac@yoshiki ~/Work/icode/lean-website $ git status
On branch development
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   .gitignore
	new file:   docs/dev/cmdlogs_2016.09.13.md

$ git commit -m "doc folder for project Design and Technical logs, and my default ignore file"
[development 6a549af] doc folder for project Design and Technical logs, and my default ignore file
 2 files changed, 157 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 docs/dev/cmdlogs_2016.09.13.md


$ git push --set-upstream origin development
Username for 'https://github.com': icode-live
Password for 'https://icode-live@github.com':
Counting objects: 6, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 2.23 KiB | 0 bytes/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To https://github.com/icode-live/lean-website.git
 * [new branch]      development -> development
Branch development set up to track remote branch development from origin


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

clone djangorestframework and replace == with >= in all requirement files, then

```
$ pip install -r requirements.txt

Successfully built django-guardian coreapi transifex-client pypandoc itypes mkdocs-bootstrap PyYAML click tornado livereload clint args
Installing collected packages: django-guardian, django-filter, requests, itypes, uritemplate, coreapi, mkdocs-bootstrap, PyYAML, click, tornado, Jinja2, mkdocs-bootswatch, livereload, mkdocs, pyflakes, mccabe, pycodestyle, flake8, pep8, isort, requests-toolbelt, args, clint, pkginfo, twine, urllib3, transifex-client, pypandoc
Successfully installed Jinja2-2.8 PyYAML-3.12 args-0.1.0 click-6.6 clint-0.5.1 coreapi-2.0.0 django-filter-0.14.0 django-guardian-1.4.6 flake8-3.0.4 isort-4.2.5 itypes-1.1.0 livereload-2.4.1 mccabe-0.5.2 mkdocs-0.15.3 mkdocs-bootstrap-0.1.1 mkdocs-bootswatch-0.4.0 pep8-1.7.0 pkginfo-1.3.2 pycodestyle-2.0.0 pyflakes-1.2.3 pypandoc-1.2.0 requests-2.11.1 requests-toolbelt-0.7.0 tornado-4.4.1 transifex-client-0.12.2 twine-1.8.1 uritemplate-3.0.0 urllib3-1.17

```


