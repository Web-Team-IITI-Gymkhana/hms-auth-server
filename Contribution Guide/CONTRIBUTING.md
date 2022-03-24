# Note to the Contributors

### Change in Environment Variables
Change in environment variables must be accompanied with changes in helper/create_env.py and server/config.py files.

### Newly Installed Packages
Newly installed packages must be written into the requirements.txt file.
Using the command `pip freeze --exclude-editable > requirements.txt` in the parent directory.  
You can also use `python manage.py -f requirements.txt` rather.

### To Create New Apps
To create new apps, (eg. "Hostel"), write the following in the parent directory.  
`python manage.py -a <app_name>`

### New Models
While creating new models, or updating the existing ones, schemas must be created or updated. The Base needs to be added to the `migrations/env.py` file if not present. To reflect those changes in the database, the following commands need to be run.  
`alembic revision --autogenerate -m "Comment about the changes"`  
`alembic upgrade heads`  
You can also use `python manage.py -m "<Comment>"` rather.

### To Reset Database
To reset the database, run the following commands.  
`alembic downgrade base`  
`alembic upgrade heads`  
You can also use `python manage.py -r` rather.

### To update the database
In order to update the database after each pull, run the following command.  
`alembic upgrade heads`

### To test
To test the API Endpoints, filenames, functions must start with `test_`, whereas classes must start with `Test`. To run pytest, run the following command in the parent directory.  
`pip install -e .`  
`pytest`  
You can also use `python manage.py -t` rather.