# AJ Developers

## Real Estate Sales & Lead Management Platform

AJ Developers is a real estate web platform for open-plot projects in Hyderabad and surrounding areas. Visitors can browse projects, send enquiries, request site visits and submit booking requests. The team manages all content, leads and follow-ups from the Django Admin.

---

## Features

### Public website

- **Home page** with hero section, property categories, featured projects, about and contact sections.
- **Project listing** showing all published projects.
- **Project detail pages** with:
  - Hero image, location, total area and total plots
  - Image gallery and YouTube video links
  - Amenities
  - Approvals and legal documents
  - Layout image / layout PDF and downloadable brochure
  - Google Maps link
- **Enquiry form**, **site visit request form** and **booking request form** on every project page.
- **Click-to-call and WhatsApp buttons** across the site, with project-specific prefilled WhatsApp messages.
- Responsive, mobile-first layout built with custom HTML and CSS.

### Lead management (Django Admin)

- **Automatic lead creation** from website forms, with the source set to `WEBSITE`.
- **Duplicate protection:** one lead per phone number and project. A repeat submission updates the existing lead instead of creating a new one, and never overwrites the original name or resets its status.
- **Status tracking:** New → Contacted → Interested → Site Visit Scheduled → Site Visit Done → Booking Requested → Booked → Closed / Not Interested.
- **Site visits and booking requests** linked to leads, each with their own status workflow.
- **Sales agents and follow-ups:** assign follow-ups (call, WhatsApp, site visit, email) with date, notes and status.
- **WhatsApp opt-in** captured on the enquiry form.
- Leads, site visits, booking requests and follow-ups can be searched and filtered in the admin.

### Content management (Django Admin)

Projects are data, not code. A new project is added entirely through the admin: details, images, videos, amenities, approvals and plots are all edited inline on the project page. Projects have `Draft`, `Published` and `Archived` states, and only published projects appear on the website.

### Data models in place for future automation

`Campaign` and `CampaignRecipient` models exist and can be managed in the admin, but **messages are not sent automatically yet** (see [Roadmap](#roadmap)).

---

## Business Rules

- **No public pricing.** Customers contact AJ Developers for current prices.
- **No public plot availability.** The site does not show Available, Reserved or Sold status. Availability is confirmed by the team.
- **Booking requests, not online payments.** The booking flow is:

  `Book This Plot → Submit Details → Booking Request → AJ Developers Contact → Confirmation & Documentation`

---

## Technology Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Django 5.2, Django ORM |
| Database | MySQL |
| Frontend | Django templates, custom CSS, JavaScript, Font Awesome |
| Config | `django-environ` (`.env` file) |
| Images | Pillow |
| Version control | Git, GitHub |

---

## Project Structure

```
aj-developers/
├── config/              # Django project settings, URLs, WSGI/ASGI
├── core/                # Main app: models, views, admin, migrations
├── templates/
│   ├── base.html        # Shared layout (navbar, footer)
│   └── core/            # home, projects, project_detail
├── static/              # CSS and site images
├── projects/images/     # Project image assets
├── docs/                # requirements.md, planning.md, design.md
├── .env.example         # Environment variable template
├── manage.py
└── requirements.txt
```

### URLs

| URL | Purpose |
|-----|---------|
| `/` | Home page |
| `/projects/` | Published projects |
| `/projects/<slug>/` | Project detail |
| `/projects/<slug>/enquiry/` | Enquiry form submission (POST) |
| `/projects/<slug>/site-visit/` | Site visit request submission (POST) |
| `/projects/<slug>/booking-request/` | Booking request submission (POST) |
| `/admin/` | Django Admin |

---

## Local Setup

### Prerequisites

- Python 3.10+
- MySQL 8+
- Git

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/PoojithaMaramreddy/aj-developers.git
cd aj-developers

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create the MySQL database
mysql -u root -p -e "CREATE DATABASE ajdevelopers CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# 5. Configure environment variables
cp .env.example .env             # then edit .env with your values

# 6. Apply migrations
python manage.py migrate

# 7. Create an admin user
python manage.py createsuperuser

# 8. Run the development server
python manage.py runserver
```

Open http://127.0.0.1:8000/ for the site and http://127.0.0.1:8000/admin/ for the admin.

Projects appear on the website only when their status is set to **Published**.

---

## Environment Variables

Set these in `.env` (never commit this file).

| Variable | Required | Description |
|----------|----------|-------------|
| `DB_NAME` | Yes | MySQL database name |
| `DB_USER` | Yes | MySQL username |
| `DB_PASSWORD` | Yes | MySQL password |
| `DB_HOST` | Yes | Database host (e.g. `127.0.0.1`) |
| `DB_PORT` | Yes | Database port (e.g. `3306`) |
| `SECRET_KEY` | Production | Django secret key. Falls back to an insecure development key if unset. |
| `DEBUG` | Production | Defaults to `True`. Set to `False` in production. |
| `ALLOWED_HOSTS` | Production | Comma-separated hostnames, e.g. `example.com,www.example.com` |
| `EMAIL_BACKEND` | Optional | Defaults to the console backend |

When `DEBUG=False`, the app automatically enables HTTPS redirect, secure cookies, HSTS and related security headers.

---

## Production Notes

Before deploying:

1. Set `DEBUG=False`, a strong `SECRET_KEY`, and `ALLOWED_HOSTS` for your domain.
2. Run `python manage.py check --deploy` and fix any warnings.
3. Run `python manage.py collectstatic`. Static files are collected into `staticfiles/`.
4. Serve static files (for example with WhiteNoise or Nginx) and run the app with a WSGI server such as Gunicorn. These are not included in `requirements.txt` yet.
5. Uploaded files (brochures, layouts, project images, approval documents) are stored in `media/`. Django only serves media in development (`DEBUG=True`), so configure your web server or object storage to serve it in production, and keep it on persistent storage.
6. Use a managed or regularly backed-up MySQL database.
7. Make sure `.env` is never committed.

---

## Documentation

Detailed project documentation lives in `docs/`:

- `docs/requirements.md`
- `docs/planning.md`
- `docs/design.md`

---

## Project Status

| Phase | Status |
|-------|--------|
| Requirement analysis | Completed |
| Planning | Completed |
| Design | Completed |
| Implementation | Completed |
| Testing | Pending (no automated tests yet) |
| Deployment | Pending |
| Maintenance | Pending |

---

## Roadmap

Planned for future phases:

- WhatsApp Business API integration and automated campaign sending
- Automated follow-up reminders and lead notifications
- Spam protection and rate limiting on public forms
- Automated tests
- Analytics dashboard
- CRM integrations
- Additional property types: villas, apartments, commercial spaces

---

## Development Philosophy

Build a reliable and practical system first. Add features when they provide real business value, improve the customer experience or improve maintainability, not simply because they are technically possible. Keep the architecture simple and let it evolve with real business needs.
