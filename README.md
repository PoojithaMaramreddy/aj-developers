# AJ Developers

## Real Estate Sales & Lead Management Platform

AJ Developers is a real-world real estate web platform focused initially on open-plot projects in Hyderabad and surrounding areas.

The platform is designed to support property discovery, lead generation, site visits, booking requests, sales follow-up, communication and future automation.

It is also being developed as a professional portfolio and GitHub project.

---

## Project Objectives

- Build a professional real estate website for AJ Developers.
- Showcase current and future property projects.
- Generate and manage customer leads.
- Allow customers to enquire about projects and individual plots.
- Allow customers to request site visits.
- Allow customers to submit booking requests.
- Integrate WhatsApp as a primary communication channel.
- Provide an admin interface for business operations.
- Support future automation, analytics and CRM integration.
- Keep the architecture simple, maintainable and scalable.

---

## Current Business Scope

### Current Property Type

- Open Plots

### Future Property Types

- Villas
- Apartments
- Commercial Spaces
- Other property categories

### Current Projects

- 6 ventures initially

The system must support adding more projects without requiring code changes for normal project content management.

---

## Project Lifecycle

1. Requirement Analysis — Completed
2. Planning — Completed
3. Design — Completed
4. Implementation — In Progress
5. Testing — Pending
6. Deployment — Pending
7. Maintenance — Pending

---

## Technology Stack

### Backend

- Python
- Django
- Django ORM

### Database

- MySQL

### Frontend

- HTML
- CSS
- Bootstrap
- JavaScript where required

### Development & Version Control

- Git
- GitHub

### Integrations & Future Technologies

- REST APIs
- WhatsApp integration
- Automation platforms
- Managed services
- Analytics
- CRM integrations

The project follows a pragmatic technology strategy.

AI tools, APIs, automation platforms, plugins, managed services and third-party services may be used whenever they provide practical value and reduce unnecessary custom development.

The project should avoid unnecessary complexity and overengineering.

---

## Current Implementation Status

The initial Django and database foundation has been completed.

### Completed

- Python development environment setup
- Virtual environment setup
- Django project setup
- Django 5.2.17 configured
- MySQL database configured
- Django ORM configured
- Environment variable configuration using `.env`
- `.env.example` added
- Git repository initialized
- GitHub repository connected
- Initial project pushed to GitHub
- `core` Django application created
- `Project` model created
- Project model migration created and applied
- Django Admin configured
- Project management through Django Admin tested
- Basic Django ORM operations tested

### Currently Working On

- Reviewing and finalizing the `Project` data model
- Creating project-related models
- Building the project management foundation

### Not Yet Implemented

- Public website frontend
- Project listing pages
- Project detail pages
- Project image/gallery management
- Project videos
- Amenities
- Approvals and legal documents
- Plot enquiry workflow
- Lead management
- Site visit requests
- Booking requests
- WhatsApp integration
- Sales follow-up system
- Campaign management
- Analytics dashboard
- Production deployment

---

## Architecture Principles

### Data-Driven Projects

The six current ventures are treated as data, not separate code.

Adding a future project should normally be possible through the admin interface without modifying application code.

### ORM-Based Database Access

Django ORM is used for application-level database operations.

The system should avoid unnecessary raw SQL and use efficient ORM queries where practical.

### No Public Pricing

Project pricing will not be publicly displayed.

Customers can contact AJ Developers for current pricing and project information.

### No Public Plot Availability

The website will not expose public Available, Reserved or Sold plot status in Phase 1.

Customers can enquire about a specific plot or submit a booking request.

Current availability will be confirmed by AJ Developers.

### Booking Requests

Phase 1 supports booking requests rather than online payment or automatic booking confirmation.

Booking flow:

Select Plot → Book This Plot → Submit Details → Booking Request → AJ Developers Contact → Confirmation & Documentation

---

## Documentation

Project documentation is maintained inside the `docs/` directory.

Current documentation:

- `docs/requirements.md`
- `docs/planning.md`
- `docs/design.md`

Additional documentation files will be created only when they become necessary.

Documentation principle:

> Need → Create → Use → Maintain

---

## Development Philosophy

Build a reliable and practical system first.

Do not build infrastructure or features simply because they are technically possible.

Features should be added when they provide real business value, improve the customer experience, improve maintainability, or provide meaningful portfolio value.

The system should remain simple during the initial development stages and evolve as real business requirements grow.

---

## Responsive Design

The website is intended to provide a single responsive experience across:

- Mobile phones
- Tablets
- Laptops
- Desktop computers
- Large screens

The design will follow a mobile-first approach with:

- Touch-friendly interfaces
- Simple enquiry forms
- Click-to-call functionality
- WhatsApp integration
- Site visit actions
- Mobile-friendly navigation
- Responsive images
- Basic accessibility considerations

---

## Customer Journey

The planned customer journey is:

```text
Website
   ↓
Project Discovery
   ↓
Project Details
   ↓
Enquiry / WhatsApp / Call
   ↓
Lead Created
   ↓
Follow-up
   ↓
Site Visit
   ↓
Booking Request
   ↓
Documentation & Confirmation