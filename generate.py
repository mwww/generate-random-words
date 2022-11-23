from string import ascii_lowercase, digits
from itertools import product
import time

alp_vowels = ['a', 'e', 'i', 'o', 'u']


def make_random_words(wl: int, m: str, amt_o_al_re_ch: int, al_re_ch_n_vow: bool, on_al_x_amt_o_re_ch_or_les: bool) \
        -> list:
    """

    :param wl: word length.
    :param m: materials. (can anyone suggest a better name?)
    :param amt_o_al_re_ch: amount of allowed repeated chars.
    :param al_re_ch_n_vow: allow repeated chars not vowel.
    :param on_al_x_amt_o_re_ch_or_les: only allow x amount of repeated char or less.
    :return:
    """
    r = []
    for length in range(wl, wl + 1):
        for combo in product(m, repeat=length):
            (prev_letter, is_exit, combo_wo_duplicates) = ("", False, list(dict.fromkeys(combo)))
            for current_letter in list(combo):
                if not prev_letter:
                    prev_letter = current_letter
                    continue
                if prev_letter not in alp_vowels and current_letter not in alp_vowels:
                    is_exit = True
                    break
                prev_letter = current_letter
            if al_re_ch_n_vow and len(combo_wo_duplicates) <= amt_o_al_re_ch:
                is_exit = False
            if is_exit:
                continue
            if not on_al_x_amt_o_re_ch_or_les:
                r.append(''.join(combo))
    return r


def main(conf_og):
    (confk, conf) = (list(conf_og), list(conf_og.values()))
    file_name = f"results/result-{conf[0]}-{conf[1]}-{conf[2]}-{conf[3]}-{conf[4]}.txt"
    print(f"generating {conf[0]} letter(s) words... \n")
    tic = time.perf_counter()
    results = make_random_words(conf[0], conf[1], conf[2], conf[3], conf[4])
    toc = time.perf_counter()
    if len(results) < 1:
        print("no result found \nreturning...")
        return
    print(f"Time to Generate {len(results)} words is {toc - tic:0.4f} seconds\noutput to {file_name} \n\nconfigs:")
    for conf_key in confk:
        print(f"\t{conf_key} = {conf_og[conf_key]}")
    with open(file_name, "w") as results_file:
        for result in results:
            results_file.write(result + "\n")


if __name__ == '__main__':
    # NOTE: ascii_lowercase: "abcdefghijklmnopqrstuvwxyz", digits: "0123456789",
    #       ascii_lowercase + digits: "abcdefghijklmnopqrstuvwxyz0123456789"
    settings = {
        "word_length": 4,
        "materials": ascii_lowercase,
        "amount_of_allowed_repeated_chars": 2,
        "allow_repeated_chars_not_vowel": False,
        "only_allow_x_amount_of_repeated_char_or_less": False,
    }
    main(settings)
