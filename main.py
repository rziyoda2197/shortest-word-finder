def eng_qisqa_soz(sozlar):
    return min(sozlar, key=len)

sozlar = ["men", "kocha", "yulduz", "kun", "sogin"]
print(eng_qisqa_soz(sozlar))
