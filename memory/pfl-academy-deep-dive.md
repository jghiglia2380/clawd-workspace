# PFL Academy - Deep Dive Analysis

*Analysis Date: 2025-01-25*

## Executive Summary

PFL Academy is a **substantially built product** with comprehensive curriculum, state-specific configurations, and a professional tech stack. The infrastructure for the flywheel exists, but I need to verify what's actually LIVE and generating leads.

---

## Product Architecture

### Curriculum Scope
- **45+ chapters** organized into 15 standards
- **Day 1 / Day 2 structure** per chapter (90 total lesson days)
- **Student content**: Learning objectives, key concepts, real-world examples, skill builders
- **Teacher guides**: Implementation notes, discussion prompts, assessment guidance

### Content Quality
Sample from Chapter 1.1 (Jobs vs. Careers):
- Professional, engaging writing
- Real-world examples (Maya's healthcare career, Carlos's tech path)
- Practical skill builders
- Reflection prompts
- **This is publication-ready content.**

### Tech Stack
- **Frontend**: Next.js application
- **Backend**: Supabase (auth, database, storage)
- **Deployment**: Vercel-ready
- **LMS Integration**: Canvas, Schoology (grade passback)

### State Personalization
- **35 states** with graduation requirements documented
- **61 state data files** (simple-data + curriculum adjustments)
- **86+ variables** for state customization
- Each state has unique: standards names, chapter mappings, terminology

---

## The Flywheel Infrastructure

### Lead Gen Assets (Free Tier)
1. **Landing Page** (`free-resources-landing-page.html`)
   - 12 universal categories
   - Professional design (Tailwind CSS)
   - Modal-based chapter exploration

2. **Gateway Page** (`free-resources-gateway.html`)
   - State selection
   - Email capture
   - Routes to state-specific page

3. **State Pages** (template system)
   - State-specific standards display
   - Chapter download buttons
   - Full curriculum download option
   - Generate via: `node generate-state-pages.js`

### Intended User Flow
```
Teacher discovers free PDF →
  Downloads from state page →
    Experiences quality →
      Wants full platform →
        Converts to $26/student paid tier
```

### What's Unclear
- [ ] Are free PDFs actually hosted and accessible?
- [ ] Is the landing page live at a public URL?
- [ ] Is email capture connected to HubSpot/CRM?
- [ ] Are state pages generated and deployed?
- [ ] What's the current conversion funnel metrics?

---

## State Mandate Landscape

### States with Requirements (35 documented)
Alabama, California, Colorado, Connecticut, Delaware, Florida, Georgia, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Michigan, Minnesota, Mississippi, Missouri, Nebraska, New Hampshire, New Jersey, New York, North Carolina, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode Island, South Carolina, Tennessee, Texas, Utah, Virginia, West Virginia, Wisconsin

### Implementation Timeline Highlights
- **California**: 0.5 credit, required for Class of 2031
- **Colorado**: Class of 2027
- **Connecticut**: Class of 2027
- **Florida**: Students entering 9th grade 2023-24 onward
- **Georgia**: Class of 2028
- **Illinois**: Class of 2028
- **Indiana**: Class of 2028

### Opportunity Window
Many states have mandates kicking in 2026-2028. This is THE window to capture market share before teachers commit to other solutions.

---

## Loop Marketing Strategy - What I Need to Understand

Based on Justin's description, the strategy involves:
1. **State DOE backlinks** — Get state departments of education to link to PFL Academy free resources
2. **SEO play** — Rank for "[State] financial literacy curriculum" searches
3. **Content flywheel** — Free PDFs → Email capture → Nurture → Convert

### Key Questions
1. What outreach has been done to state DOEs?
2. Which states have shown interest?
3. What's the email nurture sequence?
4. Where do the 552 free PDFs live?
5. What's the current organic traffic?

---

## Immediate Opportunities

### Quick Wins
1. **Verify live assets** — Are free resources actually accessible?
2. **Deploy state pages** — Generate and host all 35 state landing pages
3. **Connect email to HubSpot** — Ensure captures flow to CRM
4. **Create outreach templates** — For state DOE backlink requests

### Strategic Plays
1. **Target California** — Massive market, mandate kicks in 2027
2. **Target Florida** — Already active, large state
3. **SEO optimization** — State-specific landing pages = long-tail keywords
4. **Teacher community building** — Referral network effect

---

## Competitive Landscape

Need to research:
- NGPF (Next Gen Personal Finance) — Justin mentioned as comparison
- Everfi
- Other state-approved curriculum providers

---

## Questions for Justin

1. **What's the live URL for PFL Academy?** (pflacademy.com is a different company)
2. **Are the free PDFs hosted somewhere? Where?**
3. **Is the email gateway connected to HubSpot?**
4. **What state DOE outreach has been done?**
5. **What's the current traffic/conversion data?**
6. **Can you share the Loop Marketing Strategy doc?**
