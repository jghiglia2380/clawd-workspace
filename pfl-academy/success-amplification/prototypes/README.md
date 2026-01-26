# Success Amplification Prototypes

Interactive HTML prototypes for the PFL Academy Success Amplification system.

## How to View

Open any HTML file directly in your browser:

```bash
# From the prototypes directory
open 01-landing-with-showcase.html
```

Or serve locally:
```bash
cd pfl-academy/success-amplification/prototypes
python -m http.server 8080
# Then visit http://localhost:8080
```

## Pages

| File | Description |
|------|-------------|
| [01-landing-with-showcase.html](01-landing-with-showcase.html) | Landing page with Success Showcase section below H1 |
| [02-student-showcase-gallery.html](02-student-showcase-gallery.html) | Gallery of all student projects with filtering |
| [03-student-portfolio.html](03-student-portfolio.html) | Individual student business plan detail page |
| [04-instructor-profile.html](04-instructor-profile.html) | Instructor spotlight/profile page |
| [05-impact-report.html](05-impact-report.html) | Admin-ready impact report (print/PDF ready) |
| [styles.css](styles.css) | Shared styles matching PFL Academy branding |

## Navigation Flow

```
Landing Page (01)
    ↓
[See What Our Community is Building]
    ↓
Student Showcase Gallery (02) ←→ Instructor Profile (04)
    ↓                                    ↓
Student Portfolio (03)            Impact Report (05)
```

## Design Decisions

### Branding
- Colors pulled from `src/config/branding.ts` in the PFL Academy codebase
- Primary purple gradient: `#4338ca` → `#6d28d9` → `#3730a3`
- Accent: `rgb(79 70 229)`
- Font: System sans-serif (matches site)

### Landing Page Placement
- Success Showcase sits immediately below the hero H1
- Seamless gradient transition from hero to showcase
- Three tabs: Student Projects, Instructor Spotlights, School Success
- Aggregate stats bar for immediate social proof

### Mobile Responsive
- All pages adapt to mobile screens
- Grid layouts collapse to single column
- Touch-friendly tap targets

### Print Ready
- Impact Report (05) has print styles
- Clean output when printed or saved as PDF

## Next Steps

1. **Justin reviews** these prototypes for flow and design
2. **Iterate** based on feedback
3. **Define data model** for what Seb needs to build
4. **Convert to React components** for integration into main site
