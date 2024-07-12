from collections import defaultdict

def node():
  return defaultdict(node)
  
def word_exists(word, node):
    if not word:
        return None in node
    return word_exists(word[1:], node[word[0]])

def add_word(word, node):
    if not word:
       # terminal letter of the word
       node[None]
       return
    add_word(word[1:], node[word[0]])

trie_s = node()
add_word('hello', trie_s)
add_word('world', trie_s)
print('hello exists in trie: ' + str(word_exists('hello', trie_s)))
print('Hello exists in trie: ' + str(word_exists('Hello', trie_s)))
print('hell exists in trie: ' + str(word_exists('hell', trie_s)))
print('world exists in trie: ' + str(word_exists('world', trie_s)))
print('worldt exists in trie: ' + str(word_exists('worldt', trie_s)))
