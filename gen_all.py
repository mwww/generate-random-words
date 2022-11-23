from string import ascii_lowercase, digits
from generate import main
import json


def gen_set(wl: int, m: str, amt_o_al_re_ch: int, al_re_ch_n_vow: bool, on_al_x_amt_o_re_ch_or_les: bool):
    return {
        "word_length": wl,
        "materials": m,
        "amount_of_allowed_repeated_chars": amt_o_al_re_ch,
        "allow_repeated_chars_not_vowel": al_re_ch_n_vow,
        "only_allow_x_amount_of_repeated_char_or_less": on_al_x_amt_o_re_ch_or_les,
    }


as_wl = [4, 5, 6, 7, 8, 9]
as_m = [ascii_lowercase, digits, ascii_lowercase + digits]
as_amt_o_al_re_ch = [2]
as_al_re_ch_n_vow = [True, False]
as_on_al_x_amt_o_re_ch_or_les = [True, False]

for cas_wl in as_wl:
    for cas_m in as_m:
        for cas_amt_o_al_re_ch in as_amt_o_al_re_ch:
            for cas_al_re_ch_n_vow in as_al_re_ch_n_vow:
                for cas_on_al_x_amt_o_re_ch_or_les in as_on_al_x_amt_o_re_ch_or_les:
                    print(f"""\ncurrent: {json.dumps(gen_set(cas_wl, cas_m, cas_amt_o_al_re_ch, cas_al_re_ch_n_vow, 
                                                           cas_on_al_x_amt_o_re_ch_or_les), indent = 4)}\n""")

                    main(
                        gen_set(cas_wl, cas_m, cas_amt_o_al_re_ch, cas_al_re_ch_n_vow, cas_on_al_x_amt_o_re_ch_or_les)
                    )
