from time import time


def quality(x, y, f):
    guessed = 0.0
    total = 0.0
    checked = {x[i]: False for i in xrange(0, len(x))}
    for i in xrange(0, len(x)):
        if checked[x[i]] is False and f.get(x[i], None) is not None:
            total += 1.0
            if f[x[i]] == y[i]:
                guessed += 1.0
            checked[x[i]] = True

    return guessed / total if total != 0.0 else 1.0


if __name__ == "__main__":
    print quality("bfbf aa",
                  "abab ff",
                  {"a": "f", "b": "a", "f": "b"})
    print quality("bfbf aa",
                  "bfbf aa",
                  {"a": "f", "b": "a", "f": "b"})
    print quality("bfbf aa",
                  "bfbf aa",
                  {"a": "f", "b": "b", "f": "a"})
    t = time()
    print quality(
        "bfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aabfbf aa",
        "baba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ffbaba ff",
        {"a": "f", "b": "b", "f": "a"})
    print (time() - t)
