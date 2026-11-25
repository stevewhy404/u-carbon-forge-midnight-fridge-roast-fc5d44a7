import os

LINE = "Official apology from your fridge: it will not open after midnight. The leftovers filed a noise complaint at 11:59, and frankly, they have a point."

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
