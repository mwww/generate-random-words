from string import ascii_lowercase, digits
from itertools import product as combiner
from datetime import datetime
import time
import math
alp_vowels = ['a', 'e', 'i', 'o', 'u']


def generate(wl: int, m: str, oar: bool, aouc: int) -> list:
    """
    :param wl: word length.
    :param m: materials. (can anyone suggest a better name?)
    :param oar: only allow readable.
    :param aouc: amount of unique chars.
    :return:
    """

    # when you're reading this, you might be asking yourself, is MWWW really this stupid?
    # the short answer is yeaa...
    # but the long version is,
    # kinda(?)
    # see, there's a reason why I wrote it this way, the first is memory, and the second is performance.
    # you can experiment with these code however you want, but my experiment says that, when I check the requirements -
    # directly after combining the seeds/materials is faster and only use a fraction of the memory compared to after -
    # combining the seeds/materials.

    r = []
    if oar and aouc:
        # oar & aouc
        for combo in combiner(m, repeat=wl):
            combo = ''.join(combo)
            # oar
            isCont = False
            for i in range(1, len(combo)):
                # if previous letter and current letter is not vowel then skip it. (skip every double consonant)
                if combo[i-1] not in alp_vowels and combo[i] not in alp_vowels:
                    isCont = True
                    break
            if isCont:
                continue
            # aouc
            unique_chars = list(dict.fromkeys(combo))
            if len(unique_chars) >= aouc:
                r.append(combo)
    elif oar:
        for combo in combiner(m, repeat=wl):
            combo = ''.join(combo)
            # oar
            isCont = False
            for i in range(1, len(combo)):
                # if previous letter and current letter is not vowel then skip it. (skip every double consonant)
                if combo[i-1] not in alp_vowels and combo[i] not in alp_vowels:
                    isCont = True
                    break
            if isCont:
                continue
            r.append(combo)
    elif aouc:
        for combo in combiner(m, repeat=wl):
            combo = ''.join(combo)
            # aouc
            unique_chars = list(dict.fromkeys(combo))
            if len(unique_chars) >= aouc:
                r.append(combo)
    elif not oar and not aouc:
        for combo in combiner(m, repeat=wl):
            r.append(''.join(combo))

    return list(r)


def main(conf):
    confv = list(conf.values())

    output_file_name = 'results/txt/result'
    for c in conf:
        output_file_name += f"-{conf[c]}"

    print(f"{datetime.now()} - generating {confv[0]} letter(s) words... \n")

    tic = time.perf_counter()
    results = generate(confv[0], confv[1], confv[2], confv[3])
    toc = time.perf_counter()

    generate_time = toc - tic

    if len(results) < 1:
        print(f"{datetime.now()} - no result found \nwasted time: {toc-tic:0.4f} \nreturning...")
        return

    with open(output_file_name, "w") as results_file:
        print(f'{datetime.now()} - saving result to {output_file_name}')
        for result in results:
            results_file.write(result + "\n")

    print(f"Time to Generate {len(results)} words is "
          f"{math.floor(generate_time/60)} minutes and {generate_time%60:0.4f} seconds\noutput to {output_file_name}"
          f"\n\nconfigs:")

    for c in conf:
        print(f"\t{c} = {conf[c]}")


if __name__ == '__main__':
    # NOTE: ascii_lowercase: "abcdefghijklmnopqrstuvwxyz", digits: "0123456789",
    #       ascii_lowercase + digits: "abcdefghijklmnopqrstuvwxyz0123456789"
    # settings = {
    #     "word_length": 4,
    #     "materials": ascii_lowercase,
    #     "only_allow_readable": True,
    #     "amount_of_unique_chars": 2,
    # }
    settings = {
        "word_length": 6,
        "materials": ascii_lowercase + digits,
        "only_allow_readable": True,
        "amount_of_unique_chars": 2,
    }
    main(settings)
