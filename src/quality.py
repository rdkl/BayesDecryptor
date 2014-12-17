from time import time


def quality(x, y, f):
    guessed = 0.0
    total = 0.0
    for i in xrange(0, len(x)):
        x_word = x[i]
        y_word = y[i]
        for j in xrange(0, len(x_word)):
            y_decoded = f.get(x_word[j], None)
            if y_decoded is not None:
                total += 1.0
                if y_decoded == y_word[j]:
                    guessed += 1.0

    return guessed / total if total != 0.0 else 1.0


if __name__ == "__main__":
    print quality(["bfbf aa"],
                  ["abab ff"],
                  {"a": "f", "b": "a", "f": "b"})
    print quality(["bfbf aa"],
                  ["bfbf aa"],
                  {"a": "f", "b": "a", "f": "b"})
    print quality(["bfbf aa"],
                  ["bfbf aa"],
                  {"a": "f", "b": "b", "f": "a"})
    print quality(["bfbf aa", "bfbf aa"],
                  ["bfbf aa", "baba ff"],
                  {"a": "f", "b": "b", "f": "a"})
    t = time()
    print quality(
        "bfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aa",
        "baba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ff",
        {"a": "f", "b": "b", "f": "a"})
    print (time() - t)
