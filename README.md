# Welcome to Bangazon

This web application is the source code for the Bangazon e-commerce web site. It is powered by Python and Django.

Students, you are inheriting a basic implementation that provides the following features:

1. User registration 
1. User login 
1. User logout 
1. Adding a product 
1. Listing products

Please consult the backlog of issues and work with your product owner to implement the top priority tickets for your sprints.

## To begin work

1. The team lead should clone this repository, then push it to your team's Github repo.
1. Alert your manager when this is complete and all backlog issues will be imported into your project.
1. Each teammate should clone the repository.
1. In the `djangazon` directory that gets created, run the migrations with `python manage.py migrate`

## Helpful Resources

### Django Models and Migrations

Using the requirements above create a [model](https://docs.djangoproject.com/en/1.10/topics/db/models/) for each resource, and use [migrations](https://docs.djangoproject.com/en/1.10/topics/migrations/) to ensure your database structure is up to date.

### Templates

[Django template language](https://docs.djangoproject.com/en/1.10/ref/templates/language/)

### Form Helpers

Django, like Angular, has many built-in [helper tags and filters](https://docs.djangoproject.com/en/1.10/ref/templates/builtins/) when building the site templates. We strongly recommend reading this documentation while building your templates.


## To Run

1. Clone the repo.
1. Start your virtual environment
1. From the command line, cd into the root directory (wherever the manage.py file is located).
1. Type ```python manage.py runserver``` into the command line.
1. Open a web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Naming Conventions

1. All branches to have lowercase initials 
1. File name to match class name and describe use 
1. Every function and class needs a docstring
1. Every model class needs a dunderscore string (__str__)
1. All model names and field names should match the ERD exactly

```
Ex. js_(branch_feature)
Employee_Model.py -> class Employee_Model
Employee_View.py -> class Employee_View
```

## Pull Request Conventions

1. Pull requests should include a list of which files were added, modified, or deleted in this PR so we can check for conflicts and scope of change.

## Remigrating

Assuming you've put the script in your file, running ```pyremigrate website```