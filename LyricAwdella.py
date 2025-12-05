import time
import sys

# Warna ANSI (opsional)
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

lyrics = [
    "Rasa ini begitu indah",
    "Hanya waktu yang salah",
    "Ada dia di sisimu",
    "Ku terlambat mengenalmu",
    "Memiliki pun tak sempat",
    "Kar'na keadaan yang tak tepat",
    CYAN + "Aku sayang tapi tak bisa bilang" + RESET,
    RED + "Aku sayang tapi tak bisa bilang" + RESET
]

def type_effect(text, delay=0.07):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Main
for line in lyrics:
    type_effect(line)
    time.sleep(1.1)   # jeda antar baris
