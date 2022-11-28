from string import ascii_lowercase, digits
from generate import main
import json


def gen_conf(wl: int, m: str, oar: bool, aouc: int):
    return {
        "word_length": wl,
        "materials": m,
        "only_allow_readable": oar,
        "amount_of_unique_chars": aouc,
    }


as_wl = [2, 3, 4, 5, 6, 7, 8, 9]
# as_wl = [6, 7, 8, 9]
as_m = [ascii_lowercase, digits, ascii_lowercase + digits]
as_oar = [True, False]
# as_aouc = [0, 1, 2]
as_aouc = [2]

for cas_wl in as_wl:
    for cas_m in as_m:
        for cas_oar in as_oar:
            for cas_aouc in as_aouc:
                conf = gen_conf(cas_wl, cas_m, cas_oar, cas_aouc)
                print(f"\ncurrent: {json.dumps(conf, indent = 4)}")
                main(conf)
                print("\n---")
                break
