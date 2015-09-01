#from trie import Trie
import sys

class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert_word(self, word):
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Trie()
            node = node.children[letter]

        node.is_word = True

    def contains(self, word):
        node = self
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]

        return node.is_word

def distance(word, dict_words):
    word_length = len(word)
    dist = sys.maxsize
    row = list(range(word_length+1))
    stack = []
    for child in dict_words.children:
        stack.append((dict_words.children[child], child, row))
    while stack:
        node, letter, prev_row = stack.pop()
        next_row = list(range(word_length+1))
        next_row[0] = prev_row[0]+1
        row_min = sys.maxsize
        for i in range(word_length):
            if word[i] == letter:
                cur_row_min = prev_row[i]
            else:
                cur_row_min = min(next_row[i]+1, prev_row[i]+1, prev_row[i+1]+1)
            next_row[i+1] = cur_row_min
            if cur_row_min < row_min:
                row_min = cur_row_min

        if next_row[-1] < dist and node.is_word:
            dist = next_row[-1]

        if row_min < dist:
            for child in node.children:
                stack.append((node.children[child], child, next_row))

    return dist

def main():
    dictionary = Trie()

    lines = sys.stdin.readlines()
    num_dict_words = int(lines[0])
    dict_words = [x.strip() for x in lines[1:num_dict_words+1]]
    #map(lambda word: dictionary.insert_word(word), dict_words)
    for word in dict_words:
        dictionary.insert_word(word)
    words = [x.strip() for x in lines[num_dict_words+2:]]

    distances = [distance(word, dictionary) for word in words]
    for dist in distances:
        print(dist)
    #print sum(distances)


if __name__ == '__main__':
    sys.exit(main())
