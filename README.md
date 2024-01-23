### Hexlet tests and linter status:
[![Actions Status](https://github.com/SergeiNaum/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/SergeiNaum/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/00a61b463c5cc39bfcec/maintainability)](https://codeclimate.com/github/SergeiNaum/python-project-52/maintainability)
[![release](https://github.com/SergeiNaum/python-project-52/actions/workflows/release.yml/badge.svg)](https://github.com/SergeiNaum/python-project-52/actions/workflows/release.yml)


A task management web application built with Python and [Django](https://www.djangoproject.com/) framework. It allows you to set tasks, assign performers and change their statuses. Registration and authentication are required to work with the system.

To provide users with a convenient, adaptive, modern interface, the project uses the [Bootstrap](https://getbootstrap.com/) framework.

The frontend is rendered on the backend. This means that the page is built by the DjangoTemplates backend, which returns prepared HTML. And this HTML is rendered by the server.

[PostgreSQL](https://www.postgresql.org/) is used as the object-relational database system.


#### --> [Demo](http://77.222.53.154/) <--

### Details

For **_user_** authentication, the standard Django tools are used. In this project, users will be authorized for all actions, that is, everything is available to everyone.

Each task in the task manager usually has a **_status_**. With its help you can understand what is happening to the task, whether it is done or not. Tasks can be, for example, in the following statuses: _new, in progress, in testing, completed_.

**_Tasks_** are the main entity in any task manager. A task consists of a name and a description. Each task can have a person to whom it is assigned. It is assumed that this person performs the task. Also, each task has mandatory fields - author (set automatically when creating the task) and status.

**_Labels_** are a flexible alternative to categories. They allow you to group the tasks by different characteristics, such as bugs, features, and so on. Labels are related to the task of relating many to many.

When the tasks become numerous, it becomes difficult to navigate through them. For this purpose, a **_filtering mechanism_** has been implemented, which has the ability to filter tasks by status, performer, label presence, and has the ability to display tasks whose author is the current user.

---

### _Manual Install:_

There is always an option for those who like to do everything by themselves.

### Prerequisites

#### Python

Before installing the package make sure you have Python version 3.8 or higher installed:

```bash
>> python --version
Python 3.8+
```

#### Poetry

The project uses the Poetry dependency manager. To install Poetry use its [official instruction](https://python-poetry.org/docs/#installation).

#### PostgreSQL / SQLite

There are two main options for using a database management system for this project: **PostgreSQL** and **SQLite**.

PostgreSQL is used as the main database management system. You have to install it first. It can be downloaded from [official website](https://www.postgresql.org/download/) or installed using Homebrew:
```shell
>> brew install postgresql
```

_Alternatively you can skip this step and use **SQLite** database locally._

### Application

To use the application, you need to clone the repository to your computer. This is done using the `git clone` command. Clone the project:

```bash
>> git clone https://github.com/SergeiNaum/python-project-52.git && cd python-project-52
```

After that install all necessary dependencies:

```bash
>> make install
```

Create `.env` file in the root folder and add following variables:
```python-decuple
SECRET_KEY=django  secret key # Django will refuse to start if SECRET_KEY is not set
DB_ENGINE=django.db.backends.postgresql
DB_NAME=Your_db_name
DB_USER=your_db_uoser
DB_PASSWORD=Your_db_password
DB_HOST=localhost
DB_PORT=5432
LANGUAGE=en-us # By default the app will use ru-ru locale
```
_If you choose to use **SQLite** DBMS, do not add `DATABASE_URL` variable._

To create the necessary tables in the database, start the migration process:
```bash
>> make migrate
```

## Usage
```shell
>> make dev
```

The dev server will be at http://127.0.0.1:8000.

### Available Actions:

- **_Registration_** — First, you need to register in the application using the registration form provided;
- **_Authentication_** — To view the list of tasks and create new ones, you need to log in using the information from the registration form;
- **_Users_** — You can see the list of all registered users on the corresponding page. It is available without authorization. You can change or delete information only about yourself. If a user is the author or performer of a task, it cannot be deleted;
- **_Statuses_** — You can view, add, update, and delete task statuses if you are logged in. Statuses corresponding to any tasks cannot be deleted;
- **_Tasks_** — You can view, add, and update tasks if you are logged in. Only the task creator can delete tasks. You can also filter tasks on the corresponding page with specified statuses, performers, and labels;
- **_Labels_** — You can view, add, update, and delete task labels if you are logged in. Labels matching any tasks cannot be deleted.

---

## Additionally

### Dependencies

* python = "^3.11"
* django = "^4.2.7"
* python-decouple = "^3.8"
* django-bootstrap5 = "^23.3"
* django-filter = "^23.4"
* python-json-logger = "^2.0.7"
* rich = "^13.7.0"
* psycopg2 = "^2.9.9"
* gunicorn = "^21.2.0"
* rollbar = "^1.0.0"