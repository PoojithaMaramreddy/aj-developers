# AJ Developers

## Real Estate Sales & Lead Management Platform

AJ Developers is a real estate web platform for open-plot projects in Hyderabad and surrounding areas. Visitors can browse projects, send enquiries, request site visits and submit booking requests. The team manages project content, leads and follow-ups through Django Admin.

---

## Features

### Public website

- **Home page** with hero section, property categories, featured projects, about and contact sections.
- **Project listing** showing all published projects.
- **Project detail pages** with:
  - Hero image, location, total area and project-level number of plots where applicable
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
- **Sales agents and follow-ups:** assign follow-ups such as calls, WhatsApp messages, site visits and emails with date, notes and status.
- **WhatsApp opt-in** captured on the enquiry form.
- Leads, site visits, booking requests and follow-ups can be searched and filtered in the admin.

### Content management (Django Admin)

Projects are data, not code. A new project is added entirely through the admin: details, images, videos, amenities and approvals are managed from the project page.

Projects have `Draft`, `Published` and `Archived` states, and only published projects appear on the website.

The platform does **not** manage individual plot records, plot inventory, plot numbers or individual plot selection.

### Data models in place for future automation

`Campaign` and `CampaignRecipient` models exist and can be managed in the admin, but **messages are not sent automatically yet**.

---

## Business Rules

- **No public pricing.** Customers contact AJ Developers for current prices.
- **No individual plot inventory management.** The system does not manage individual plot records or show individual plot availability such as Available, Reserved or Sold. Project availability is confirmed by the AJ Developers team.
- **Booking requests, not online payments.** The booking flow is:

  `Select Project → Submit Details → Booking Request → AJ Developers Contact → Confirmation & Documentation`

- Project-level information such as the **number of plots in a development** may be displayed as descriptive project information where applicable. It is not used as individual plot inventory.

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

```text
aj-developers/
├── config/              # Django project settings, URLs, WSGI/ASGI
├── core/                # Main app: models, views, admin, migrations
├── templates/
│   ├── base.html        # Shared layout (navbar, footer)
│   └── core/            # Home, projects and project detail templates
├── static/              # CSS and site assets
├── projects/images/     # Project image assets
├── docs/                # Requirements, planning and design documentation
├── .env.example         # Environment variable template
├── manage.py
└── requirements.txt
```

---

## URLs

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
source .venv/Scripts/activate        # Windows
# source .venv/bin/activate          # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create the MySQL database
mysql -u root -p -e "CREATE DATABASE ajdevelopers CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# 5. Configure environment variables
copy .env.example .env               # Windows
# cp .env.example .env               # macOS/Linux
# Then edit .env with your values

# 6. Apply migrations
python manage.py migrate

# 7. Create an admin user
python manage.py createsuperuser

# 8. Run the development server
python manage.py runserver
```

Open `http://127.0.0.1:8000/` for the site and `http://127.0.0.1:8000/admin/` for the admin.

Projects appear on the website only when their status is set to **Published**.

---

## Environment Variables

Set these in `.env`. **Never commit this file.**

| Variable | Required | Description |
|----------|----------|-------------|
| `DB_NAME` | Yes | MySQL database name |
| `DB_USER` | Yes | MySQL username |
| `DB_PASSWORD` | Yes | MySQL password |
| `DB_HOST` | Yes | Database host, for example `127.0.0.1` |
| `DB_PORT` | Yes | Database port, for example `3306` |
| `SECRET_KEY` | Production | Django secret key |
| `DEBUG` | Production | Defaults to `True`; set to `False` in production |
| `ALLOWED_HOSTS` | Production | Comma-separated hostnames |
| `EMAIL_BACKEND` | Optional | Defaults to the console backend |

When `DEBUG=False`, the application enables HTTPS redirect, secure cookies, HSTS and related security settings.

---

## Production Notes

Before deploying:

1. Set `DEBUG=False`, a strong `SECRET_KEY`, and appropriate `ALLOWED_HOSTS`.
2. Run:

   ```bash
   python manage.py check --deploy
   ```

   and address any warnings.
3. Run:

   ```bash
   python manage.py collectstatic
   ```

4. Serve static files using an appropriate production setup such as WhiteNoise or Nginx.
5. Run Django with a production WSGI server such as Gunicorn.
6. Uploaded files such as brochures, layouts, project images and approval documents are stored in `media/`. Configure persistent storage and production media serving before deployment.
7. Use a managed or regularly backed-up MySQL database.
8. Make sure `.env` is never committed.
9. Configure domain, HTTPS, email and other production services before going live.

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
| Testing | Pending — automated test coverage is not yet implemented |
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
- Additional property types such as villas, apartments and commercial spaces

---

## Development Philosophy

Build a reliable and practical system first.

Add features when they provide real business value, improve the customer experience or improve maintainability—not simply because they are technically possible.

Use technology, AI and automation where they provide clear value. Prefer simple, maintainable solutions and use no-code or low-code tools where appropriate instead of adding unnecessary custom code.

Keep the architecture simple and let the platform evolve with real business needs.