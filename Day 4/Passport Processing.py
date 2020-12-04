
from pathlib import Path
from pprint import pprint
import re

def read_input(path:str)->list:

    txt_file = Path(path)
    if not txt_file.is_file():
        return []

    passports = []
    passport = {}

    with txt_file.open('r') as f:
        for line in f.readlines():

            raw_line = line.replace('\n', '')

            if len(raw_line) == 0:
                passports.append(passport)
                passport = {}
                continue

            items = raw_line.split(" ")

            for item in items:
                fields = item.split(":")
                passport[fields[0]] = fields[1]

        passports.append(passport)
    return passports

def check_passport(passport:dict)->int:

    if not passport.get("byr"):
        passport["byr"] = "missed"
        return 0
    elif not passport.get("iyr"):
        passport["iyr"] = "missed"
        return 0
    elif not passport.get("eyr"):
        passport["eyr"] = "missed"
        return 0
    elif not passport.get("hgt"):
        passport["hgt"] = "missed"
        return 0
    elif not passport.get("hcl"):
        passport["hcl"] = "missed"
        return 0
    elif not passport.get("ecl"):
        passport["ecl"] = "missed"
        return 0
    elif not passport.get("pid"):
        passport["pid"] = "missed"
        return 0
    elif not passport.get("cid"):
        return 1
    else:
        return 1

def check_passport2(passport:dict)->int:

    if not passport.get("byr"):
        passport["byr"] = "missed"
        return 0
    else:
        if not passport["byr"].isdecimal():
            return 0
        byr_num = int(passport["byr"])

        if byr_num < 1920 or byr_num > 2002:
            return 0

    if not passport.get("iyr"):
        passport["iyr"] = "missed"
        return 0
    else:
        if not passport["iyr"].isdecimal():
            return 0
        byr_num = int(passport["iyr"])

        if byr_num < 2010 or byr_num > 2020:
            return 0

    if not passport.get("eyr"):
        passport["eyr"] = "missed"
        return 0
    else:
        if not passport["eyr"].isdecimal():
            return 0
        byr_num = int(passport["eyr"])

        if byr_num < 2020 or byr_num > 2030:
            return 0

    if not passport.get("hgt"):
        passport["hgt"] = "missed"
        return 0
    else:
        hgt_len = len(passport["hgt"])
        last2chars = passport["hgt"][hgt_len-2:]
        if last2chars != "cm" and last2chars != "in":
            return 0

        hgt = int(passport["hgt"][:hgt_len-2])

        if last2chars == "cm" and (hgt < 150 or hgt > 193):
            return 0
        elif last2chars == "in" and (hgt < 59 or hgt > 76):
            return 0

        # print(hgt)
        # print(last2chars)

    if not passport.get("hcl"):
        passport["hcl"] = "missed"
        return 0
    else:
        if passport["hcl"][0] != "#":
            return 0

        hcl = passport["hcl"][1:]

        if len(hcl) != 6:
            return 0

        wrong_chars = re.findall("[^0-9a-f]", hcl)
        if len(wrong_chars) != 0:
            # print(passport)
            # print(hcl)
            # print(wrong_chars)

            return 0

    if not passport.get("ecl"):
        passport["ecl"] = "missed"
        return 0
    else:
        if passport["ecl"] != "amb"\
                and passport["ecl"] != "blu"\
                and passport["ecl"] != "brn"\
                and passport["ecl"] != "gry"\
                and passport["ecl"] != "grn"\
                and passport["ecl"] != "hzl"\
                and passport["ecl"] != "oth":

            # print(passport)
            # print(passport["ecl"])
            return 0

    if not passport.get("pid"):
        passport["pid"] = "missed"
        return 0
    else:
        if len(passport["pid"]) != 9:
            # print(passport)
            # print(passport["pid"])
            return 0

        if not passport["pid"].isdecimal():
            # print(passport)
            # print(passport["pid"])
            return 0

    return 1

passports = read_input("./input.txt")
# passports = read_input("./test_input.txt")
# pprint(passports)

counter = 0
for passport in passports:
    counter += check_passport2(passport)

pprint(counter)