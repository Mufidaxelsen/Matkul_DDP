import time
import sys

# Warna ANSI (cocok untuk Git Bash)
RED = "\033[91m"
RESET = "\033[0m"

lyrics = [
    # "Aku ingin engkau slalu",
    # "Hadir dan temani aku",
    # "Disetiap langkah",
    # "Yang meyakiniku",
    # "Kau tercipta untukku",
    "meski waktu akan mampu",
    RED + "memanggil seluruh ragaku..." + RESET,  # bagian warna merah
    "ku ingin kau tau",
    "ku s'lalu milikmu",
    "yang mencintaimu"
]

def type_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)  # kecepatan typing effect
    print()

# Main loop
for line in lyrics:
    type_effect(line)
    time.sleep(1.2)  # jeda antar baris


# import time
# import sys

# # ANSI Color
# RED = "\033[91m"
# RESET = "\033[0m"

# # Fade intensity
# FADE_STAGES = [
#     "\033[2m",   # dim (redup)
#     "\033[22m",  # normal
#     "\033[1m"    # bright/terang
# ]

# lyrics = [
#     "Aku ingin engkau slalu",
#     "Hadir dan temani aku",
#     "Disetiap langkah",
#     "Yang meyakiniku",
#     "Kau tercipta untukku",
#     "Meski waktu akan mampu",
#     RED + "Memanggil seluruh ragaku" + RESET,  # merah
#     "Ku ingin kau tau",
#     "Kuslalu milikmu",
#     "Yang mencintaimu"
# ]

# def type_effect(text):
#     """Huruf muncul satu per satu"""
#     output = ""
#     for char in text:
#         output += char
#         sys.stdout.write("\r" + output)
#         sys.stdout.flush()
#         time.sleep(0.04)
#     print()

# def fade_in(text):
#     """Teks fade-in dari redup → normal → terang"""
#     for stage in FADE_STAGES:
#         sys.stdout.write("\r" + stage + text + RESET)
#         sys.stdout.flush()
#         time.sleep(0.25)
#     print()

# # Main Process
# for line in lyrics:
#     fade_in(line)       # efek fade-in dulu
#     type_effect(line)   # lalu hurufnya seperti diketik
#     time.sleep(0.6)     # jeda antar baris
