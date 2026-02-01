from pathlib import Path


def main():
    out_dir = Path("data_sub")
    out_dir.mkdir(parents=True, exist_ok=True)

    pairs = []
    for a in range(20):
        for b in range(10):
            if a >= b:
                pairs.append(f"{a}-{b}={a-b}")

    with open(out_dir / "train.txt", "w", encoding="utf-8") as f:
        for p in pairs:
            f.write(p + "\n")

    with open(out_dir / "val.txt", "w", encoding="utf-8") as f:
        for p in pairs:
            f.write(p + "\n")

    print(f"Sub generated: {len(pairs)} lines")


if __name__ == "__main__":
    main()
