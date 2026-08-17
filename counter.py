def get_path() -> str:
    while True:
        path = input("please enter the path: ")
        if not path:
            print("please enter path")
            continue
        return path


def read_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("file not found...")
        return ""


def count_sentences(content: str) -> int:
    return content.count(".") + content.count("?") + content.count("!")


def count_lines(content: str) -> int:
    return content.count("\n") + 1


def normalize_string(content: str) -> str:
    return (
        content.replace(".", " ").replace("?", " ").replace("!", " ").replace("\n", " ")
    )


def count_normalized_characters_without_space(content: str) -> int:
    return len(normalize_string(content).replace(" ", ""))


def main():
    path = get_path()
    content = read_file(path)
    words = normalize_string(content).split()
    print(f"""characters(with space) : {len(content)}
characters(without space,enter,dot,?,!) : {count_normalized_characters_without_space(content)}
lines : {count_lines(content)}
sentences : {count_sentences(content)}
words : {len(words)}
""")


if __name__ == "__main__":
    main()
