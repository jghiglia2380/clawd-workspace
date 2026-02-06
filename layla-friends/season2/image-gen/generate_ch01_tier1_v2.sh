#!/bin/bash
# Generate CH01 Tier 1 images - CORRECT STYLE (flat vector)

export PATH="$HOME/.local/bin:$PATH"

SCRIPT="/home/ubuntu/.nvm/versions/node/v22.22.0/lib/node_modules/clawdbot/skills/nano-banana-pro/scripts/generate_image.py"
OUTDIR="/home/ubuntu/clawd/layla-friends/season2/image-gen/ch01-tier1-v2"
mkdir -p "$OUTDIR"

# TIER 1 STYLE - flat vector, simple, minimal
STYLE="Simple flat vector illustration for young children. Bold clean outlines, flat solid colors, NO gradients, NO texture, NO shading. Minimalistic background with simple shapes. Cartoon style with big round eyes with white sclera and black pupils. Like a children's educational cartoon. NO TEXT IN IMAGE."

# CHARACTER DESCRIPTIONS - matching Season 1
LAYLA="Layla - young girl with dark brown curly puffy hair, big yellow bow on top with yellow headband, brown skin, teal hoodie with happy yellow sun design, teal pants, white shoes, big round cartoon eyes with white sclera"
RILEY="Riley - young girl with straight dark brown hair, pink bow in hair, brown Indian skin tone, purple dress with yellow stars, pink shoes, big round cartoon eyes with white sclera"
ELLIS="Ellis - young boy with short blonde hair, fair skin with rosy cheeks, red-orange shirt with soccer ball design, blue shorts, big round cartoon eyes with white sclera"
BENNY="Benny - friendly brown teddy bear character, green plaid scarf, tan snout, big round eyes with WHITE sclera and black pupils, always smiling"
MRS_P="Mrs. Patterson - friendly older Black woman, gray hair, warm smile, simple dress"
ELDERLY="Elderly woman with white hair, glasses, kind smile, simple cardigan"

generate() {
    local scene=$1
    local prompt=$2
    local outfile="$OUTDIR/S2-CH01-SC$(printf '%02d' $scene)-T1.png"
    
    echo "=== Generating Scene $scene ==="
    for attempt in 1 2 3; do
        if uv run "$SCRIPT" --prompt "$STYLE $prompt" --filename "$outfile" --resolution 1K 2>&1; then
            echo "Scene $scene complete"
            return 0
        fi
        echo "Attempt $attempt failed, retrying in 5s..."
        sleep 5
    done
    echo "Scene $scene FAILED after 3 attempts"
    return 1
}

# Scene 1
generate 1 "$LAYLA walking on a simple sidewalk, looking at a colorful sign on a wooden pole. Simple flat background with blue sky, green grass, brown fence. Minimalistic."

# Scene 2
generate 2 "Close-up of $LAYLA looking excited, happy expression with big smile. Simple colorful background. Flat vector style."

# Scene 3
generate 3 "$LAYLA and $RILEY at a simple door. Layla excited, Riley listening. Simple house entrance, flat colors, minimal details."

# Scene 4
generate 4 "All four friends standing together in a simple park setting: $LAYLA, $ELLIS, $RILEY, $BENNY. Green grass, simple trees, blue sky with clouds. Everyone thinking. Flat vector style."

# Scene 5
generate 5 "$LAYLA in a simple room holding a puzzle box. Minimal furniture, flat colors, simple background."

# Scene 6
generate 6 "$RILEY holding colored pencils and stickers. Simple room background, flat colors, minimal details."

# Scene 7
generate 7 "$ELLIS holding a book and small toy car. Simple room, flat colors, minimal background."

# Scene 8
generate 8 "$BENNY holding a colorful bouncy ball and small drum. Happy expression. Simple room background, flat colors."

# Scene 9
generate 9 "Four friends walking together on a simple path: $LAYLA, $RILEY, $ELLIS, $BENNY. Each carrying items. Simple building ahead, blue sky, green grass. Flat vector style."

# Scene 10
generate 10 "Interior with simple tables. $MRS_P greeting $LAYLA, $RILEY, $ELLIS, $BENNY. Simple items on tables. Flat colors, minimal details, clean lines."

# Scene 11
generate 11 "$MRS_P talking to $LAYLA, $RILEY, $ELLIS, $BENNY, pointing to a table. Simple interior, flat colors."

# Scene 12
generate 12 "$LAYLA, $RILEY, $ELLIS, $BENNY at a table with items displayed: puzzle, pencils, book, toy car, ball, drum. Simple flat style."

# Scene 13
generate 13 "Wide view of simple swap meet room. $LAYLA, $RILEY, $ELLIS, $BENNY browsing. Simple tables with items. Flat colors, minimal details."

# Scene 14
generate 14 "$RILEY looking excited at watercolor paints on a table. $ELDERLY behind table. Simple flat style."

# Scene 15
generate 15 "$RILEY and $ELDERLY trading items. Riley holds paints, woman holds pencils. Both smiling. Simple flat style."

# Scene 16
generate 16 "$LAYLA, $RILEY, $ELLIS, $BENNY together showing their new items. In background, small boy with drum. Simple flat style, minimal details."

# Scene 17
generate 17 "$BENNY smiling warmly watching a happy boy with drum in background. Simple flat style."

# Scene 18
generate 18 "$LAYLA at table with excited little boy pointing at puzzle. Simple flat style, minimal background."

# Scene 19
generate 19 "$LAYLA, $RILEY, $ELLIS, $BENNY sitting on simple bench outside. Each holding new items. Blue sky, simple background. Flat vector style."

# Scene 20
generate 20 "$LAYLA, $RILEY, $ELLIS, $BENNY on bench. Layla gesturing excitedly sharing an idea. Others listening with interest. Simple sunset colors, flat style."

echo "=== GENERATION COMPLETE ==="
ls -la "$OUTDIR"
