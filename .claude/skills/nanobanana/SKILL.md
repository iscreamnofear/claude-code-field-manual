---
name: nanobanana
description: Generate or edit images using Nano Banana Pro via tools/nanobanana.py.
allowedTools:
  - Bash
  - Read
  - Edit
---

## Setup check
Before first use, verify:
1. `GEMINI_API_KEY` is set in the environment
2. `google-genai` and `pillow` are installed (`pip install -U google-genai pillow`)
3. `tools/nanobanana.py` exists

## Generation
```bash
python tools/nanobanana.py gen \
  --prompt "PROMPT" \
  --aspect "ASPECT" \
  --size "SIZE" \
  --out "outputs/_runs/YYYY-MM-DD/name.png"
```

Required: --prompt, --out
Defaults: --aspect 1:1, --size 2K, --model pro

Valid aspects: 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9
Valid sizes: 1K, 2K, 4K

## Editing
```bash
python tools/nanobanana.py edit \
  --input "path/to/source.png" \
  --prompt "EDIT INSTRUCTIONS" \
  --out "outputs/_runs/YYYY-MM-DD/name_v2.png"
```

## After generation
1. Open the output image and describe what was generated
2. Suggest prompt refinements if quality needs improvement
3. For iterative editing, use the edit command with the previous output as input

## Prompting rules
- Always include "no text, no watermark" unless text is intentionally needed
- Put exact text to render in quotes
- Specify hex colors when brand consistency matters
- Include composition (close-up, wide, isometric, centered)
- Include style (flat vector, photoreal, editorial ink)
- End with aspect ratio context ("wide panoramic" for 21:9, etc.)
