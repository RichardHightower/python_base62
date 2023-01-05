import math
import functools

DIGITS = [
    # 0    1    2    3    4    5    6    7    8    9
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    # 10    11   12   13  14   15   16   17    18    19   20  21
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
    # 22    23   24   25  26   27   28   29    30    31   32  33    34  35
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    # 36  37  38   39   40   41    42    43   44  45   46    47
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',  # Easy to add more characters
    # if not using lookup tables.
    # 48  49   50   51   52   53   54   55  56   57   58  59   60   61   // 62   63, 64
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def convert_to_encoded_string(an_id):
    builder = []
    place_holder = find_start_bucket(an_id)
    (_, results, _) = accumulate_digits(place_holder, an_id, builder)
    bucket_value = pow_digits_base(1)
    digit_index = math.floor(results / bucket_value)
    acc = results - (bucket_value * digit_index)
    append_safe(builder, digit_index)
    # Put the remainder in the ones column
    place1_digit_index = math.floor(acc % bucket_value)
    append_safe(builder, place1_digit_index)
    return "".join(builder)


def find_start_bucket(bucket_value):
    index = (i for i in range(0, 14) if bucket_value < pow_digits_base(i))
    try:
        return next(index)
    except StopIteration:
        return 0


def pow_digits_base(exponent):
    return do_pow(exponent, len(DIGITS))

def do_pow(exponent, base):
    if exponent == 0: return 1
    return do_pow(exponent - 1, base) * base


def accumulate_digits(place_holder, acc, builder):
    if place_holder <= 1:
        return [place_holder, acc, builder]

    bucket_value = pow_digits_base(place_holder)
    digit_index = math.floor(acc / bucket_value)
    return accumulate_digits(place_holder - 1, acc - (bucket_value * digit_index), append_safe(builder, digit_index))


def append_safe(builder, digit_index):
    digit_index = math.floor(digit_index)
    if digit_index != 0:
        builder.append(DIGITS[digit_index])
    else:
        if len(builder) > 0:
            builder.append(DIGITS[digit_index])
    return builder


def convert_to_long(str_id):
    return do_convert_to_long(str_id)


def compute_value(c, position):
    digit_index = find_index_of_digit_in_table(c)
    multiplier = pow_digits_base(position)
    return digit_index * multiplier


def foldl(func, acc, xs):
    return functools.reduce(func, xs, acc)


def do_convert_to_long(str_id):
    chars = [char for char in str_id]
    chars.reverse()

    def do_reduce(pos, ch):
        (acc, position) = pos
        value = compute_value(ch, position)
        return acc + value, position + 1

    (result, _) = foldl(do_reduce, (0, 0), chars)
    return result


def find_index_of_digit_in_table(c):
    return DIGITS.index(c)


def main():
    print("Output", convert_to_encoded_string(12345678910), convert_to_long("DTVD3O"))
    long_url = "https://www.somewebiste.com/dp/0201616165/?_encoding=UTF8&pd_rd_w=vwEcs&content-id=amzn1.sym.8cf3b8ef-6a74-45dc-9f0d-6409eb523603&pf_rd_p=8cf3b8ef-6a74-45dc-9f0d-6409eb523603&pf_rd_r=BQ0KD40K57XG761DBNBA&pd_rd_wg=DtkHk&pd_rd_r=f94b60b7-9080-4065-b77f-6377ec854d17&ref_=pd_gw_ci_mcx_mi";
    url_id = abs(hash(long_url))
    short_handle = convert_to_encoded_string(url_id)
    print("url id", url_id, "short handle", short_handle, convert_to_long(short_handle))


if __name__ == "__main__":
    main()
