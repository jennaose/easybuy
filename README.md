# Easy Buy

Easy Buy is a Django+DRF project for a marketplace-style application.

## What was added today

- Added a browser-friendly homepage with direct links to key app sections.
- Added a browser-based user list page at `/users/`.
- Added a browser-based active user detail page at `/users/<id>/`.
- Kept API functionality for:
  - `GET /api/users/` — active users list
  - `GET /api/users/profile/` — authenticated current user profile
  - `POST /api/users/register/` — user registration
  - `POST /api/token/` and `POST /api/token/refresh/` — JWT authentication
- Added tests for the user API views and homepage.

## Quick start

1. Create and activate a Python virtual environment.
2. Install dependencies (if requirements are available).
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver 127.0.0.1:8000
   ```
5. Visit the app:
   - Homepage: `http://127.0.0.1:8000/`
   - Browser users list: `http://127.0.0.1:8000/users/`
   - API user list: `http://127.0.0.1:8000/api/users/?format=json`
   - Profile endpoint: `http://127.0.0.1:8000/api/users/profile/?format=json`

## Notes

- The profile API requires JWT authentication via the `Authorization: Bearer <access_token>` header.
- The browser-facing pages are designed to allow clicking through users without using curl or environment variables.
