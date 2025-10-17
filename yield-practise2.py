# Zrób generator filter_errors(lines), który:
# przyjmuje listę (np. ["INFO: start", "ERROR: brak paliwa", "INFO: stop", "ERROR: GPS"]),
# używa yield,
# zwraca tylko te linie, które zaczynają się od "ERROR:".
#
# lines = [
#     "INFO: Kierowca Damian rozpoczął kurs.",
#     "ERROR: Brak paliwa.",
#     "INFO: Klient wsiadł do pojazdu.",
#     "ERROR: Awaria GPS."
# ]
#
# for err in filter_errors(lines):
#     print(err)

# *****************************************************************
def filter_errors(lines):
    for line in lines:
        if "ERROR:" in line:
            yield line
        else:
            continue




lines = [
    "INFO: Kierowca Damian rozpoczął kurs.",
    "ERROR: Brak paliwa.",
    "INFO: Klient wsiadł do pojazdu.",
    "ERROR: Awaria GPS."
]

for err in filter_errors(lines):
    print(err)
