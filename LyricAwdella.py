import time
import sys

CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"

lyrics = [
    ("Rasa ini begitu indah", 2.0, False),
    ("Hanya waktu yang salah", 2.0, False),
    ("Ada dia di sisimu", 2.0, False),
    ("Ku terlambat mengenalmu", 1.3, False),
    ("Memiliki pun tak sempat", 1.5, False),
    ("Kar'na keadaan yang tak tepat", 2.4, False),
    
    # Baris 7 → ADA jeda panjang pada "bilaaaaaang"
    (CYAN + "Aku sayang tapi tak bisa bilaaang" + RESET, 0.3, True),

    # Baris 8 → NORMAL tanpa jeda panjang
    (RED + "Aku sayang tapi tak bisa bilang" + RESET, 1.0, False)
]

def type_effect_with_pause(text, enable_long_pause):
    i = 0
    while i < len(text):
        char = text[i]

        # ==== JEDA KHUSUS 1: "tepat" → tahan 2 detik pada "pat" ====
        if text[i:i+3] == "pat":
            for c in "pat":
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.07)
            time.sleep(2)   # jeda dramatis 2 detik
            i += 3
            continue

        # ==== JEDA KHUSUS 2: untuk baris pertama "bilaaaaaaaang" ====
        if enable_long_pause and "aaa" in text:
            if text[i:i+3] == "aaa":   # 8 huruf 'a'
                for c in "aaa":
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(0.07)
                time.sleep(7)  # jeda dramatis 7 detik
                i += 3
                continue

        # Normal typing
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.09)
        i += 1

    print()

# Main
for line, pause, enable_long_pause in lyrics:
    type_effect_with_pause(line, enable_long_pause)
    time.sleep(pause)




                # VERSI NORMAL
# import time
# import sys

# # Warna ANSI (opsional)
# RED = "\033[91m"
# CYAN = "\033[96m"
# RESET = "\033[0m"

# lyrics = [
#     "Rasa ini begitu indah",
#     "Hanya waktu yang salah",
#     "Ada dia di sisimu",
#     "Ku terlambat mengenalmu",
#     "Memiliki pun tak sempat",
#     "Kar'na keadaan yang tak tepat",
#     CYAN + "Aku sayang tapi tak bisa bilang" + RESET,
#     RED + "Aku sayang tapi tak bisa bilang" + RESET
# ]

# def type_effect(text, delay=0.07):
#     for char in text:
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(delay)
#     print()

# # Main
# for line in lyrics:
#     type_effect(line)
#     time.sleep(1.1)   # jeda antar baris
