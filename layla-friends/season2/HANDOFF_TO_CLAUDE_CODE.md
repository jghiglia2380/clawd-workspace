# Project Explore Season 2 — Handoff to Claude Code

**Date:** 2026-02-06
**Purpose:** Complete handoff for continuing Season 2 production pipeline
**Owner:** Justin Ghiglia

---

## Executive Summary

You're picking up production work on "Layla & Friends" Season 2 — an animated K-4 financial literacy curriculum. The story arc, scene outlines, and all 48 scripts are COMPLETE. Your job is to:

1. Upload the scripts to Airtable
2. Analyze 320 reference images from Google Drive
3. Generate storyboard prompts that reference those images
4. Ensure script-image alignment

---

## Quick Access — Credentials

### Airtable (Season 2 Base)
- **Base ID:** `app9n9Tz4ppihC1Bb`
- **Base Name:** Project Explore Season 2
- **PAT:** Ask Justin or check `~/.bashrc` for `$AIRTABLE_PAT`
- **API Endpoint:** `https://api.airtable.com/v0/app9n9Tz4ppihC1Bb/`

### GitHub
- **Repo:** https://github.com/jghiglia2380/clawd-workspace
- **Season 2 folder:** `layla-friends/season2/`

### Google Drive (320 Reference Images)
- **Location:** Ask Justin for the folder link — these are the reference images to analyze and incorporate into storyboard prompts

---

## What's Already Done

### ✅ Story Arc (COMPLETE)
- File: `layla-friends/season2/SEASON2_ARC_FINAL.md`
- 12 chapters with full FL concepts, character beats, S1 callbacks
- Cultural diversity: Morocco, Japan, Italy, Mediterranean, Germany, Mexico, Latino USA
- Mr. Mason and Frances "remember a time when..." framing device
- Intergenerational wisdom transfer theme
- Culminates in kids hosting their own Community Market (Ch 12)

### ✅ Scene-by-Scene Outlines (COMPLETE)
- Location: `layla-friends/season2/chapters/`
- 12 files, one per chapter
- Each has 20 scenes with descriptions

### ✅ Scripts (COMPLETE — ALL 48)
- Location: `layla-friends/season2/scripts/`
- Format: `CH{01-12}_TIER{1-4}_FINAL.md`
- Example: `CH05_TIER3_FINAL.md`

### ✅ Airtable Structure (CLEAN)
The Season 2 Airtable base has scaffolding in place:
- 1 Season (Journey to Wonder)
- 12 Chapters (placeholder titles — need updating)
- 240 Scenes (placeholder descriptions — need updating)
- 48 Scripts (empty — need content)
- 12 Activities (empty — need content)
- 0 Storyboard Prompts (need generating)

### ✅ Image Generation Tests
- Location: `layla-friends/season2/image-gen/`
- CH01 Tier 1 has multiple generation attempts
- Prompt JSON files exist for all chapters

---

## What Needs To Be Done

### 1. Update Airtable Chapters with Real Data
The 12 chapters currently have placeholder titles. Update with correct data from `SEASON2_ARC_FINAL.md`:

| CH | Correct Title | FL Concept |
|----|---------------|------------|
| 1 | The Swap Meet | Fair trade, perceived value |
| 2 | The Lemonade Problem | Supply & demand |
| 3 | The Busy Saturday | Specialization, division of labor |
| 4 | Mr. Mason's Trunk | Objects carry stories |
| 5 | The Spice Market | Negotiation, patience |
| 6 | The Fish Auction | Auctions, competition sets price |
| 7 | The Family Bakery | Family business, learning a trade |
| 8 | The Morning Market | Perishables, time-sensitive value |
| 9 | La Vecina's Garden | Local economy, knowing your seller |
| 10 | The Christmas Market | Seasonal demand, handmade value |
| 11 | El Mercado de los Muertos | Value beyond price (meaning, love) |
| 12 | La Tamalada & Community Market | Collaboration, sharing abundance |

### 2. Update Airtable Scenes with Real Descriptions
Pull scene descriptions from `layla-friends/season2/chapters/CH{XX}_*.md` files and update the 240 scene records.

### 3. Upload Scripts to Airtable
Parse the 48 script files and upload to the Scripts table:
- Match to correct Chapter via chapter number
- Set Visual Tier (Tier 1-4)
- Set Reading Level (D for Tier 1, J for Tier 2, M-N for Tier 3, O-P for Tier 4)
- Set Target WPM (75/112/125/146)
- Upload Script Text content
- Calculate Word Count

### 4. Analyze 320 Reference Images
Justin has compiled 320 reference images. You need to:
- Get access to the Google Drive folder
- Analyze/categorize the images (characters, settings, moods, actions)
- Create a reference index that maps images to scene types

### 5. Generate Storyboard Prompts
For each of the 240 scenes × 4 tiers = 960 storyboard prompts:
- Generate from the script text (prompts must match narration EXACTLY)
- Reference specific images from the 320 reference set where appropriate
- Include character tags, setting, action, mood/lighting
- Follow the prompt structure from Season 1

---

## Airtable Table Schemas

### Chapters Table
| Field | Type | Notes |
|-------|------|-------|
| Chapter ID | Formula | Auto: "CH{num} - {title}" |
| Season | Link | Link to Seasons table |
| Chapter Number | Number | 1-12 |
| Chapter Title | Text | Real title from arc |
| Story Spine | Long text | From arc document |
| FL Concepts | Long text | Financial literacy concepts |
| Production Status | Select | Outline/Scripting/Images Pending/Complete |
| Script Status | Select | Not Started/In Progress/Complete/Reviewed |
| Image Status | Select | Not Started/Generating/Review Needed/Complete |

### Scenes Table
| Field | Type | Notes |
|-------|------|-------|
| Scene ID | Text | Format: S2-CH{01-12}-SC{01-20} |
| Chapter | Link | Link to Chapters |
| Scene Number | Number | 1-20 |
| Scene Description | Long text | What happens in scene |
| Production Notes | Long text | Any special notes |

### Scripts Table
| Field | Type | Notes |
|-------|------|-------|
| Script ID | Formula | Auto-generated |
| Chapter | Link | Link to Chapters |
| Reading Level | Select | A through O-P |
| Visual Tier | Select | Tier 1-4 |
| Target WPM | Number | 75/112/125/146 |
| Script Text | Long text | Full script content |
| Word Count | Number | Calculated |
| Script Status | Select | Not Started/Draft/Review Needed/Final |

### Storyboard Prompts Table
| Field | Type | Notes |
|-------|------|-------|
| Scene ID | Text | Reference to scene |
| Visual Tier | Select | Tier 1-4 |
| Full Prompt Text | Long text | Complete image gen prompt |
| Character Tags | Long text | e.g., "layla-tier3, benny-tier3" |
| Setting Tags | Multi-select | Indoor/Outdoor/Garden/etc. |
| Mood Tags | Multi-select | Happy/Excited/Curious/etc. |
| Generation Status | Select | Pending/Generating/Generated/Approved |
| Scene | Link | Link to Scenes table |

---

## Production Rules (From Season 1 Lessons Learned)

### CRITICAL: Script-Image Alignment
- Storyboard prompts MUST match script narration EXACTLY
- If script says "Layla and Riley at the table" — prompt must include BOTH
- Characters, settings, actions, objects must all align

### CRITICAL: Tier Consistency
- All 4 tiers tell the SAME story
- Same characters, same settings, same actions
- Only difference is vocabulary complexity and sentence length

### CRITICAL: Pronouns
| Character | Gender | Pronouns |
|-----------|--------|----------|
| Ellis | MALE | he/him/his |
| Benny | MALE | he/him/his |
| Mr. Mason | MALE | he/him/his |
| Layla | FEMALE | she/her/hers |
| Riley | FEMALE | she/her/hers |
| Frances | FEMALE | she/her/hers |

### Script Specifications by Tier
| Tier | Grade | Words | Avg Sentence | Target WPM | Reading Level |
|------|-------|-------|--------------|------------|---------------|
| 1 | K-1st | 600-750 | 5-10 words | 75 | D |
| 2 | 2nd | 900-1,100 | 9-11 words | 112 | J |
| 3 | 3rd | 1,000-1,200 | 11-12 words | 125 | M-N |
| 4 | 4th | 1,200-1,600 | 14-16 words | 146 | O-P |

---

## Characters (Visual Reference)

### Main Cast
- **Layla** (Protagonist): Yellow bow, teal hoodie with rolled sleeves, adventurous
- **Riley** (Creative): Pink ribbon bows, purple dress with white embroidered flowers
- **Ellis** (Analytical): Blonde hair, athletic build — MALE (he/him)
- **Benny** (Bear): Brown stuffed bear, green scarf ALWAYS, playful

### Mentors
- **Mr. Mason**: Wire-rimmed glasses, blue cardigan, white mustache
- **Frances** (Mr. Mason's wife): Well-worn gardening apron, gentle smile

---

## Recommended Workflow

### Phase 1: Airtable Data Population
```python
# Pseudocode workflow
1. Parse SEASON2_ARC_FINAL.md for chapter metadata
2. Update 12 chapter records with correct titles, FL concepts, story spines
3. Parse chapter outline files for scene descriptions
4. Update 240 scene records with correct descriptions
5. Parse 48 script files
6. Upload script content to Scripts table
```

### Phase 2: Image Reference Analysis
```python
1. Get Google Drive folder access from Justin
2. Download/analyze 320 reference images
3. Categorize by: character, setting, mood, action type
4. Create mapping index for prompt generation
```

### Phase 3: Storyboard Prompt Generation
```python
for chapter in 1..12:
    for scene in 1..20:
        for tier in 1..4:
            script_text = get_script_scene(chapter, tier, scene)
            reference_images = find_matching_references(script_text)
            prompt = generate_prompt(script_text, reference_images)
            upload_to_airtable(prompt)
```

---

## API Examples

### List Chapters
```bash
curl -s "https://api.airtable.com/v0/app9n9Tz4ppihC1Bb/Chapters" \
  -H "Authorization: Bearer $AIRTABLE_PAT"
```

### Update a Chapter
```bash
curl -X PATCH "https://api.airtable.com/v0/app9n9Tz4ppihC1Bb/Chapters/RECORD_ID" \
  -H "Authorization: Bearer $AIRTABLE_PAT" \
  -H "Content-Type: application/json" \
  -d '{"fields": {"Chapter Title": "The Swap Meet", "FL Concepts": "Fair trade, perceived value"}}'
```

### Create Script Records (batch)
```bash
curl -X POST "https://api.airtable.com/v0/app9n9Tz4ppihC1Bb/Scripts" \
  -H "Authorization: Bearer $AIRTABLE_PAT" \
  -H "Content-Type: application/json" \
  -d '{"records": [{"fields": {...}}, ...]}'
```

---

## File Locations Summary

| Content | Location |
|---------|----------|
| Season Arc | `layla-friends/season2/SEASON2_ARC_FINAL.md` |
| Chapter Outlines | `layla-friends/season2/chapters/CH{01-12}_*.md` |
| Scripts | `layla-friends/season2/scripts/CH{01-12}_TIER{1-4}_FINAL.md` |
| Existing Prompts | `layla-friends/season2/image-gen/ch{01-12}-tier1-prompts.json` |
| Test Images | `layla-friends/season2/image-gen/ch01-tier1-v3/` |
| S1 Lessons Learned | `layla-friends/LESSONS_LEARNED.md` |
| Full Project Docs | `layla-friends/PROJECT.md` |

---

## Questions for Justin (Before Starting)

1. **Google Drive folder link** for the 320 reference images
2. **Priority order** — all chapters at once, or chapter-by-chapter?
3. **Image reference strategy** — should prompts cite specific image filenames, or describe the style to match?

---

## Contact

If context is lost, this document plus the `SEASON2_ARC_FINAL.md` file contain everything needed to continue. The scripts are all written — the job is now data pipeline and prompt generation.

**GitHub:** https://github.com/jghiglia2380/clawd-workspace/tree/main/layla-friends/season2
