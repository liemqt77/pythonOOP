import random

def distribusi_skor(total, n_item, min_val=1, max_val=5):
    # cek batas logis
    if total < n_item * min_val or total > n_item * max_val:
        return None

    # nilai awal rata-rata
    base = total // n_item
    scores = [base] * n_item
    sisa = total - sum(scores)

    # distribusi sisa secara acak
    while sisa != 0:
        i = random.randint(0, n_item - 1)

        if sisa > 0 and scores[i] < max_val:
            scores[i] += 1
            sisa -= 1
        elif sisa < 0 and scores[i] > min_val:
            scores[i] -= 1
            sisa += 1

    random.shuffle(scores)
    return scores


# ===== LOOP UTAMA =====
while True:
    try:
        n_item = int(input("\nJumlah item (misal 9 / 12): "))
        totals_input = input(
            "Masukkan TOTAL skor (pisahkan koma) atau ketik 'exit': "
        )

        if totals_input.lower() == "exit":
            print("Program selesai.")
            break

        totals = [int(x.strip()) for x in totals_input.split(",")]

        print("\nHasil (copy–paste ke Excel):")
        for t in totals:
            hasil = distribusi_skor(t, n_item)
            if hasil is None:
                print(f"TOTAL {t} ❌ tidak mungkin untuk {n_item} item skala 1–5")
            else:
                print("\t".join(map(str, hasil)) + f"\t{sum(hasil)}")

    except ValueError:
        print("❌ Input tidak valid, coba lagi.")
