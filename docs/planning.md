# AJ Developers — Project Planning

## 1. Project Overview

AJ Developers is being developed as a real-world real estate website and sales/lead management platform.

The project is also intended to demonstrate practical software engineering skills in a professional portfolio/GitHub repository.

---

## 2. Project Goals

Primary goals:

1. Build a professional real estate website.
2. Generate customer enquiries.
3. Capture and manage leads.
4. Manage site visits.
5. Manage booking requests.
6. Support WhatsApp communication.
7. Provide an internal admin system.
8. Support analytics.
9. Allow future automation.
10. Maintain a simple and scalable architecture.

---

## 3. Seven-Phase Development Lifecycle

The project follows seven major phases:

### Step 1 — Requirement Analysis

Identify and document:

* Business requirements
* Customer requirements
* Functional requirements
* Non-functional requirements
* Legal requirements
* Security requirements
* Business workflows

Status: **Completed**

---

### Step 2 — Planning

Define:

* Technology direction
* Architecture approach
* Database planning
* Feature scope
* Admin requirements
* Communication strategy
* Analytics
* Testing
* Deployment approach

Status: **Completed**

---

### Step 3 — Design

Define:

* Sitemap
* Page layouts
* Wireframes
* UI/UX
* Design system
* Typography
* Colours
* Components
* Responsive behaviour
* Navigation
* CTA placement

Status: **Next**

---

### Step 4 — Implementation

Build:

* Django application
* Database models
* Django ORM queries
* Website pages
* Forms
* Admin
* Lead management
* Site visits
* Booking requests
* WhatsApp integration
* Analytics
* SEO
* Security

Status: **Pending**

---

### Step 5 — Testing

Test:

* Functional features
* Forms
* Lead flow
* Site visit flow
* Booking flow
* Admin functionality
* Permissions
* Database/ORM
* Responsive behaviour
* Browsers
* Security
* Performance
* SEO
* Links
* File uploads
* Backups
* Production smoke tests

Status: **Pending**

---

### Step 6 — Deployment

Deploy:

* Application
* Database
* Static files
* Media
* Domain
* HTTPS
* Environment variables
* Monitoring
* Backups

Preferred flow:

Local → GitHub → Staging → UAT → Production

Status: **Pending**

---

### Step 7 — Maintenance

After launch:

* Security updates
* Dependency updates
* Database backups
* Monitoring
* Content updates
* Project updates
* Performance checks
* Bug fixes
* Feature improvements

Status: **Pending**

---

# 4. Technology Strategy

## Preferred Stack

* Python
* Django
* Django ORM
* MySQL
* HTML
* CSS
* Bootstrap
* JavaScript where required

The stack is a preferred starting point rather than an excuse to avoid better tools.

Technology decisions should be based on:

* Business value
* Maintainability
* Cost
* Development speed
* Security
* Scalability
* Portfolio value

---

# 5. Pragmatic Technology Philosophy

The project should not attempt to code everything from scratch.

Where appropriate, use:

* AI tools
* APIs
* Automation platforms
* Plugins
* Existing libraries
* Managed services
* Cloud services
* Third-party integrations

The objective is to build a useful production system rather than maximize the amount of custom code.

---

# 6. Architecture Philosophy

Start simple.

Initial architecture should preferably be a modular Django application with:

* Django
* Django ORM
* MySQL
* Templates
* Bootstrap
* JavaScript where needed

Avoid unnecessary:

* Microservices
* Kubernetes
* Distributed systems
* Multiple application servers
* Complex infrastructure

Complexity should be introduced only when the business requires it.

---

# 7. Database Planning

Core planned entities:

* Project
* ProjectImage
* ProjectVideo
* Amenity
* ProjectApproval
* Plot
* Lead
* SiteVisit
* BookingRequest
* SalesAgent
* LeadFollowUp
* Campaign
* CampaignRecipient

Django Models and Django ORM will be the primary database access approach.

Raw SQL should only be used when there is a clear technical reason.

---

# 8. Project Data Strategy

The six initial ventures are data records, not separate code modules.

Example concept:

Project 1
Project 2
Project 3
...
Project 6

A future Project 7 should normally be added through the admin interface without modifying application code.

---

# 9. Property Type Strategy

Projects should have a property type.

Initial type:

`OPEN_PLOT`

Future types may include:

* `VILLA`
* `APARTMENT`
* `COMMERCIAL`
* `OTHER`

This allows the system to grow without redesigning the project structure.

---

# 10. Admin Strategy

Phase 1:

Use Django Admin.

Admin should support routine business operations without developer intervention.

A custom dashboard may be developed later if Django Admin becomes insufficient for daily operations.

---

# 11. Lead Management Strategy

The lead system should support:

* Lead capture
* Lead source tracking
* Project interest
* Plot interest
* Status management
* Sales-agent assignment
* Follow-ups
* Site visits
* Booking requests
* Campaign eligibility

Future CRM integration may be added if required.

---

# 12. WhatsApp Strategy

WhatsApp is the primary customer communication channel.

### Phase 1

Use WhatsApp Business and click-to-chat.

Support:

* General enquiry
* Project enquiry
* Plot enquiry
* Site visit
* Booking enquiry
* Register interest

### Future

Evaluate:

* WhatsApp Business Platform/API
* CRM integration
* Automated campaigns
* Scheduled follow-ups
* Multiple sales agents

Automation must comply with WhatsApp policies and customer consent requirements.

---

# 13. Campaign Strategy

Future campaign manager:

1. Select audience
2. Select template
3. Preview
4. Schedule or send
5. Track result

Possible audience criteria:

* Interested project
* Lead status
* WhatsApp opt-in
* Campaign eligibility
* Sales agent
* Follow-up state

Automated/bulk WhatsApp communication requires an appropriate official API/provider.

---

# 14. Analytics Strategy

Initial analytics:

* Visitors
* Page views
* Project views
* Brochure downloads
* WhatsApp clicks
* Call clicks
* Enquiries
* Site visits
* Booking requests

Primary funnel:

Visitors → Project Views → Leads → Interested → Site Visits → Booking Requests

Future Data Science capabilities may include:

* Lead scoring
* Conversion analysis
* Lead-source analysis
* Follow-up prioritization
* Campaign performance
* Sales forecasting

AI/ML should only be introduced when sufficient clean data and a real business use case exist.

---

# 15. Responsive Strategy

Use one responsive website.

The same application should adapt to:

* Phones
* Tablets
* Laptops
* Desktops
* Large screens

No separate mobile/tablet/desktop websites.

Bootstrap can be used as the initial responsive UI framework.

---

# 16. SEO Strategy

Each project should have:

* SEO title
* Meta description
* Slug
* Proper headings
* Image alt text
* Internal links

Technical SEO should include:

* Sitemap
* robots.txt
* Structured data where appropriate
* Search Console
* Mobile-friendly design
* Performance optimization

---

# 17. Performance Strategy

Priorities:

* Optimize images
* Lazy-load appropriate media
* Minimize unnecessary JavaScript
* Optimize database queries
* Avoid N+1 ORM queries
* Use `select_related()` where appropriate
* Use `prefetch_related()` where appropriate
* Add indexes where useful
* Introduce caching when justified

Do not introduce advanced optimization before measuring a real need.

---

# 18. Media Strategy

### Development

Media can initially use local/static storage.

### Production

Depending on scale, media may later move to:

* Cloud object storage
* CDN
* Image optimization service

Project videos should preferably be hosted on YouTube and embedded rather than unnecessarily storing large video files on the application server.

---

# 19. Deployment Strategy

Development:

Local machine

Version control:

Git + GitHub

Testing:

Staging environment

Production:

Cloud hosting + hosted MySQL

Production requirements:

* HTTPS
* `DEBUG=False`
* Secure environment variables
* Database backups
* Monitoring
* Error logging
* Static/media configuration

---

# 20. Domain Strategy

Current domain:

`ajdevelopers.in`

Future domain possibility:

`ajdevelopers.com`

Domain configuration should be centralized so migration can be performed without rewriting hard-coded URLs throughout the project.

---

# 21. Testing Strategy

Testing should include:

* Unit tests for critical logic
* Model tests
* Form tests
* View tests
* Authentication tests
* Permission tests
* Lead-flow tests
* Site-visit tests
* Booking tests
* Admin tests
* Responsive tests
* Browser tests
* Security tests
* Performance tests
* SEO checks
* Broken-link checks
* Backup/restore tests
* Production smoke tests

Client/UAT testing should be performed before production launch.

---

# 22. GitHub Strategy

Use GitHub from the beginning.

Recommended practices:

* Meaningful commits
* `.gitignore`
* Environment configuration
* README
* Documentation
* Issue tracking
* Feature branches when useful
* Pull requests when appropriate

Never commit:

* Secrets
* API keys
* Passwords
* Production credentials
* Private customer data
* Sensitive business information

---

# 23. Environment Strategy

Maintain separate configurations for:

* Development
* Staging
* Production

Production should use:

`DEBUG=False`

Secrets should be stored outside source control.

---

# 24. Backup Strategy

Production backups should include:

* Database
* Important media
* Required configuration information

Backups must also be periodically tested by performing a restore procedure.

---

# 25. Cost Strategy

Development should initially aim for:

**₹0 / minimal cost**

Use:

* Local development
* GitHub
* Free/low-cost development tools
* Existing domain
* Free or low-cost services where practical

Production costs will depend on:

* Hosting
* Database
* Storage
* Email
* WhatsApp/API usage
* Automation services
* Traffic

Do not purchase infrastructure before it is needed.

---

# 26. Scalability Strategy

Initial system:

Simple single-application architecture.

Future growth may introduce:

* Better hosting
* Managed database
* Cloud storage
* CDN
* Caching
* Background workers
* API integrations
* CRM
* Multiple sales agents

Only introduce these components when business requirements justify them.

---

# 27. Documentation Strategy

Documentation should remain useful and current.

Do not create unnecessary files.

Rule:

> Need → Create → Use → Maintain

Potential future documentation files may include:

* `design.md`
* `database.md`
* `testing.md`
* `deployment.md`
* `security.md`
* `api.md`
* `user-guide.md`

These should be created only when the relevant phase requires them.

---

# 28. Current Planning Status

Requirement Analysis: **Completed**

Planning: **Completed**

Design: **Next**

Implementation: **Pending**

Testing: **Pending**

Deployment: **Pending**

Maintenance: **Pending**
