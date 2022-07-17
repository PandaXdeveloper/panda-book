# Panda Book

## Backend

- Go to directory that have manage.py file

  ```bash
  cd backend
  ```

- Create virtual environments

  ```bash
  python3 -m venv venv
  ```

- Activate virtual environments

  ```bash
  source venv/bin/activate
  ```

- Create new migrations

  ```bash
  python3 manage.py makemigrations
  ```

- Apply migrations

  ```bash
  python3 manage.py migrate
  ```

- Run server

  ```bash
  python3 manage.py runserver
  ```
