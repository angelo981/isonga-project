# ISONGA CENTRE Django Website Starter

This is a development-ready Django starter structure for the ISONGA CENTRE website.

## Included
- Django project structure
- Core app with views, urls, forms
- Reusable base template
- Section-by-section templates for all main pages
- Simple styling file

## Suggested setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install django
cd isonga_django_site
python manage.py migrate
python manage.py runserver
```

## Project structure
- `isonga_site/` project config
- `core/` main website app
- `core/templates/core/` HTML templates
- `core/static/core/css/styles.css` site styles

## Pages included
- Home
- About
- Programs
- Events
- Talent & Success Stories
- Partnerships
- Media & Gallery
- News & Blog
- Contact

## Notes
- Replace placeholders such as email, phone, and images.
- Connect forms to your preferred email backend or CRM.
- Add models/admin if you want dynamic event, blog, and gallery management.
