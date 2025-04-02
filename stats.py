# gets word count from given text
def get_word_count(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

# gets character & symbol count from given text
def count_chars(text):
    charDict = {}
    for a in text:
        sub = a.lower()
        if sub not in charDict:
            charDict[sub] = 1
        elif sub in charDict:
            charDict[sub] += 1
    return charDict

def sort_on(dict):
    return dict["count"]

def sort_dict(results):
    sort_res = []
    
    for char in results:
        num = results[char]
        entry = {"character": char, "count": num}
        sort_res.append(entry)
    sort_res.sort(key=sort_on, reverse=True)
    return sort_res


# {'t': 29493, 'h': 19176, 'e': 44538, ' ': 70480, 'p': 5952, 'r': 20079, 'o': 24494, 'j': 497, 'c': 9011, 'g': 5795, 'u': 10111, 'n': 23643, 'b': 4868, 'k': 1661, 'f': 8451, 'a': 25894, 's': 20360, 'i': 23927,
# ';': 1350, ',': 5962, 'm': 10206, 'd': 16318, '\n': 7630, 'y': 7756, 'w': 7450, 'l': 12306, 'v': 3737, '.': 3121, '-': 173, ':': 211, '2': 19, '3': 15, '0': 18, '1': 91, '[': 2, '#': 1, '4': 12, '5': 12, ']': 2,
#  '&': 5, '8': 24, '/': 8, '*': 97, '’': 144, 'x': 691, '_': 124, 'q': 325, '?': 208, '—': 123, '6': 9, 'z': 235, '(': 35, ')': 35, '7': 18, 'æ': 28, '!': 201, '“': 506, '”': 316, '9': 9, 'ë': 2, '‘': 43, 'â': 8,
#  'ê': 7, 'ô': 1, '™': 57, '•': 4, '%': 1, '$': 2}
