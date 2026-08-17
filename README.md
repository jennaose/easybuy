# Easy Buy

EasyBuy is a web-based purchasing platform built with Python, Django, and Django REST Framework (DRF). The project is designed to allow users to browse products, manage accounts, and interact with a backend API for purchasing-related operations.

The project uses a structured REST API architecture, with Django handling the backend logic, database models, authentication, serialization, and API routing.

## Main technologies
   - Python
   - Django
   - Django REST Framework (DRF)
   - PostgreSQL/SQLite depending on your development setup
   - JWT authentication using Simple JWT
   - RESTful API architecture
   - Key components you worked on

1. Authentication

   - User registration/login functionality
   - JWT-based authentication
   - Access and refresh tokens
   - Token endpoints such as:
   - /api/token/
   - /api/token/refresh/

2. API structure
The project separates the API from the main Django configuration, while working with routes such as:

/
   ├── admin/
   ├── api/
   ├── api/token/
   └── api/token/refresh/

3. Django models
   Worked with Django models to represent the application's data and relationships. The models form the foundation for storing users, products, orders/purchases, and other EasyBuy-related information.

4. Serializers
   Utilized DRF serializers to:

   - Convert Django model instances into JSON
   - Validate incoming API data
   - Handle nested/related data
   - Control what information is exposed through the API

5. View/API logic
The backend uses DRF views/viewsets to process requests and return API responses. This gives EasyBuy a frontend-independent backend that can communicate with a web or mobile client.

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
5. Visit the app

## Notes

- The profile API requires JWT authentication via the `Authorization: Bearer <access_token>` header.
- The browser-facing pages are designed to allow clicking through users without using curl or environment variables.

## Cloudinary (image hosting)

This project can be configured to upload and serve media (images) from Cloudinary instead of local filesystem storage. To enable Cloudinary storage:

1. Install the required packages in your virtual environment:

```bash
pip install cloudinary django-cloudinary-storage
```

2. Provide your Cloudinary credentials via environment variables (do NOT commit secrets to the repository):

- `CLOUDINARY_STORAGE_CLOUD_NAME` — your Cloudinary cloud name
- `CLOUDINARY_STORAGE_API_KEY` — your Cloudinary API key
- `CLOUDINARY_STORAGE_API_SECRET` — your Cloudinary API secret

Alternatively you may set a single `CLOUDINARY_URL` environment variable (format: `cloudinary://API_KEY:API_SECRET@CLOUD_NAME`).

3. With the environment variables set, Django will use Cloudinary for file storage automatically. Uploaded ImageField files (e.g., avatars, listing images) will be stored in Cloudinary.

4. For development without Cloudinary, files will continue to be saved under the local `media/` directory.

Security note: Treat your Cloudinary API key/secret like a password. Use environment variables or a secrets manager in production.

