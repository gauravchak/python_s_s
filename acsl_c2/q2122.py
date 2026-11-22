debug = False


def process(string_to_code: str, key: str) -> str:
    # convert string_to_code to list
    # get ascii code for each character
    vals = [ord(c) for c in string_to_code]
    if debug:
        print(f"Ascii vals of input string = {vals}")
    # generate Fibonacci starting with 1, 2 of the length of string_to_code
    fib_vals = [1] * len(vals)
    if len(fib_vals) >= 2:
        fib_vals[1] = 2
        i = 2
        while i < len(fib_vals):
            fib_vals[i] = fib_vals[i - 1] + fib_vals[i - 2]
            i = i + 1
    if debug:
        print(f"Fib vals = {fib_vals}")
    # convert key to character offset from 'a'
    key_offset: int = ord(key) - ord("a")
    if debug:
        print(f"key offset = {key_offset}")
    # add to Fib values
    fib_vals = [key_offset + v for v in fib_vals]
    # modulo 26 + ord('a')
    # get back character by adding to 'a'
    # get ascii value of each character
    offset_vals = [v % 26 + ord("a") for v in fib_vals]
    if debug:
        print(f"offset_chars = {[chr(v) for v in offset_vals]}")
    # add to ascii code for string_to_code
    final_vals = offset_vals
    for i in range(len(offset_vals)):
        final_vals[i] = final_vals[i] + vals[i]
    # return list of numbers
    return " ".join([str(num) for num in final_vals])


input, key = "ACSL c2", "h"
res = process(input, key)
print(f"For {input}, key={key}: result = {res}")

input, key = "Python Programming", "s"
res = process(input, key)
print(f"For {input}, key={key}: result = {res}")
