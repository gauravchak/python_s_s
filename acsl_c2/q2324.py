debug = False


def process(book: str, message: str) -> str:
    book_sentences = book.split(".  ")
    if debug:
        print(
            f"Number of sentences in book = {len(book_sentences)} and sentences = {book_sentences}."
        )
    swclist = message.split(" ")
    outlist = []
    for swc in swclist:
        nums = swc.split(".")
        if len(nums) != 3:
            continue
        sentence_idx, word_idx, char_idx = (
            int(nums[0]) - 1,
            int(nums[1]) - 1,
            int(nums[2]) - 1,
        )
        if debug:
            print(f"indexes = {nums}")
        if sentence_idx >= len(book_sentences):
            outlist.append(" ")
        else:
            words = book_sentences[sentence_idx].split(" ")
            if word_idx >= len(words):
                outlist.append(" ")
            else:
                word = words[word_idx]
                if char_idx >= len(word):
                    outlist.append(" ")
                else:
                    if debug:
                        print(f"Char {char_idx} of {word}")
                    outlist.append(list(word)[char_idx])
    return "".join(outlist)


input = "ACSL is an international computer science competition among more than 300 schools.  With countrywide and worldwide participants it became the American Computer Science League.  It has been in continuous existence since 1978.  Each yearly competition consists of 4 regular season contests.  All students at each school may compete but the team score is the sum of the best 3 or 5 top scores.  Each contest consists of a written section and a programming section."
message = "1.5.4 4.2.6 1.10.1 3.2.1 6.11.6 2.9.8 4.10.3 5.18.1"
res = process(book=input, message=message)
print(f"Result - {res}")

input = "To be or not to be that is the question is a quote by William Shakespeare.  2B or not 2B is also a Boolean expression.  Write it both ways."
message = "2.1.2 1.3.1 1.4.2 2.8.4 1.13.5 2.7.1 2.3.1 1.17.2 1.15.5 1.10.4 4.1.1 1.15.6 2.8.4 3.4.1 1.7.3 3.4.3 1.16.6 3.3.5 1.1.1 1.3.2 1.13.2 1.10.3"
res = process(book=input, message=message)
print(f"Result - {res}")
