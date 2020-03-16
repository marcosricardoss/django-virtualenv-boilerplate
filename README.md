### Django Virtual Environment Project Boilerplate

This Django application is a pre-configured project with a well-done file structure. Use this boilerplate to quickly start you new Django projects.

#### The Virtual Environment 

This boilerplate is meant to be used in Virtual Environment. See below the nice suggestion of a file structure for it:

  .
  ├── commands
  ├── dumps
  ├── project
  └── venv

`commands`: local shell scripts that are related to the project.
`dumps`: directory for database dumps.
`project`: your Django project.
`venv`: virtual environment directory.

#### Project Structure

  .
  ├── **externals**
  ├── **locale**
  ├── magazine
  ├── **media**
  ├── **myproject**
  ├── **requirements**
  ├── **site_static**
  ├── **static**
  ├── **templates**
  ├── **tmp**
  ├── **utils**
  ├── .gitignore
  ├── LICENSE.md
  ├── manage.py
  └── README.md

- `externals`: directory for include external dependencies directly within your project.
- `locale`: directory for your project translations.
- `media`: project uploads.
- `myproject`: project's Python package.
- `requirements`: directory for requirements txt files.
- `site_static`: project-specific static files.
- `static`: collected static files.
- `templates`: directory for project templates.
- `tmp`: directory for the upload procedure.
- `utils`: for different functionalities that are shared throughout the project.