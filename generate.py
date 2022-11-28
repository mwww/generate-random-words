from string import ascii_lowercase, digits
from itertools import product as combiner
import time
alp_vowels = ['a', 'e', 'i', 'o', 'u']


def generate(wl: int, m: str, oar: bool, aouc: int) -> list:
    """
    :param wl: word length.
    :param m: materials. (can anyone suggest a better name?)
    :param oar: only allow readable.
    :param aouc: amount of unique chars.
    :return:
    """

    r = []
    for length in range(wl, wl + 1):
        for combo in combiner(m, repeat=length):
            r.append(''.join(combo))
    # check for vowels existence
    if oar:
        (rt, r) = (r, [])
        for combo in rt:
            isCont = False
            for i in range(1, len(combo)):
                # if previous letter and current letter is not vowel then skip it. (skip every double consonant)
                if combo[i-1] not in alp_vowels and combo[i] not in alp_vowels:
                    isCont = True
                    break
            if isCont:
                continue
            r.append(combo)
    # check for unique chars
    if aouc:
        (rt, r) = (r, [])
        for combo in rt:
            unique_chars = list(dict.fromkeys(combo))
            if len(unique_chars) >= aouc:
                r.append(combo)
    return r


def main(conf):
    (confv, output_file_name) = (list(conf.values()), 'result')
    for c in conf:
        output_file_name += f"-{conf[c]}"
    print(f"generating {confv[0]} letter(s) words... \n")
    (tic, results, toc) = time.perf_counter(), generate(confv[0], confv[1], confv[2], confv[3]), time.perf_counter()
    if len(results) < 1:
        print(f"no result found \nwasted time: {toc-tic:0.4f} \nreturning...")
        return
    with open(output_file_name, "w") as results_file:
        results_file.writelines("\n".join(map(str, results)))
    print(f"Time to Generate {len(results)} words is {toc-tic:0.4f} seconds\noutput to {output_file_name} \n\nconfigs:")
    for c in conf:
        print(f"\t{c} = {conf[c]}")


if __name__ == '__main__':
    # NOTE: ascii_lowercase: "abcdefghijklmnopqrstuvwxyz", digits: "0123456789",
    #       ascii_lowercase + digits: "abcdefghijklmnopqrstuvwxyz0123456789"
    settings = {
        "word_length": 4,
        "materials": ascii_lowercase,
        "amount_of_unique_chars": 2,
        "only_allow_readable": True,
    }
    main(settings)
