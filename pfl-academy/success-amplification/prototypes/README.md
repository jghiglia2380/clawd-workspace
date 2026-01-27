# Success Amplification Prototypes

Interactive HTML prototypes for the PFL Academy Success Amplification system.

## Key Distinction

**PFL Academy** = Personal Financial Literacy for high school credit (daytime, for graduation, letter grades)

**NOT** Startup Smartup (enrichment, afterschool, entrepreneurship)

## How to View

Live at: https://jghiglia2380.github.io/clawd-workspace/pfl-academy/success-amplification/prototypes/01-landing-with-showcase.html

Or open locally:
```bash
cd pfl-academy/success-amplification/prototypes
python -m http.server 8080
# Then visit http://localhost:8080
```

## Pages

| File | Description |
|------|-------------|
| [01-landing-with-showcase.html](01-landing-with-showcase.html) | Landing page with Skills Showcase below H1 |
| [02-skills-showcase.html](02-skills-showcase.html) | Full skills breakdown — 45 chapters, AI scenarios, sample work |
| [04-instructor-profile.html](04-instructor-profile.html) | Instructor spotlight with class progress & skill stats |
| [05-impact-report.html](05-impact-report.html) | Admin-ready impact report (print/PDF ready) |
| [styles.css](styles.css) | Shared styles matching PFL Academy branding |

## What's Showcased (Life Skills, Not Business Plans)

- **Mock Interviews** — AI-simulated job interviews, recorded for review
- **Resume Building** — Portfolio-ready resumes students can use
- **Negotiations** — Landlord, roommate, salary scenarios with AI
- **Budgets** — Personalized financial plans
- **45 Chapters** — Career readiness, banking, insurance, taxes, etc.

## Privacy Considerations

- Students are minors — no personal info shown
- Sample work is anonymized/redacted
- Aggregate stats only (X interviews completed, Y% improvement)
- Individual student showcase removed — focus is on skills & instructors

## Navigation Flow

```
Landing Page (01)
    ↓
[Real Skills. Real Practice. Real Results.]
    ↓
Skills Showcase (02) ←→ Instructor Profile (04)
                              ↓
                        Impact Report (05)
```

## Design Decisions

- **Branding:** Colors from `src/config/branding.ts`
- **Focus:** Skills practiced, not individual student work
- **Aggregate Stats:** Mock interviews completed, resumes built, completion rates
- **AI Scenarios:** Highlight the recorded practice conversations
- **Print-Ready:** Impact Report styled for PDF output
