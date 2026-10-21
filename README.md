
# AJ Developers — Real Estate Sales & Lead Management Platform

AJ Developers is a full-stack real estate web application built using **Python, Django, MySQL, HTML, CSS, and JavaScript**.

The platform allows visitors to explore real estate projects, submit enquiries, request site visits, and send booking requests. It also provides an internal lead management workflow through Django Admin, helping the team organize customer enquiries, track follow-ups, and manage project information.

**Project Status:** Core implementation completed | Automated testing and deployment pending

## Tech Stack

| Layer | Technologies |
|-------|-------------|
| Backend | Python, Django 5.2, Django ORM |
| Database | MySQL |
| Frontend | HTML, CSS, JavaScript, Django Templates |
| Configuration | django-environ |
| Image Processing | Pillow |
| Version Control | Git, GitHub |

## Key Features

### 1. Property Listings and Project Management

- Display published real estate projects.
- View project details, locations, images, amenities, and brochures.
- Access layout documents and Google Maps links.
- Manage project information through Django Admin.
- Support Draft, Published, and Archived project statuses.
- Display only published projects on the public website.

### 2. Customer Enquiries and Booking Requests

- Submit enquiries for individual projects.
- Request property site visits.
- Submit booking requests.
- Use click-to-call and WhatsApp contact options.
- Associate submitted requests with the relevant real estate project.

Booking requests are handled by the sales team. The platform does not process online payments.

### 3. Lead Management

- Automatically create leads from website enquiries.
- Associate leads with their respective projects.
- Prevent duplicate leads for the same phone number and project.
- Update repeat enquiries without overwriting the original customer name or resetting lead status.
- Track leads through multiple sales stages.
- Search and filter lead records through Django Admin.

### 4. Sales Follow-up Management

- Track customer follow-up activities.
- Record calls, WhatsApp messages, site visits, and emails.
- Assign follow-ups to sales agents.
- Maintain follow-up dates, notes, and statuses.
- Link site visits and booking requests to customer leads.

### 5. Responsive User Interface

- Responsive layouts for desktop and mobile devices.
- Project listing and project detail pages.
- Image galleries and downloadable project documents.
- Enquiry, site visit, and booking request forms.

## Application Workflow

### Customer Journey

1. A visitor opens the website.
2. The visitor explores available real estate projects.
3. The visitor selects a project and views its details.
4. The visitor submits an enquiry, site visit request, or booking request.
5. The system records the request and associates it with a lead.
6. The sales team reviews and follows up through Django Admin.

### Administrative Workflow

1. Create or update real estate project information.
2. Publish projects for public viewing.
3. Review customer enquiries and requests.
4. Track lead statuses.
5. Assign and manage follow-up activities.
6. Update site visit and booking request statuses.

## Important Business Rules

- Project prices are not displayed publicly.
- Booking requests do not involve online payments.
- Individual plot inventory and plot selection are not managed by the system.
- Project availability is confirmed by the sales team.
- Campaign and campaign-recipient models exist, but automated message sending is not implemented.

## Application Architecture

The application follows Django's Model-View-Template architecture.

- **Models:** Represent real estate projects, leads, enquiries, site visits, booking requests, and related records.
- **Views:** Handle application requests, business logic, and form submissions.
- **Templates:** Render the public-facing website.
- **Django Admin:** Provides internal project and lead management interfaces.
- **MySQL:** Stores application data using Django ORM.

## Project Structure

```text
aj-developers/
├── config/              # Django settings, URLs and application configuration
├── core/                # Models, views, admin configuration and migrations
├── templates/           # Django HTML templates
├── static/              # CSS, JavaScript and static assets
├── projects/images/     # Project image assets
├── docs/                # Requirements, planning and design documentation
├── .env.example         # Environment variable template
├── manage.py
├── requirements.txt
└── README.md
```

## Local Installation

### Prerequisites

- Python 3.10+
- MySQL 8+
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/PoojithaMaramreddy/aj-developers.git
cd aj-developers
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Or on macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Create a MySQL database named `ajdevelopers`, or configure another database name through environment variables.

### 5. Configure Environment Variables

Copy `.env.example` to `.env` and configure:

- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT
- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS

Never commit the `.env` file or real credentials.

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create an Admin User

```bash
python manage.py createsuperuser
```

### 8. Start the Development Server

```bash
python manage.py runserver
```

Open:

- Website: http://127.0.0.1:8000/
- Django Admin: http://127.0.0.1:8000/admin/

Projects must be marked as Published to appear on the public website.

## Testing and Deployment Status

| Development Phase | Status |
|-------------------|--------|
| Requirements Analysis | Completed |
| Planning and Design | Completed |
| Core Application Development | Completed |
| Automated Testing | Pending |
| Production Deployment | Pending |
| Maintenance | Not started |

**Deployment:** The application currently runs in a local development environment. A public production URL is not yet available.

Before production deployment, the application requires appropriate Django security settings, production static and media storage, a hosted MySQL database, and deployment validation.

## Documentation

Additional project documentation is available in the `docs/` directory:

- `docs/requirements.md`
- `docs/planning.md`
- `docs/design.md`

## Future Enhancements

- Automated testing for models, views, and form submissions
- Production deployment
- Automated follow-up reminders
- WhatsApp Business API integration
- Lead analytics dashboard
- Spam protection and rate limiting
- Additional real estate property categories

## Skills Demonstrated

- Python and Django web development
- Django ORM and MySQL integration
- Database-backed application development
- Model-View-Template architecture
- CRUD operations
- Form processing and validation
- Lead management and business workflow implementation
- Django Admin customization
- Responsive frontend development
- Git and GitHub version control

## Project Summary

AJ Developers demonstrates the development of a database-driven real estate application that connects public property listings and customer enquiries with internal lead management workflows.

The core application is implemented, while automated testing and public deployment remain planned improvements.
