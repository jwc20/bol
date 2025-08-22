from anki.collection import Collection
import zstandard


INPUT_PATH = "./collection.anki21b"
OUTPUT_PATH = "./collection.anki2"


def main():
    dctx = zstandard.ZstdDecompressor()
    with open(INPUT_PATH, "rb") as ifh, open(OUTPUT_PATH, "wb") as ofh:
        dctx.copy_stream(ifh, ofh)

        c = Collection(OUTPUT_PATH)
        print(c.find_cards(""))


if __name__ == "__main__":
    main()
