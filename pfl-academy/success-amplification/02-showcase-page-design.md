# Student Showcase Page Design
## Structure & Wireframe Specification

### Purpose
Define the layout and content structure for individual student portfolio pages and the public showcase gallery.

---

## Individual Student Portfolio Page

### URL Structure
```
pflacademy.com/showcase/[student-slug]
Example: pflacademy.com/showcase/bright-bites-bakery
```

### Page Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  [PFL Academy Logo]              [Back to Showcase] [Share ▼]  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐                                               │
│  │              │   BRIGHT BITES BAKERY                         │
│  │   Business   │   "Healthy cookies that taste like a treat"  │
│  │    Logo/     │                                               │
│  │   Image      │   Created by: Jordan M. | Grade 11            │
│  │              │   Instructor: Ms. Dianna Martinez             │
│  └──────────────┘   School: Lincoln High School, CA             │
│                     Completed: January 2025                     │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  THE PROBLEM                                                    │
│  ─────────────                                                  │
│  "Students at my school want snacks but the vending machines    │
│  only have junk food. Parents complain, kids are hungry, and    │
│  the school doesn't have healthy options."                      │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  THE SOLUTION                                                   │
│  ────────────                                                   │
│  Bright Bites Bakery makes cookies using natural sweeteners     │
│  and whole ingredients. We sell them at school events and       │
│  through pre-orders. Each cookie has nutrition info so          │
│  parents know exactly what their kids are eating.               │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  BY THE NUMBERS                                                 │
│  ──────────────                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │  $12,400    │  │   $2,800    │  │    67%      │              │
│  │  Projected  │  │   Startup   │  │   Profit    │              │
│  │  Revenue    │  │   Costs     │  │   Margin    │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│                                                                 │
│  Target Market: High school students and parents                │
│  Revenue Model: Direct sales at events + weekly pre-orders      │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  INSTRUCTOR NOTES                               [Optional]      │
│  ─────────────────                                              │
│  "Jordan showed exceptional understanding of market research.   │
│  She surveyed 150 students before finalizing her product line.  │
│  This is college-application-ready work."                       │
│                        — Ms. Dianna Martinez                    │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ATTACHMENTS                                    [Optional]      │
│  ───────────                                                    │
│  📄 Full Business Plan (PDF)                                    │
│  📊 Pitch Deck (12 slides)                                      │
│  📈 Financial Projections Spreadsheet                           │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  🎓 This business plan was created through PFL Academy  │   │
│  │     Learn more about bringing PFL Academy to your       │   │
│  │     school → [Get Started]                              │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  [← Previous Student]                    [Next Student →]       │
└─────────────────────────────────────────────────────────────────┘
```

### Content Fields

| Section | Field | Required | Max Length |
|---------|-------|----------|------------|
| Header | Business Name | Yes | 60 chars |
| Header | Tagline | Yes | 100 chars |
| Header | Student Name (display) | Yes | 50 chars |
| Header | Grade Level | Yes | — |
| Header | Instructor Name | Yes | 50 chars |
| Header | School Name | Yes | 100 chars |
| Header | Completion Date | Yes | — |
| Header | Business Logo/Image | No | 500x500px |
| Problem | Problem Statement | Yes | 500 chars |
| Solution | Solution Description | Yes | 750 chars |
| Numbers | Projected Revenue | Yes | Currency |
| Numbers | Startup Costs | No | Currency |
| Numbers | Profit Margin | No | Percentage |
| Numbers | Target Market | Yes | 200 chars |
| Numbers | Revenue Model | Yes | 200 chars |
| Instructor | Instructor Notes | No | 500 chars |
| Attachments | Business Plan PDF | No | 10MB |
| Attachments | Pitch Deck | No | 25MB |
| Attachments | Other files | No | 10MB each |

---

## Public Showcase Gallery

### URL
```
pflacademy.com/showcase
```

### Gallery Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  [PFL Academy Logo]                              [Sign In]      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│           STUDENT SHOWCASE                                      │
│    See what PFL Academy students are building                   │
│                                                                 │
│    "X business plans created | $Y million in projected revenue" │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  FILTER BY:                                                     │
│  [All Grades ▼] [All States ▼] [All Categories ▼] [Search 🔍]  │
│                                                                 │
│  SORT BY: [Most Recent ▼]                                       │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │  [Image]        │  │  [Image]        │  │  [Image]        │ │
│  │                 │  │                 │  │                 │ │
│  │  Bright Bites   │  │  Pet Pal App    │  │  Green Clean    │ │
│  │  Bakery         │  │                 │  │  Co.            │ │
│  │                 │  │                 │  │                 │ │
│  │  Jordan M.      │  │  Alex T.        │  │  Sam K.         │ │
│  │  Grade 11 | CA  │  │  Grade 10 | TX  │  │  Grade 12 | NY  │ │
│  │                 │  │                 │  │                 │ │
│  │  $12,400        │  │  $45,000        │  │  $8,200         │ │
│  │  projected      │  │  projected      │  │  projected      │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │  [Image]        │  │  [Image]        │  │  [Image]        │ │
│  │  ...            │  │  ...            │  │  ...            │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
│                                                                 │
│                    [Load More]                                  │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Want to see YOUR students here?                        │   │
│  │  Bring PFL Academy to your school → [Learn More]        │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Card Component

| Element | Content |
|---------|---------|
| Image | Business logo or placeholder |
| Title | Business Name |
| Subtitle | Student Name (display) |
| Meta | Grade Level | State |
| Highlight | Projected Revenue |

### Filter Options

| Filter | Options |
|--------|---------|
| Grade Level | All, 9th, 10th, 11th, 12th |
| State | All, [List of states with students] |
| Category | All, Food & Beverage, Technology, Services, Retail, etc. |
| Sort | Most Recent, Highest Revenue, Alphabetical |

---

## Featured Section (Homepage or Showcase)

### "Featured This Month" Component

```
┌─────────────────────────────────────────────────────────────────┐
│  ⭐ FEATURED THIS MONTH                                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                                                           │ │
│  │  [Large Image]              BRIGHT BITES BAKERY           │ │
│  │                             ────────────────────          │ │
│  │                             "Healthy cookies that         │ │
│  │                             taste like a treat"           │ │
│  │                                                           │ │
│  │                             Jordan M. | Grade 11          │ │
│  │                             Lincoln High School, CA       │ │
│  │                             Ms. Dianna Martinez's Class   │ │
│  │                                                           │ │
│  │                             Projected Revenue: $12,400    │ │
│  │                                                           │ │
│  │                             [View Full Plan →]            │ │
│  │                                                           │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Share Functionality

### Share Dropdown Options
- Copy Link
- Share to LinkedIn
- Share to Twitter/X
- Share to Facebook
- Download as PDF
- Email This

### Social Share Preview (OG Tags)
```
Title: Bright Bites Bakery | PFL Academy Student Showcase
Description: A student business plan by Jordan M. (Grade 11) - Healthy cookies for schools. $12,400 projected revenue.
Image: Business logo or auto-generated card
```

---

## Mobile Responsiveness

### Portfolio Page (Mobile)
- Stack all sections vertically
- Full-width images
- Collapsible sections for Problem/Solution
- Sticky share button at bottom

### Gallery (Mobile)
- Single column card layout
- Filters collapse into dropdown
- Infinite scroll instead of pagination

---

## Technical Notes for Seb

### Components Needed
1. `StudentPortfolioPage` — Individual showcase page
2. `ShowcaseGallery` — Grid of cards with filtering
3. `StudentCard` — Reusable card component
4. `ShareDropdown` — Social/copy/download sharing
5. `FeaturedSpotlight` — Large featured student component

### API Endpoints Needed
```
GET /api/showcase — List public student portfolios (paginated, filterable)
GET /api/showcase/[slug] — Single portfolio details
GET /api/showcase/featured — Current featured students
POST /api/showcase/[id]/share — Track share events (optional analytics)
```

### SEO Considerations
- Each portfolio page should have unique meta tags
- Structured data (Schema.org) for educational content
- Sitemap inclusion for public portfolios

---

## Content Examples (For Mockups)

### Example 1: Food Business
- **Name:** Bright Bites Bakery
- **Tagline:** Healthy cookies that taste like a treat
- **Revenue:** $12,400
- **Category:** Food & Beverage

### Example 2: Tech/App
- **Name:** Pet Pal App
- **Tagline:** Never forget to feed your pet again
- **Revenue:** $45,000
- **Category:** Technology

### Example 3: Service Business
- **Name:** Green Clean Co.
- **Tagline:** Eco-friendly lawn care for busy families
- **Revenue:** $8,200
- **Category:** Services

### Example 4: Retail
- **Name:** Threads by Tay
- **Tagline:** Upcycled vintage clothing with a modern twist
- **Revenue:** $15,800
- **Category:** Retail/Fashion
