# Command Center - Dashboard Prototype

A morning briefing dashboard designed for Justin to get a quick overview of all business activities, priorities, and relevant news in one place.

## Quick Start

Open `prototype.html` in any browser. No build step required.

---

## Sections Overview

### 🌅 Header
- **Command Center** title with gradient styling
- **Live clock** that updates every second
- **Current date** display
- Personalized greeting message

---

### ☀️ Morning Digest (3-card bento grid)

| Card | Purpose |
|------|---------|
| **Weather Widget** | Local weather at a glance (temp, humidity, wind). Helps decide if meetings should be in-person or virtual. |
| **Today's Schedule** | Top 3 calendar events with times and color-coded priority indicators. Quick scan of the day ahead. |
| **Priority Tasks** | Checkbox-style task list of the 4 most urgent items. Interactive checkboxes for satisfaction. |

---

### 🚀 Startup Smartup Panel

| Card | Purpose |
|------|---------|
| **Coalinga-Huron Deal** | Highlighted "hot deal" with the $41.5K pending amount, contract status, and progress bar. Includes last contact date. This is the priority deal to close. |
| **Project Explore Queue** | Visual progress tracker for Books 2-4. Shows which book is in what stage (review, development, outline) with percentage complete. |
| **Active Pipeline** | Quick stats: total pipeline value, prospect count, proposals out, deals closing. High-level sales health. |

---

### 🎓 PFL Academy Panel

| Card | Purpose |
|------|---------|
| **Sales Pipeline** | Breakdown of active deals by state (Colorado, Texas, Florida) with dollar values. Shows where revenue is coming from. |
| **State Mandate Intel** | Live tracking of financial literacy mandates by state. Color-coded by status (Active/Pending/Implementation). Critical for sales targeting. |
| **Conversion Metrics** | Demo-to-proposal and proposal-to-close rates. Month-over-month comparisons. Average deal size. Data-driven sales optimization. |

---

### 📰 News Feed (Tabbed Interface)

Three tabs to avoid information overload:

| Tab | Content | Why It Matters |
|-----|---------|----------------|
| **Tech to Leverage** | AI tools, edtech innovations, automation trends | Find efficiency gains and competitive advantages |
| **After-School Education** | Funding opportunities, program trends, policy changes | Relevant for Project Explore and after-school partnerships |
| **Financial Literacy** | State mandate news, research, advocacy updates | Direct sales intel for PFL Academy |

Each news item shows:
- Category tag (color-coded)
- Headline
- Brief summary
- Source and timestamp

---

### ⚡ Quick Actions

One-click buttons for common tasks:
- **Check Email** - Primary CTA
- **Ask Clawd** - Quick AI assistance
- **Schedule Meeting** - Calendar action
- **Create Proposal** - Sales workflow
- **Research District** - Prospecting
- **View Analytics** - Deep dive
- **Call Coalinga** - Highlighted deal action

---

## Design Notes

### Visual Style
- **Dark mode** optimized for morning/low-light viewing
- **Glass morphism** cards with subtle blur effects
- **Gradient accents** (blue → purple) for brand consistency
- **Color coding**: 
  - 🟢 Emerald = success/active/money
  - 🔵 Blue = primary/info
  - 🟣 Purple = special/featured
  - 🟡 Amber = warning/pending
  - 🔴 Rose = metrics/data

### Tech Stack
- Single HTML file (no build required)
- Tailwind CSS via CDN
- Font Awesome icons
- Vanilla JavaScript (clock + tabs)
- Google Fonts (Inter)

---

## Iteration Ideas

### Phase 2 Enhancements
- [ ] Pull real calendar data (Google Calendar API)
- [ ] Pull real weather (OpenWeather API)
- [ ] Connect to actual CRM for deal data
- [ ] RSS feed integration for news sections
- [ ] Task integration (Todoist/Notion API)

### Phase 3 Enhancements
- [ ] Clawd integration for conversational queries
- [ ] Voice briefing option (TTS summary)
- [ ] Email digest companion
- [ ] Mobile responsive improvements
- [ ] Customizable widgets (drag/drop)

---

## Feedback Requested

1. **Layout** - Is the bento-box arrangement intuitive?
2. **Sections** - Anything missing? Anything unnecessary?
3. **Data priority** - What should be more prominent?
4. **Actions** - What other quick actions would be useful?
5. **News categories** - Are these the right three?

---

*Prototype v0.1 | Built by Clawd | Data is placeholder*
