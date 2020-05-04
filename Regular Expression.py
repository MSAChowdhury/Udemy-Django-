import re

text = "tanshed"
match = re.search('tansh', text)
print(match.start())

def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = ' aba..aabb.asaasa.%.aavv.#asfds..avv..aasss'
#test_pattern =['ab*']
#test_pattern =['ab{}']
#test_pattern =['ab?']
#test_pattern =['ab+']
#test_pattern =['[^.%#]+']
test_pattern =[r'/d+'] #back slash expression
multi_re_find(test_pattern,test_phrase)
