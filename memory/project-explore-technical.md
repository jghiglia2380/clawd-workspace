# Project Explore - Technical Deep Dive

## Production Scale

**Total Output:** 48 videos (12 chapters × 4 tiers)
**Scenes per Video:** 20
**Total Scenes:** 240 unique scenes (same story, 4 art style variants each)

## Content Structure

Each chapter has:
- 20 scenes with evolving artwork per tier
- Narration at tier-appropriate reading level
- Closed captioning (karaoke-style)
- Spanish versions

### Tier Specifications

| Tier | Grade | Target WPM | Word Count | Pause Duration |
|------|-------|------------|------------|----------------|
| 1 | K-1st | 75 | ~600 words | 2.5s between scenes |
| 2 | 2nd | 112 | ~800 words | 0.45s |
| 3 | 3rd | 125 | ~1,000 words | None |
| 4 | 4th | 146 | ~1,170 words | None |

## Characters

**Main Gang:**
- **Ellis** — Male (he/him)
- **Benny** — Male (he/him) [the Bear]
- **Riley** — Female (she/her)
- **Layla** — Female (she/her)

**Guides:**
- **Mr. Mason** — Male (he/him)
- **Frances** — Female (she/her) [Mr. Mason's wife]
- **Ms. Chen** — Female (she/her)

## Tech Stack

### Content Management
- **Airtable** — Master content database for scripts, scenes, metadata

### Audio Production
- **ElevenLabs** — Text-to-speech
  - Voice: Jessica Anne Bogart (ID: lxYfHSkYm1EzQzGhdbfc)
  - Model: eleven_multilingual_v2
  - Settings: Stability 0.2, Similarity 0.45, Style 1.0
- Tier-specific speed settings (0.70 → 1.20)
- Sentence-by-sentence generation with timestamp capture

### Image Generation
- ComfyUI integration (references in repo)
- 20 scenes × 4 art styles = 80 images per chapter
- 960 total images for 12 chapters

### Video Assembly
- Python scripts for rough cuts
- Timestamp-based scene alignment
- Caption overlay

## Production Status (per Jan 5, 2026 doc)

| Component | Status |
|-----------|--------|
| Final Scripts | 35/48 complete, 13 corrupted |
| Pronoun fixes | 116 fixes applied locally |
| Airtable sync | Not pushed |
| Audio files | Need regeneration |
| Images | Need inventory check |
| Videos | Not started |

## Key Files

- `generate_chapter.py` — Core chapter generator
- `generate_sentence_by_sentence.py` — TTS logic
- `render_video.py` — Video assembly
- `Final Scripts/` — Source markdown (48 files needed)
- `Audio/` — Generated audio by chapter/tier

## Reading Level Mapping

| Tier | Reading Levels |
|------|----------------|
| 1 | A-D (use D) |
| 2 | E-J (use J) |
| 3 | K-N (use M-N) |
| 4 | O-P |

## Questions to Clarify

- What exactly is "Book 1" vs "Chapter 1"?
- Are all 12 chapters part of one "book" (Season 1)?
- Or is each chapter a separate "book"?
- Current state of image assets?
- Airtable access credentials?
