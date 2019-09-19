"""
CSCI Project Spellotron
By Mehul Sen
This is an helper program to spellotron.py
Although it can be used independently to correct simple lowercase strings.
"""
dictionary = set()
LEGAL_WORD_FILE = 'american-english.txt'
KEY_ADJACENCY_FILE = 'keyboard-letters.txt'


def getdata(filename):
    """
    This function is used to add the 'american-english.txt' words to the set on initialization.
    :param filename:
    :return:
    """
    with open(filename) as fd:
        for line in fd:
            word = line.strip()
            dictionary.add(word)
    fd.close()


getdata(LEGAL_WORD_FILE)


def configurations(filename):
    """
    This program reads the 'keyboard-letters.txt' file and sets the configurations of keys that lie next to it. It is
    used as a helper function for process1.
    :param filename:
    :return:
    """
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    i = []
    j = []
    k = []
    l = []
    m = []
    n = []
    o = []
    p = []
    q = []
    r = []
    s = []
    t = []
    u = []
    v = []
    w = []
    listx = []
    y = []
    z = []
    with open(filename) as fd:
        for line in fd:
            lst = line.split()
            if lst[0] == 'a':
                for x in range(1, len(lst)):
                    a.append(lst[x])
            if lst[0] == 'b':
                for x in range(1, len(lst)):
                    b.append(lst[x])
            if lst[0] == 'c':
                for x in range(1, len(lst)):
                    c.append(lst[x])
            if lst[0] == 'd':
                for x in range(1, len(lst)):
                    d.append(lst[x])
            if lst[0] == 'e':
                for x in range(1, len(lst)):
                    e.append(lst[x])
            if lst[0] == 'f':
                for x in range(1, len(lst)):
                    f.append(lst[x])
            if lst[0] == 'g':
                for x in range(1, len(lst)):
                    g.append(lst[x])
            if lst[0] == 'h':
                for x in range(1, len(lst)):
                    h.append(lst[x])
            if lst[0] == 'i':
                for x in range(1, len(lst)):
                    i.append(lst[x])
            if lst[0] == 'j':
                for x in range(1, len(lst)):
                    j.append(lst[x])
            if lst[0] == 'k':
                for x in range(1, len(lst)):
                    k.append(lst[x])
            if lst[0] == 'l':
                for x in range(1, len(lst)):
                    l.append(lst[x])
            if lst[0] == 'm':
                for x in range(1, len(lst)):
                    m.append(lst[x])
            if lst[0] == 'n':
                for x in range(1, len(lst)):
                    n.append(lst[x])
            if lst[0] == 'o':
                for x in range(1, len(lst)):
                    o.append(lst[x])
            if lst[0] == 'p':
                for x in range(1, len(lst)):
                    p.append(lst[x])
            if lst[0] == 'q':
                for x in range(1, len(lst)):
                    q.append(lst[x])
            if lst[0] == 'r':
                for x in range(1, len(lst)):
                    r.append(lst[x])
            if lst[0] == 's':
                for x in range(1, len(lst)):
                    s.append(lst[x])
            if lst[0] == 't':
                for x in range(1, len(lst)):
                    t.append(lst[x])
            if lst[0] == 'u':
                for x in range(1, len(lst)):
                    u.append(lst[x])
            if lst[0] == 'v':
                for x in range(1, len(lst)):
                    v.append(lst[x])
            if lst[0] == 'w':
                for x in range(1, len(lst)):
                    w.append(lst[x])
            if lst[0] == 'x':
                for char in range(1, len(lst)):
                    listx.append(lst[char])
            if lst[0] == 'y':
                for x in range(1, len(lst)):
                    y.append(lst[x])
            if lst[0] == 'z':
                for x in range(1, len(lst)):
                    z.append(lst[x])
    fd.close()

    return [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, listx, y, z]


def process1(word):
    """
    This function handles the accidental slipping of finger to write and alternate letter.
    :param word:
    :return:
    """
    if check(word) is False:
        x = 0
        for ch in word:

            prechar = word[:x]
            postchar = word[x + 1:]
            x += 1

            abc = replace1(ch, prechar, postchar)
            if abc is not None:
                return abc

    else:
        return word


def replace1(char, prechar, postchar):
    """
    This is another helper function of process1, it contains each character and runs through the configurations to see
    if a word is formed or not when the character is replaced.
    :param char:
    :param prechar:
    :param postchar:
    :return:
    """
    lst = configurations(KEY_ADJACENCY_FILE)
    if char is 'a':
        for ch in lst[0]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'b':
        for ch in lst[1]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'c':
        for ch in lst[2]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'd':
        for ch in lst[3]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'e':
        for ch in lst[4]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'f':
        for ch in lst[5]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'g':
        for ch in lst[6]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'h':
        for ch in lst[7]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'i':
        for ch in lst[8]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'j':
        for ch in lst[9]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'k':
        for ch in lst[10]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'l':
        for ch in lst[11]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'm':
        for ch in lst[12]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'n':
        for ch in lst[13]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'o':
        for ch in lst[14]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'p':
        for ch in lst[15]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'q':
        for ch in lst[16]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'r':
        for ch in lst[17]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 's':
        for ch in lst[18]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 't':
        for ch in lst[19]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'u':
        for ch in lst[20]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'v':
        for ch in lst[21]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'w':
        for ch in lst[22]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'x':
        for ch in lst[23]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'y':
        for ch in lst[24]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w
    if char is 'z':
        for ch in lst[25]:
            w = prechar + ch + postchar
            if check(w) is True:
                return w


def check(word):
    """
    This function simply checks if the word provided is in the dictionary or not.
    :param word:
    :return:
    """
    return word in dictionary


def process2(word):
    """
    This function accounts for the second problem in the spellotron, it checks if any letters are missing from a word
    and adds them.
    :param word:
    :return:
    """
    if process1(word) is None:
        lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']
        x = 0
        while x < len(word):
            prechar = word[:x + 1]
            postchar = word[x + 1:]
            x += 1
            for ch in lst:
                w = prechar + ch + postchar
                if check(w) is True:
                    return w
    else:
        return process1(word)


def process3(word):
    """
    This function solves the final part of the spellotron, it fixes any extra letter that might have accidentally
    added to the word and removes them.
    :param word:
    :return:
    """
    if process2(word) is None:
        x = 0
        while x < len(word):
            prechar = word[:x]
            postchar = word[x + 1:]
            x += 1
            w = prechar + postchar
            if check(w) is True:
                return w
    else:
        return process2(word)


def speller(word):
    """
    This function combines all the processes, and gives the output, either the word itself if it is correct or False
    if the word is incorrect and the techniques don't work.
    :param word:
    :return:
    """
    if process3(word) is None:
        return False
    else:
        return process3(word)


if __name__ == '__main__':
    """
    This function is just used to check if all aspects of this program are working or not. This is for testing purpose
    only and has nothing to do with the project spellotron itself
    """
    print(process1('labofatory'))
    print(process2('laboatory'))
    print(process3('labonratory'))
    print(speller('thooht'))
    print(check('mr'))
