import random

def distribusi_skor(total, n_item=9, min_val=1, max_val=5):
    base = total // n_item
    scores = [base] * n_item
    sisa = total - sum(scores)

    # Tambahkan sisa secara acak
    while sisa > 0:
        i = random.randint(0, n_item - 1)
        if scores[i] < max_val:
            scores[i] += 1
            sisa -= 1

    # Pastikan tidak ada nilai di bawah minimum
    for i in range(n_item):
        if scores[i] < min_val:
            diff = min_val - scores[i]
            scores[i] = min_val
            scores[random.randint(0, n_item - 1)] -= diff

    return scores


# ===== LOOP INPUT =====
while True:
    total = input("Masukkan TOTAL skor (atau ketik q untuk keluar): ")

    if total.lower() == 'q':
        print("Program selesai.")
        break

    total = int(total)
    hasil = distribusi_skor(total)

    print("Hasil distribusi (9 item):")
    print("\t".join(map(str, hasil)))
    print("Total:", sum(hasil))
    print("-" * 40)
