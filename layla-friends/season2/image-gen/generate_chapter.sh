#!/bin/bash
# Generate all 20 images for S2 CH01 Tier 1

export PATH="$HOME/.local/bin:$PATH"
export GEMINI_API_KEY="AIzaSyBBUAmM4sHkG83tuX9MNiCSYghL21jIeyM"

SCRIPT="/home/ubuntu/.nvm/versions/node/v22.22.0/lib/node_modules/clawdbot/skills/nano-banana-pro/scripts/generate_image.py"
OUTDIR="/home/ubuntu/clawd/layla-friends/season2/image-gen/ch01-tier1"
mkdir -p "$OUTDIR"

STYLE="Children's book illustration, warm painterly style with soft brush strokes. NO TEXT IN IMAGE."
LAYLA="Layla - girl with curly dark brown hair, yellow bow on top, teal hoodie with golden sun design"
RILEY="Riley - girl with straight dark hair, pink bow, purple dress with white stars"
ELLIS="Ellis - boy with blonde hair, blue eyes, orange and blue soccer jersey"
BENNY="Benny - friendly brown teddy bear character wearing green plaid scarf"

generate() {
    local scene=$1
    local prompt=$2
    local outfile="$OUTDIR/S2-CH01-SC$(printf '%02d' $scene)-T1.png"
    
    if [ -f "$outfile" ]; then
        echo "Scene $scene already exists, skipping"
        return
    fi
    
    echo "Generating Scene $scene..."
    for attempt in 1 2 3; do
        if uv run "$SCRIPT" --prompt "$STYLE $prompt" --filename "$outfile" --resolution 1K 2>&1; then
            echo "Scene $scene complete"
            return
        fi
        echo "Attempt $attempt failed, retrying in 5s..."
        sleep 5
    done
    echo "Scene $scene FAILED after 3 attempts"
}

# Scene 1
generate 1 "$LAYLA walking on a sunny neighborhood sidewalk, looking up curiously at a colorful hand-painted sign on a telephone pole. Morning light, suburban street with houses."

# Scene 2  
generate 2 "$LAYLA standing next to a colorful community swap meet sign on a telephone pole. She looks excited reading it. Sunny morning."

# Scene 3
generate 3 "$LAYLA standing excitedly at a front porch doorway. $RILEY in pajamas listening with interest. Cozy house entrance. Morning light."

# Scene 4
generate 4 "Four friends together at a park playground having excited conversation: $LAYLA, $RILEY, $ELLIS, $BENNY. Sunny day, playground equipment in background."

# Scene 5
generate 5 "$LAYLA sitting on her bedroom floor surrounded by toys and items from her closet. She holds up a puzzle box, looking thoughtful."

# Scene 6
generate 6 "$RILEY at her desk in her bedroom with art supplies. She examines colored pencils and sticker sheets, deciding what to bring."

# Scene 7
generate 7 "$ELLIS in his neat organized bedroom, placing a book and toy car into a small box. Clean room with shelves."

# Scene 8
generate 8 "$BENNY in his cozy room, excitedly holding up a colorful bouncy ball in one hand and a small toy drum in the other."

# Scene 9
generate 9 "Four friends walking on neighborhood sidewalk toward community center: $LAYLA, $RILEY, $ELLIS, $BENNY. Each carries a bag or box. Sunny day."

# Scene 10
generate 10 "Community center entrance with busy swap meet. Tables set up, neighbors with boxes, colorful items. $LAYLA, $RILEY, $ELLIS, $BENNY arriving."

# Scene 11
generate 11 "Inside community center. Friendly older Black woman (Mrs. Patterson) greeting four friends warmly. $LAYLA, $RILEY, $ELLIS, $BENNY listening. Folding tables behind."

# Scene 12
generate 12 "$LAYLA, $RILEY, $ELLIS, $BENNY arranging items on a folding table. Table shows puzzle, pencils, book, toy car, drum, bouncy ball."

# Scene 13
generate 13 "Wide shot of busy swap meet inside community center. Colorful items on tables, people browsing. $LAYLA, $RILEY, $ELLIS, $BENNY visible among crowd."

# Scene 14
generate 14 "$RILEY at a craft supplies table, holding watercolor paints with excited expression. Elderly white-haired woman smiles behind the table."

# Scene 15
generate 15 "Close view of hands exchanging colored pencils for watercolor paints. $RILEY and elderly neighbor both smiling at the trade."

# Scene 16
generate 16 "$LAYLA, $RILEY, $ELLIS, $BENNY back at their table, excitedly showing new trades. Riley holds paints, Ellis has magnifying glass."

# Scene 17
generate 17 "$BENNY watching with soft warm smile as a young boy walks away happily banging a toy drum. Touching joyful moment."

# Scene 18
generate 18 "$LAYLA at table with young boy holding puzzle box excitedly. Layla looks through a kaleidoscope. Happy successful trade."

# Scene 19
generate 19 "$LAYLA, $RILEY, $ELLIS, $BENNY sitting on benches outside in golden afternoon light. Each holds new treasures. Peaceful reflective moment."

# Scene 20
generate 20 "$LAYLA, $RILEY, $ELLIS, $BENNY on bench. Layla gestures excitedly with idea while others lean in intrigued. Golden sunset light."

echo "=== GENERATION COMPLETE ==="
ls -la "$OUTDIR"
