import re


def solve():
    normalized_passports = get_and_normalize_input()
    okay_keys, wrong_keys = validate_keys_and_values_in_passports(normalized_passports)
    print("Total is {}, out of which {} passports were okay and {} were wrong".format(len(normalized_passports), okay_keys, wrong_keys))
    okay_values, wrong_values = validate_keys_and_values_in_passports(normalized_passports, value_check=True)
    print("Total is {}, out of which {} passport values were okay and {} were wrong".format(okay_keys, okay_values, wrong_values))


def validate_keys_and_values_in_passports(passport_list, value_check=False):
    okay_keys = wrong_keys = 0
    okay_values = wrong_values = 0
    for kv_pairs in sorted([x for x in passport_list]):
        turbocheck = False

        if len(kv_pairs) < 7:
            wrong_keys += 1
        elif len(kv_pairs) == 7:
            try:
                assert 'cid' not in [x[0] for x in kv_pairs]
                okay_keys += 1
                if value_check:
                    turbocheck = True
            except AssertionError:
                wrong_keys += 1
                continue
            # print("Checking dict {}".format(kv_pairs))
        elif len(kv_pairs) == 8:
            okay_keys += 1
            if value_check:
                turbocheck = True
        else:
            wrong_keys += 1

        if turbocheck:
            wrong = False
            for kv in kv_pairs:
                wrong = False
                if kv[0] == 'byr' and not 1920 <= int(kv[1]) <= 2002:
                    wrong = True
                    break
                elif kv[0] == 'iyr' and not 2010 <= int(kv[1]) <= 2020:
                    wrong = True
                    break
                elif kv[0] == 'eyr' and not 2020 <= int(kv[1]) <= 2030:
                    wrong = True
                    break
                elif kv[0] == 'hgt' and not re.match('1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in', kv[1]):
                    wrong = True
                    break
                elif kv[0] == 'hcl' and not re.match('#[0-9a-f]{6}', kv[1]):
                    wrong = True
                    break
                elif kv[0] == 'ecl' and not kv[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    wrong = True
                    break
                elif kv[0] == 'pid' and not re.match('^[0-9]{9}$', kv[1]):
                    wrong = True
                    break
                elif kv[0] == 'cid':
                    continue
                else:
                    continue
            if not wrong:
                okay_values += 1
            else:
                wrong_values += 1

    if value_check:
        return okay_values, wrong_values
    else:
        return okay_keys, wrong_keys


def get_and_normalize_input():
    with open('./input.txt', 'r') as passportsfile:
        passport_list = []
        single_passport = ''
        for line in passportsfile:
            if line[0] == '\n':
                passport_list += [[elem.split(':') for elem in single_passport[:-1].split(' ')]]
                single_passport = ''
                continue
            else:
                single_passport += "{} ".format(line[:-1])
    return passport_list


if __name__ == "__main__":
    solve()