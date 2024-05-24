
def sort_dict_by_keys(dict):
    keys = list(dict.keys())
    keys.sort()
    return {k: dict[k] for k in keys}


def count_chars(str):
    ord_range = range(ord('a'), ord('z')+1)
    chars_dict = {chr(i): 0 for i in ord_range}
    for c in str.lower():
        if ord(c) in ord_range:
            chars_dict[c] += 1
    return chars_dict


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        chars_dict = count_chars(file_contents)

        for k, v in sort_dict_by_keys(chars_dict).items():
            print(f"The '{k}' character was found {v} times")


if __name__ == '__main__':
    main()
