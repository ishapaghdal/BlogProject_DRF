# Blog App


## Tasks Achieved

### Task-1: Authentication
- [x] A user is able to register & login using Email & Password. I have used JWT to implement this.
- [x] A user is able to update profile information.

### Task-2: Blogs
- [x] A user is able to create a draft of a blog.
- [x] A user is able to publish a draft blog.
- [x] A user is able to edit and delete a self-published blog.
- [x] All users is able to get the list of blogs published by anyone on the platform.
- [x] It support filters by Author, Category, and Tags.
- [x] It support filters by a textual search parameter.
- [x] It also support pagination.

### Task-3: Comments
- [x] All users are to add comments to a blog published by anyone on the platform.
- [x] A user are able to delete anyone’s comment on a self-published blog.


## Installation
To install the necessary dependencies, run the following commands:
```bash
python3 -m venv env
source env/bin/activate
```
```bash
git clone https://github.com/ishapaghdal/BlogProject_DRF
```
```bash
cd BlogProject_DRF
```
```bash
pip install -r requirements.txt
```

## Setup
Before running the project, you’ll need to set up the database and other environment variables:


Run database migrations to set up the tables:
```bash
python manage.py migrate
```

Create superuser for Django admin panel:
```bash
python manage.py createsuperuser
 ```

## Usage
To start the application, use the following command:
```bash
python manage.py runserver
```

## Test
You can test the backend by hitting the API endpoints. Here are some example endpoints you can use:

| **Action**       | **Method** | **Endpoint**            |
|------------------|------------|-------------------------|
| Generate tokens    | POST       | `/api/token/`    |
| Generate refresh tokens    | POST       | `/api/token/refresh/`    |
| Register User       | POST       | `/users/`       |
| Login User       | POST       | `/login/`       |
| Update Profile   | PUT        | `/users/{id}`     |
| Create Blog      | POST       | `/blogs/`           |
| Publish Blog     | PATCH      | `/blogs/publish`|
| Edit Blog        | PUT        | `/blogs/{id}`       |
| Delete Blog      | DELETE     | `/blogs/{id}`       |
| List Blogs       | GET        | `/blogs/`           |
| Blog Details     | GET        | `/blogs/{id}`       |
| Add Comment      | POST       | `/comment/{id}`|
| Get Comment      | GET       | `/comment/{id}`|
| Delete Comment   | DELETE     | `/comments/{id}`    |
