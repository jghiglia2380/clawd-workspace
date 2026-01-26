# Instructor Profile & Spotlight Format
## Design Specification for Educator Features

### Purpose
Define the structure for instructor profile pages and spotlight features that help educators showcase their work and gain recognition.

---

## Instructor Profile Page

### URL Structure
```
pflacademy.com/educators/[instructor-slug]
Example: pflacademy.com/educators/dianna-martinez
```

### Page Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  [PFL Academy Logo]              [Back to Educators] [Share ▼] │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐                                               │
│  │              │   DIANNA MARTINEZ                             │
│  │   Profile    │   Business & Entrepreneurship Teacher         │
│  │    Photo     │                                               │
│  │              │   Lincoln High School                         │
│  │              │   Sacramento, California                      │
│  └──────────────┘                                               │
│                     🏆 PFL Academy Educator since 2023          │
│                     ⭐ Featured Instructor — January 2025       │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ABOUT                                                          │
│  ─────                                                          │
│  "I believe every student can be an entrepreneur. My job is     │
│  to give them the tools and confidence to try."                 │
│                                                                 │
│  Dianna has been teaching business courses for 8 years,         │
│  specializing in helping students develop real-world            │
│  financial literacy and entrepreneurship skills.                │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  IMPACT BY THE NUMBERS                                          │
│  ─────────────────────                                          │
│                                                                 │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐               │
│  │   127   │ │   89    │ │  $847K  │ │   94%   │               │
│  │Students │ │Business │ │Projected│ │Complete │               │
│  │ Taught  │ │ Plans   │ │ Revenue │ │  Rate   │               │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘               │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  TEACHING APPROACH                              [Optional]      │
│  ─────────────────                                              │
│  • Uses weekly pitch sessions for peer feedback                 │
│  • Integrates financial literacy with real business planning    │
│  • Invites local entrepreneurs as guest speakers                │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  FEATURED STUDENT WORK                                          │
│  ─────────────────────                                          │
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │  Bright Bites   │  │  Pet Pal App    │  │  Green Clean    │ │
│  │  Bakery         │  │                 │  │  Co.            │ │
│  │  Jordan M.      │  │  Alex T.        │  │  Sam K.         │ │
│  │  $12,400        │  │  $45,000        │  │  $8,200         │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
│                                                                 │
│                    [View All Student Work →]                    │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  BADGES & RECOGNITION                                           │
│  ────────────────────                                           │
│                                                                 │
│  🎯 First 50 Students    🏅 High Completion Rate                │
│  ⭐ Featured Instructor  📊 Top 10% Assessment Scores           │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Want to join educators like Dianna?                    │   │
│  │  Bring PFL Academy to your school → [Get Started]       │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Profile Content Fields

### Required Fields
| Field | Description | Max Length |
|-------|-------------|------------|
| Full Name | Instructor's name | 50 chars |
| Title/Role | Job title | 100 chars |
| School Name | Where they teach | 100 chars |
| Location | City, State | 50 chars |
| Member Since | When they joined PFL Academy | Date |

### Optional Fields
| Field | Description | Max Length |
|-------|-------------|------------|
| Profile Photo | Professional headshot | 500x500px |
| Bio Quote | Personal statement | 200 chars |
| About Paragraph | Extended bio | 500 chars |
| Teaching Approach | Bullet points on methods | 3-5 bullets |
| Subjects Taught | List of courses | List |
| Years Teaching | Experience level | Number |
| Website/LinkedIn | External links | URLs |

### Auto-Calculated Metrics
| Metric | Description |
|--------|-------------|
| Total Students | Sum of all enrolled students |
| Business Plans Created | Count of student submissions |
| Total Projected Revenue | Sum of all student projections |
| Completion Rate | % of students completing curriculum |
| Average Assessment Score | Mean across all students |
| Semesters Active | How long using platform |

---

## Instructor Spotlight Feature

### "Meet Our Educators" Gallery

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│           MEET OUR EDUCATORS                                    │
│    The teachers bringing entrepreneurship to life               │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  [Filter: All States ▼] [Sort: Featured First ▼]               │
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │  [Photo]        │  │  [Photo]        │  │  [Photo]        │ │
│  │                 │  │                 │  │                 │ │
│  │  Dianna M.      │  │  Robert K.      │  │  Sarah L.       │ │
│  │  Sacramento, CA │  │  Austin, TX     │  │  Chicago, IL    │ │
│  │                 │  │                 │  │                 │ │
│  │  127 students   │  │  89 students    │  │  156 students   │ │
│  │  ⭐ Featured    │  │                 │  │  🏆 Top 10%     │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Spotlight Card Component
| Element | Content |
|---------|---------|
| Photo | Profile image (200x200) |
| Name | First name + Last initial |
| Location | City, State |
| Key Metric | Total students taught |
| Badge | Featured, Top 10%, etc. (if applicable) |

---

## Monthly Spotlight Email/Feature

### Format for "Instructor of the Month"

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   ⭐ INSTRUCTOR SPOTLIGHT — JANUARY 2025 ⭐

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   DIANNA MARTINEZ
   Lincoln High School | Sacramento, CA

   "My students don't just learn about business—
   they build businesses."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   BY THE NUMBERS

   127 students taught
   89 business plans created
   $847,000 in projected student revenue
   94% completion rate

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   WHAT MAKES DIANNA SPECIAL

   Dianna transforms her classroom into a startup
   incubator. Her students pitch weekly, get peer
   feedback, and leave with portfolio-ready work.

   One of her students actually launched their
   business at a local farmers market.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   DIANNA'S ADVICE

   "Start with the simulation games. They hook
   students immediately. By the time you get to
   business plans, they're invested."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   → Read Dianna's full story
   → See her students' work

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Badges & Recognition System

### Achievement Badges
| Badge | Criteria | Icon |
|-------|----------|------|
| Early Adopter | Joined in first year | 🌟 |
| First 10 Students | 10 students completed | 🎯 |
| First 50 Students | 50 students completed | 🎯 |
| Century Club | 100+ students | 💯 |
| High Completion | >90% completion rate | 🏅 |
| Top Assessments | Top 10% avg scores | 📊 |
| Million Dollar Class | $1M+ in student projections | 💰 |
| Referral Champion | 3+ colleague referrals | 🤝 |
| Multi-Year Veteran | 2+ years active | 🏆 |
| Featured Instructor | Selected for spotlight | ⭐ |

### Badge Display Rules
- Show top 4 badges on profile
- Full badge collection on dedicated page
- New badges trigger notification/celebration

---

## Shareable Assets for Instructors

### What Instructors Can Download/Share

1. **Profile Card**
   - Social media-sized image with stats
   - "I'm a PFL Academy Educator" badge

2. **Impact Summary**
   - One-pager with their metrics (see Impact Report)

3. **Certificate**
   - "PFL Academy Certified Educator" certificate
   - Milestone certificates (100 students, etc.)

4. **Social Share Templates**
   - Pre-written posts with their stats
   - Images formatted for LinkedIn, Twitter

---

## Instructor Dashboard View

### "My Impact" Section

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  MY IMPACT                                    [Share Profile →] │
│                                                                 │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐               │
│  │   127   │ │   89    │ │  $847K  │ │   94%   │               │
│  │Students │ │Business │ │Projected│ │Complete │               │
│  │ Taught  │ │ Plans   │ │ Revenue │ │  Rate   │               │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘               │
│                                                                 │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  RECENT ACHIEVEMENTS                                            │
│  🏅 New Badge: High Completion Rate                            │
│  ⭐ You've been selected for January Spotlight!                │
│                                                                 │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  [Download Impact Report]  [View Public Profile]  [Edit Bio]   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Opt-In Flow

### Profile Visibility Settings

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  PROFILE VISIBILITY                                             │
│                                                                 │
│  ○ Private — Only I can see my profile                         │
│  ○ PFL Community — Other PFL educators can see                 │
│  ● Public — Anyone can view my profile                         │
│                                                                 │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  SPOTLIGHT OPT-IN                                               │
│                                                                 │
│  ☑ I'm open to being featured in PFL Academy spotlights        │
│  ☑ You can contact me about success story interviews           │
│  ☑ Include my profile in the educator directory                │
│                                                                 │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  DISPLAY PREFERENCES                                            │
│                                                                 │
│  ☑ Show my full name (vs. First name + Last initial)           │
│  ☑ Show my school name                                          │
│  ☐ Show my photo                                                │
│                                                                 │
│                                              [Save Preferences] │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Technical Notes for Seb

### New Database Fields (Instructor Model)
```
bio_quote: string (200 char)
about: text (500 char)
teaching_approach: array of strings
profile_photo_url: string
linkedin_url: string
website_url: string
profile_visibility: enum (private, community, public)
spotlight_opt_in: boolean
story_interview_opt_in: boolean
directory_opt_in: boolean
show_full_name: boolean
show_school: boolean
show_photo: boolean
```

### API Endpoints
```
GET /api/educators — List public educator profiles
GET /api/educators/[slug] — Single educator profile
GET /api/educators/[id]/impact — Educator's metrics
GET /api/educators/featured — Current featured educators
PATCH /api/educators/[id]/settings — Update visibility preferences
```

### Components
1. `InstructorProfilePage` — Full profile view
2. `InstructorCard` — Gallery card component
3. `ImpactStats` — Reusable stats display
4. `BadgeCollection` — Badge display component
5. `SpotlightFeature` — Featured educator component
6. `ProfileSettings` — Visibility/opt-in management
