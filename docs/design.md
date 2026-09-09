# AJ Developers — Design Specification

## 1. Design Overview

AJ Developers website will use a clean, modern and trustworthy real-estate design.

The primary goal is to present projects professionally and convert visitors into:

- Enquiries
- WhatsApp conversations
- Phone calls
- Site visits
- Booking requests

The website will be mobile-first and fully responsive across phones, tablets, laptops and desktops.

---

## 2. Design Principles

The website design should follow these principles:

1. Trust first
2. Simple navigation
3. Strong project visuals
4. Clear calls-to-action
5. Mobile-first experience
6. Fast loading
7. Easy-to-read content
8. Minimal unnecessary animations
9. Consistent branding
10. Easy future maintenance

The website should feel like a real business website, not a generic template or demo project.

---

## 3. Brand

### Company

AJ Developers

### Tagline

Developing Spaces, Enriching Lives.

### Domain

ajdevelopers.in

### Logo

The provided AJ Developers logo will be used as the official website logo.

### Brand Direction

The visual language should communicate:

- Trust
- Premium quality
- Professionalism
- Real estate
- Growth
- Long-term value

---

# 4. Sitemap

## Main Navigation

- Home
- Projects
- About Us
- Contact

Primary CTA:

- WhatsApp

## Main Pages

- `/`
- `/projects/`
- `/projects/<project-slug>/`
- `/about/`
- `/contact/`
- `/site-visit/`
- `/callback/`
- `/register-interest/`
- `/booking-request/`
- `/thank-you/`

## Legal Pages

- `/privacy-policy/`
- `/terms-and-conditions/`
- `/disclaimer/`
- `/legal/`

---

# 5. Header Design

## Desktop

Header contains:

- AJ Developers logo
- Home
- Projects
- About Us
- Contact
- WhatsApp CTA

The header should remain clean and uncluttered.

## Mobile

Mobile header contains:

- Logo
- Menu button
- WhatsApp shortcut where appropriate

Navigation opens through a mobile menu.

---

# 6. Homepage Layout

The homepage will contain the following sections in order.

## 6.1 Hero Section

Purpose:

Immediately communicate what AJ Developers offers.

Content:

- Premium open plots positioning
- Strong headline
- Short supporting statement
- Key trust/value points
- Primary CTA
- Secondary CTA
- High-quality project/location visual

Primary CTA:

`Explore Projects`

Secondary CTA:

`Book a Site Visit`

Possible supporting points:

- Prime Locations
- Planned Communities
- Trusted Development

Only use claims that are factually supported.

---

## 6.2 Featured Ventures

Purpose:

Show the current six ventures prominently.

Content:

- Section heading
- Short introduction
- Six project cards
- View Project CTA
- View All Projects CTA

Each project card may contain:

- Project image
- Project name
- Location
- Property type
- Short highlight
- View Project button

Projects are stored as database records.

The design must support more than six projects in the future.

---

## 6.3 Why AJ Developers

Purpose:

Build trust and communicate company strengths.

Possible points:

- Prime Locations
- Quality Planning
- Clear Documentation
- Customer Focus
- Transparent Process
- Dedicated Support

Only publish claims that AJ Developers can substantiate.

---

## 6.4 Location & Connectivity

Purpose:

Communicate the importance of project locations.

Content:

- Location introduction
- Connectivity highlights
- Major roads/highways
- Schools
- Hospitals
- Workplaces
- Airports
- Google Maps CTA

Project-specific location information should be displayed on project pages.

---

## 6.5 Project Highlights

Purpose:

Show common project benefits without making unsupported claims.

Possible items:

- Wide Roads
- Green Spaces
- Water Supply
- Electricity
- Security
- Landscaping
- Other project-specific amenities

Amenities should come from project data rather than hard-coded content.

---

## 6.6 Site Visit CTA

Purpose:

Convert interested visitors into site visit requests.

Content:

- Short heading
- Supporting text
- `Book a Site Visit` button

The CTA should be visually prominent.

---

## 6.7 About AJ Developers

Purpose:

Introduce the company.

Content:

- Company image/project image
- Short company description
- Brand philosophy
- `Learn More About Us` CTA

Longer information will be available on the About page.

---

## 6.8 Contact Section

Purpose:

Provide multiple ways to contact AJ Developers.

Contact methods:

- Phone
- WhatsApp
- Email
- General location
- Enquiry form

The public website should use a genuine business/contact location.

The user's personal home address must not be presented as a corporate office address.

---

## 6.9 Footer

Footer contains:

- AJ Developers logo
- Tagline
- Navigation links
- Contact information
- Social media links
- WhatsApp
- Privacy Policy
- Terms & Conditions
- Disclaimer
- Copyright

Social platforms:

- Facebook
- Instagram
- YouTube
- WhatsApp

LinkedIn may be added later.

---

# 7. Projects Listing Page

URL:

`/projects/`

Purpose:

Display all published ventures.

Each project card should show:

- Project image
- Project name
- Location
- Property type
- Short description
- Key highlights
- View Project CTA

Possible future filtering:

- Property Type
- Location

Filtering should only be implemented when it provides real value.

---

# 8. Individual Project Page

URL:

`/projects/<project-slug>/`

Page structure:

1. Hero
2. Project Overview
3. Key Highlights
4. Amenities
5. Location & Connectivity
6. Layout
7. Approvals / Legal Information
8. Gallery
9. Videos
10. Brochure
11. Enquiry CTA
12. Site Visit CTA
13. Booking Request CTA
14. Contact / WhatsApp CTA

---

# 9. Project Hero

Project hero contains:

- Project name
- Location
- Property type
- Short description
- Main project image
- `Enquire Now`
- `WhatsApp`
- `Book a Site Visit`

Public project pricing will not be displayed.

Public plot availability will not be displayed.

---

# 10. Project Layout

Projects may include:

- Layout image
- Layout PDF
- Roads
- Plot numbers
- Amenities
- Blocks
- Important landmarks

Future enhancement:

Clickable interactive plot layout.

A visitor may select a plot and choose:

`Ask About This Plot`

The enquiry should capture:

- Project
- Plot number
- Customer details
- Message

There will be no public Available / Reserved / Sold status in Phase 1.

---

# 11. Forms UX

Forms should be:

- Short
- Simple
- Mobile-friendly
- Clearly labelled
- Easy to complete

## Enquiry Form

Fields:

- Name
- Mobile Number
- Email (optional)
- Interested Project
- Plot Number (optional)
- Message
- WhatsApp communication consent where applicable

---

## Site Visit Form

Fields:

- Name
- Mobile Number
- Preferred Date
- Preferred Time
- Interested Project
- Optional Message

---

## Booking Request

Flow:

Select Project → Select Plot → Submit Details → Booking Request → AJ Developers Contact → Confirmation & Documentation

A booking request is not an automatic final booking confirmation.

No online payment will be implemented in Phase 1.

---

# 12. CTA Strategy

Primary CTAs:

- Explore Projects
- Enquire Now
- Call Now
- WhatsApp
- Book a Site Visit
- Request a Callback
- Register Interest
- Ask About This Plot
- Book This Plot
- Download Brochure

Avoid:

- Check Available Plots
- View Current Availability
- EMI Calculator
- Loan Calculator

because public availability and finance tools are not part of Phase 1.

---

# 13. Mobile UX

The website must work on:

- Small phones
- Large phones
- Tablets
- Laptops
- Desktops
- Large screens

Mobile experience should include a fixed bottom CTA bar:

`Call | WhatsApp | Site Visit`

Requirements:

- Touch-friendly buttons
- Large enough tap targets
- Simple forms
- Responsive images
- No horizontal scrolling
- Fast loading
- Easy navigation

---

# 14. Design System

## Colors

The exact final palette will be derived from the AJ Developers logo.

Design should use:

- Primary brand color
- Secondary brand/accent color
- Neutral background
- Dark text
- Muted text
- Success/action colors where required

Colors should remain consistent across the website.

---

## Typography

Use a modern, highly readable font system.

Typography hierarchy:

- H1 — Hero headline
- H2 — Major sections
- H3 — Cards/subsections
- Body — Main content
- Small text — Supporting information

Typography must remain readable on mobile devices.

---

# 15. Components

Reusable UI components should include:

### Navigation

- Header
- Mobile menu
- Footer

### Content

- Hero
- Section heading
- Project card
- Amenity card
- Highlight card
- Image gallery
- Video embed
- Approval card

### Actions

- Primary button
- Secondary button
- WhatsApp button
- Call button
- Site Visit CTA
- Download button

### Forms

- Input
- Select
- Textarea
- Checkbox
- Form validation
- Success message
- Error message

### Project

- Project hero
- Project overview
- Project gallery
- Layout viewer
- Location section
- Approval section
- Project CTA

---

# 16. Accessibility

The website should provide basic accessibility.

Requirements:

- Proper heading hierarchy
- Labels for form fields
- Alternative text for images
- Keyboard navigation
- Sufficient text/background contrast
- Visible focus states
- Do not rely only on color to communicate status
- Accessible buttons and links

---

# 17. SEO Design Considerations

Each project page should support:

- SEO title
- Meta description
- Clean URL
- Proper headings
- Image alt text
- Internal links
- Breadcrumbs where useful

Example:

`ajdevelopers.in/projects/project-name/`

The design should allow SEO content without making pages look keyword-stuffed.

---

# 18. Performance Design

Design decisions should support performance.

Requirements:

- Optimized images
- Responsive images
- Lazy loading
- Minimal unnecessary JavaScript
- Efficient YouTube embeds
- Avoid excessive animations
- Avoid huge background assets
- Keep forms lightweight

---

# 19. Placeholder Content Strategy

During development:

- Use dummy project names
- Use placeholder project images
- Use sample descriptions
- Use sample amenities
- Use sample approval data

Real project content and assets can be added later through the admin panel.

The website should not require all real images/content before development can begin.

---

# 20. Design Philosophy

AJ Developers should look like a professional real-estate company while remaining practical to maintain.

The design should prioritize:

`Trust → Projects → Enquiry → WhatsApp/Call → Site Visit → Booking`

The website should not be overloaded with:

- Unnecessary animations
- Excessive popups
- Fake reviews
- Fake statistics
- Unsupported investment claims
- Public pricing
- Public availability
- Unnecessary calculators

---

# 21. Design Status

Step 3 — Design:

- Homepage wireframe: Approved
- Overall page structure: Approved
- Responsive approach: Approved
- Mobile CTA strategy: Approved
- Project page structure: Approved
- Form strategy: Approved
- CTA strategy: Approved
- No public pricing: Locked
- No public availability: Locked
- No EMI/loan calculator: Locked
- Component-based UI: Locked