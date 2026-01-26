# PFL Academy Success Amplification System
## Data Requirements Specification

### Purpose
Define what data we need to collect, track, and display to power the Success Amplification system — enabling instructors to showcase their impact and students to build portfolios.

---

## Instructor-Level Data

### Profile Information
| Field | Source | Required |
|-------|--------|----------|
| Full Name | Registration | Yes |
| School Name | Registration | Yes |
| School District | Registration | Yes |
| State | Registration | Yes |
| Grade Level(s) Taught | Registration | Yes |
| Subject Area | Registration | Yes |
| Profile Photo | Upload (optional) | No |
| Bio/Statement | Input (optional) | No |
| Years Using PFL Academy | Calculated | Auto |

### Aggregate Metrics (Auto-calculated)
| Metric | Description | Display |
|--------|-------------|---------|
| Total Students | # of students enrolled across all classes | Number |
| Active Students | # currently engaged (logged in within 30 days) | Number |
| Chapters Completed | Total chapters completed by all students | Number |
| Average Completion Rate | % of enrolled students completing curriculum | Percentage |
| Average Assessment Score | Mean score across all student assessments | Percentage |
| Business Plans Created | # of student business plans submitted | Number |
| Total Projected Revenue | Sum of all student business plan revenue projections | Currency |
| Time on Platform | Aggregate student engagement hours | Hours |

### Recognition Data
| Field | Description |
|-------|-------------|
| Badges Earned | Milestones hit (First 10 completions, 100 students, etc.) |
| Spotlight Features | Dates/links if featured in newsletters or showcases |
| Referrals Made | # of colleagues who signed up via their link |
| Tenure | How long they've been active |

---

## Student-Level Data

### Profile Information
| Field | Source | Privacy |
|-------|--------|---------|
| Display Name | Input (can be pseudonym) | Public (optional) |
| Grade Level | Registration | Public |
| School | Via instructor | Public (optional) |
| Instructor | Via enrollment | Public |

### Progress Metrics
| Metric | Description |
|--------|-------------|
| Chapters Completed | List of completed chapters with dates |
| Assessment Scores | Score per chapter assessment |
| Overall Progress | % through curriculum |
| Time Spent | Total engagement hours |
| Completion Date | When they finished the full curriculum |

### Business Plan Data (Portfolio Core)
| Field | Description | Public |
|-------|-------------|--------|
| Business Name | Student's venture name | Yes |
| Business Type | Category (product, service, etc.) | Yes |
| Problem Statement | What problem they're solving | Yes |
| Solution Summary | Their approach | Yes |
| Target Market | Who they're serving | Yes |
| Revenue Model | How they'll make money | Yes |
| Projected Revenue | Financial projection | Yes |
| Startup Costs | Initial investment needed | Optional |
| Pitch Deck | Uploaded slides | Optional |
| Business Plan PDF | Full document | Optional |
| Instructor Feedback | Teacher comments/endorsement | Optional |

### Recognition Data
| Field | Description |
|-------|-------------|
| Featured Status | If selected for showcase |
| Awards/Badges | Competition wins, achievements |
| Endorsements | Instructor or peer endorsements |

---

## School/District-Level Data (Aggregated)

### Metrics
| Metric | Description |
|--------|-------------|
| Total Instructors | # of teachers using PFL Academy |
| Total Students | # of students enrolled |
| Completion Rate | School-wide average |
| Assessment Performance | School-wide average score |
| Business Plans Created | Total across all classes |
| Total Projected Revenue | Sum of all student projections |

### For Success Stories
| Field | Source |
|-------|--------|
| School Name | Registration |
| District | Registration |
| Location (City, State) | Registration |
| School Type | Public, Private, Charter, etc. |
| Demographics (optional) | Title I status, urbanicity, etc. |

---

## Data Collection Points

### Automatic (System Tracks)
- Login frequency and duration
- Chapter completion timestamps
- Assessment submissions and scores
- Business plan submissions
- Progress through curriculum

### Instructor Input
- Student roster (names or pseudonyms)
- Final business plan approval/feedback
- Success story quotes or testimonials
- Permission for student work to be featured

### Student Input
- Business plan details
- Opt-in for public showcase
- Profile customization

### Admin Input (PFL Academy Team)
- Feature selections for spotlights
- Badge/award assignments
- Success story curation

---

## Privacy & Permissions

### Default State
- Student work is PRIVATE unless explicitly opted-in
- Instructor profiles are PRIVATE unless opted-in
- Aggregate school data can be used internally

### Opt-In Levels
1. **Private** — Only visible to student and instructor
2. **School** — Visible within school community
3. **Public** — Featured in showcase, shareable externally

### Required Consents
- Instructor consent for spotlight features
- Student/parent consent for public showcase (if under 18)
- School consent for school-level success stories

---

## Technical Notes for Seb

### Data Already Available (Likely)
- User registration data
- Chapter completion tracking
- Assessment scores
- Time on platform

### Data Needing New Collection
- Business plan structured fields (may need form redesign)
- Opt-in permissions system
- Instructor profile enhancements
- Referral tracking

### Calculations Needed
- Aggregation queries for instructor/school dashboards
- "Projected revenue" sum across business plans
- Completion rate calculations
- Percentile rankings (optional, for gamification)

---

## Next Steps
1. Audit current data model against these requirements
2. Identify gaps in what's currently collected
3. Design business plan submission form with structured fields
4. Build permission/opt-in system
5. Create aggregation queries for dashboards
