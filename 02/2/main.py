from difflib import get_close_matches


with open('input') as f:
    box_id = list(map(lambda x: x[:-1], f))

for i in box_id:
    matches = get_close_matches(i, box_id, 2, 0.95)
    matches.remove(i)
    if matches:
        solution = ''.join(
            [a if a == b else " " for a, b in zip(i, matches[0])]
        )
        print(f"id:{i}\nma:{matches[0]}\nso:{solution}")
        break
