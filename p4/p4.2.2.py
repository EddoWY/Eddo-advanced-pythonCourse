def parse_ranges(ranges_string):
    ranges = (r.split('-') for r in ranges_string.split(','))
    return (n for s, e in ((int(s), int(e)) for s, e in ranges) for n in range(s, e + 1))


print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))