#!/bin/bash
# Generate CH01 Tier 1 images from new prompts

export PATH="$HOME/.local/bin:$PATH"

SCRIPT="/home/ubuntu/.nvm/versions/node/v22.22.0/lib/node_modules/clawdbot/skills/nano-banana-pro/scripts/generate_image.py"
OUTDIR="/home/ubuntu/clawd/layla-friends/season2/image-gen/ch01-tier1"
mkdir -p "$OUTDIR"

STYLE="Children's book illustration, warm painterly style with soft brush strokes. NO TEXT IN IMAGE."
LAYLA="Layla - girl with curly dark brown hair, yellow bow on top, teal hoodie with golden sun design"
RILEY="Riley - girl with straight dark hair, pink bow, purple dress with white stars"
ELLIS="Ellis - boy with blonde hair, blue eyes, orange and blue soccer jersey"
BENNY="Benny - friendly brown teddy bear character wearing green plaid scarf"
MRS_P="Mrs. Patterson - friendly older Black woman with warm smile"
ELDERLY="Elderly white-haired woman with kind smile and glasses"

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
generate 1 "$LAYLA walking on a sunny neighborhood sidewalk, pausing to look up at a colorful hand-painted sign on a wooden telephone pole. Bright morning light, friendly suburban street with houses and trees."

# Scene 2
generate 2 "Close-up of $LAYLA face lighting up with excitement as she reads the colorful swap meet sign. Her expression shows recognition and joy. Sunny background."

# Scene 3
generate 3 "$LAYLA at $RILEY front porch, knocking excitedly. $RILEY opening the door in casual clothes, listening with growing interest. Cozy house entrance with potted plants. Morning light."

# Scene 4
generate 4 "All four friends gathered at a sunny park playground. $LAYLA explaining excitedly while $ELLIS, $RILEY, and $BENNY listen. Everyone has thoughtful expressions, brainstorming what to bring. Playground equipment in background."

# Scene 5
generate 5 "$LAYLA kneeling on her bedroom floor, looking through her closet. She holds up a colorful puzzle box, examining it thoughtfully. Warm bedroom with toys and books visible."

# Scene 6
generate 6 "$RILEY at her art desk surrounded by creative supplies. She examines short colored pencils and sticker sheets, placing them into a small bag. Colorful, creative bedroom with artwork on walls."

# Scene 7
generate 7 "$ELLIS in his neat, organized bedroom. He holds a chapter book and small toy car, looking at them with a thoughtful expression. Clean shelves with books and trophies in background."

# Scene 8
generate 8 "$BENNY in his cozy, slightly messy room, surprised and happy to rediscover a colorful bouncy ball and small toy drum. He holds both items up with delight."

# Scene 9
generate 9 "Four friends walking together on a neighborhood sidewalk toward a community center building visible ahead: $LAYLA, $RILEY, $ELLIS, $BENNY. Each carries a bag or box of items. Warm sunny day, chatting happily as they walk."

# Scene 10
generate 10 "Interior of community center filled with folding tables covered in items. Neighbors of all ages browsing. $MRS_P greeting $LAYLA, $RILEY, $ELLIS, $BENNY warmly at the entrance. Colorful, busy, welcoming atmosphere."

# Scene 11
generate 11 "$MRS_P explaining the rules to $LAYLA, $RILEY, $ELLIS, $BENNY, gesturing toward an empty spot at a table. Friends listening attentively, holding their items. Swap meet activity in background."

# Scene 12
generate 12 "$LAYLA, $RILEY, $ELLIS, $BENNY arranging their items on a folding table: puzzle box, colored pencils, book, toy car, bouncy ball, small drum. $LAYLA gesturing excitedly to explore. Items neatly displayed."

# Scene 13
generate 13 "Wide shot of the bustling swap meet. $LAYLA, $RILEY, $ELLIS, $BENNY browsing different tables. Diverse neighbors of all ages examining items. Tables full of toys, books, games. Warm, community atmosphere."

# Scene 14
generate 14 "$RILEY at a craft table, eyes wide with excitement at a watercolor paint set. $ELDERLY behind the table smiling kindly. Riley hopeful, eager expression."

# Scene 15
generate 15 "$RILEY and $ELDERLY completing their trade. Riley hands over colored pencils while receiving watercolor paints. Both smiling warmly. Successful, happy exchange."

# Scene 16
generate 16 "$LAYLA, $RILEY, $ELLIS, $BENNY gathered together showing off their trades. Riley holds paints, Ellis has magnifying glass. In background, a young boy walks by happily banging a toy drum. Benny watching and laughing."

# Scene 17
generate 17 "$BENNY watching with a warm, satisfied smile as a young boy in background joyfully plays a drum. Benny expression shows the good feeling of making someone else happy."

# Scene 18
generate 18 "$LAYLA at their table with an excited little boy pointing at her puzzle box. The boy parent stands nearby. Layla smiling, happy to pass on something she loved. Trading moment."

# Scene 19
generate 19 "$LAYLA, $RILEY, $ELLIS, $BENNY sitting together on a bench outside the community center in golden afternoon light. Each examining their new treasures. Peaceful, satisfied moment. Swap meet winding down behind them."

# Scene 20
generate 20 "$LAYLA, $RILEY, $ELLIS, $BENNY on the bench. Layla gesturing with excitement as she shares a new idea. Other friends leaning in with curious, intrigued expressions. Golden sunset light. Seeds of bigger plans."

echo "=== GENERATION COMPLETE ==="
ls -la "$OUTDIR"
