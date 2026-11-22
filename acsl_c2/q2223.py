debug = False


def process(s: str) -> int:
    # for each character get the ASCII value
    # get the binary string of the ASCII value
    bin_strings = [format(ord(c), "08b") for c in s]
    # print(bin_strings)
    # concatenate it to a big string
    full_str = "".join(bin_strings)
    if debug:
        print(f"full string = {" ".join(bin_strings)}")
    # starting with 0 keep trying to find the indexes of the binary
    # representation of the numbers till you can't.
    next_num: int = 0
    start_idx: int = 0
    last_found = 0
    while True:
        next_str = format(next_num, "b")
        found_idx = full_str.find(next_str, start_idx)
        if debug:
            print(f"find({start_idx}, {next_str}) --> {found_idx}")
        if found_idx == -1:
            break
        last_found = next_num
        next_num = next_num + 1
        # start_idx = found_idx + len(
        #     next_str
        # )  # start after the end of the previous string
        start_idx = 0  # Always search from the first character
    return last_found


input = "Roses are red."
res = process(input)
print(f"For {input} result = {res}")

input = "A stitch in time saves nine."
res = process(input)
print(f"For {input} result = {res}")

input = "Is HackerRabk the platform used by ACSL?"
res = process(input)
print(f"For {input} result = {res}")
