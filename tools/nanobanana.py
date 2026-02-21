#!/usr/bin/env python3
"""Generate and edit images via Nano Banana Pro (gemini-3-pro-image-preview)."""

import argparse
import sys
from pathlib import Path
from typing import Optional

from google import genai
from google.genai import types
from PIL import Image


MODELS = {
    "pro": "gemini-3-pro-image-preview",   # Nano Banana Pro (high fidelity)
    "flash": "gemini-2.5-flash-image",      # Nano Banana (fast/cheap)
}

VALID_ASPECTS = [
    "1:1", "2:3", "3:2", "3:4", "4:3",
    "4:5", "5:4", "9:16", "16:9", "21:9",
]

VALID_SIZES = ["1K", "2K", "4K"]


def _save_images(response, out_path: Path) -> int:
    """Save all images from response. Returns count saved."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    saved = 0
    for i, part in enumerate(response.parts):
        if part.text is not None:
            print(f"[text] {part.text[:200]}")
        elif image := part.as_image():
            if saved == 0:
                target = out_path
            else:
                target = out_path.with_stem(f"{out_path.stem}_{saved}")
            image.save(target)
            print(f"[saved] {target}")
            saved += 1
    return saved


def generate(
    prompt: str,
    out_path: Path,
    aspect: str = "1:1",
    size: str = "2K",
    model_key: str = "pro",
    search: bool = False,
):
    client = genai.Client()

    tools = None
    if search:
        tools = [types.Tool(google_search=types.GoogleSearch())]

    image_cfg_kwargs = {"aspect_ratio": aspect}
    # image_size may not be supported in all SDK versions
    try:
        test_cfg = types.ImageConfig(aspect_ratio="1:1", image_size="2K")
        image_cfg_kwargs["image_size"] = size
    except Exception:
        pass

    config = types.GenerateContentConfig(
        response_modalities=["IMAGE"],
        image_config=types.ImageConfig(**image_cfg_kwargs),
        tools=tools,
    )

    response = client.models.generate_content(
        model=MODELS[model_key],
        contents=prompt,
        config=config,
    )

    saved = _save_images(response, out_path)
    if saved == 0:
        print("[error] No image returned. Full response parts:")
        for p in response.parts:
            print(f"  type={type(p).__name__}, text={getattr(p, 'text', None)}")
        sys.exit(1)


def edit(
    prompt: str,
    input_path: Path,
    out_path: Path,
    aspect: Optional[str] = None,
    size: str = "2K",
    model_key: str = "pro",
):
    client = genai.Client()

    config = types.GenerateContentConfig(
        response_modalities=["IMAGE"],
    )

    if aspect:
        edit_cfg_kwargs = {"aspect_ratio": aspect}
        try:
            types.ImageConfig(aspect_ratio="1:1", image_size="2K")
            edit_cfg_kwargs["image_size"] = size
        except Exception:
            pass
        config = types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(**edit_cfg_kwargs),
        )

    img = Image.open(input_path)

    response = client.models.generate_content(
        model=MODELS[model_key],
        contents=[prompt, img],
        config=config,
    )

    saved = _save_images(response, out_path)
    if saved == 0:
        print("[error] No image returned during edit.")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Nano Banana Pro CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # Generate
    g = sub.add_parser("gen", help="Text to image")
    g.add_argument("--prompt", required=True)
    g.add_argument("--out", required=True)
    g.add_argument("--aspect", default="1:1", choices=VALID_ASPECTS)
    g.add_argument("--size", default="2K", choices=VALID_SIZES)
    g.add_argument("--model", default="pro", choices=list(MODELS))
    g.add_argument("--search", action="store_true",
                   help="Enable Google Search grounding for factual content")

    # Edit
    e = sub.add_parser("edit", help="Image + text editing")
    e.add_argument("--prompt", required=True)
    e.add_argument("--input", required=True, dest="inp")
    e.add_argument("--out", required=True)
    e.add_argument("--aspect", default=None, choices=VALID_ASPECTS)
    e.add_argument("--size", default="2K", choices=VALID_SIZES)
    e.add_argument("--model", default="pro", choices=list(MODELS))

    args = parser.parse_args()

    if args.cmd == "gen":
        generate(args.prompt, Path(args.out), args.aspect, args.size,
                 args.model, args.search)
    elif args.cmd == "edit":
        edit(args.prompt, Path(args.inp), Path(args.out), args.aspect,
             args.size, args.model)


if __name__ == "__main__":
    main()
