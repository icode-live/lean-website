
## Project Description

We want a lean django project (one module project)

It will be a personal  webpage site with landing page and most static information on that one page.

It will have a REST_API to query the website for specific categories, sections ...

It will host a simple tech how-to blog (Python3, Javacript, HTML5 Canvas games)

## dev notes

Settings are in it's own file to keep thing clean.

Our file structure look like this for now.

```
../
├── docs
│   └── dev
│       ├── cmdlogs_2016.09.13.md
│       └── design_2016.09.13.md
├── leanwebsite
│   ├── conftest.py
│   ├── __init__.py
│   ├── manage.py
│   ├── pytest.ini
│   ├── settings.py
│   ├── static
│   ├── templates
│   └── test_settings.py
├── LICENSE
└── README.md
```
The main file is called *manage.py* because it is still through
this module that we access django commands from the CLI with
`execute_from_command_line(sys.argv)`


