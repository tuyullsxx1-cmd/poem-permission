import os

POEM = """You lent me your umbrella.
I carried it closed
through the rain,
afraid to open
what was yours.
At your door I gave it back,
dry as I found it.
You laughed.
'It was never the umbrella,'
you said.
'It was the walk.'"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"Wrote {len(POEM)} characters to {path}")


if __name__ == "__main__":
    main()
