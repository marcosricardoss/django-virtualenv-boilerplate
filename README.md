### Django Virtual Environment Project Boilerplate

This Django application is a pre-configured project with a well-done file structure. Use this boilerplate to quickly start you new Django projects.

#### Virtual Environment File Structure

See below a file structure suggestion to use this boilerplate in a virtual environment.

    .
    ├── commands
    ├── dumps
    ├── project
    └── venv

- `commands`: local shell scripts that are related to the project.
- `dumps`: directory for database dumps.
- `project`: your Django project.
- `venv`: virtual environment directory.

#### Project Structure

    .
    ├── externals
    │   ├── apps
    │   ├── libs
    │   └── README.md
    ├── LICENSE.md
    ├── locale
    │   └── README.md
    ├── magazine
    │   ├── admin.py
    │   ├── app_settings.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   ├── models.py
    │   ├── README.md
    │   ├── signals.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    ├── media
    │   └── README.md
    ├── myproject
    │   ├── asgi.py
    │   ├── config
    │   ├── db.sqlite3
    │   ├── __init__.py
    │   ├── README.md
    │   ├── settings.py
    │   ├── settings.py.example
    │   ├── urls.py
    │   └── wsgi.py
    ├── README.md
    ├── requirements
    │   ├── base.txt
    │   ├── dev.txt
    │   ├── prod.txt
    │   ├── README.md
    │   ├── staging.txt
    │   └── test.txt
    ├── site_static
    │   ├── README.md
    │   └── site
    ├── static
    │   └── README.md
    ├── templates
    │   └── README.md
    ├── tmp
    │   ├── __init__.py
    │   └── README.md
    └── utils
        ├── admin.py
        ├── apps.py
        ├── __init__.py
        ├── migrations
        ├── misc.py
        ├── models.py
        ├── README.md
        ├── tests.py
        └── views.py

- `externals`: directory for include external dependencies directly within your project.
- `locale`: directory for your project translations.
- `media`: project uploads.
- `myproject`: project's Python package.
- `requirements`: directory for requirements txt files.
- `site_static`: project-specific static files.
- `static`: collected static files.
- `templates`: directory for project templates.
- `tmp`: directory for the upload procedure.
- `utils`: app with different functionalities that are shared throughout the project.