import re
def order(sentence):
    if sentence == '':return ''
    interger = re.compile('\D')
    return ' '.join(sorted(sentence.split(" "),key=lambda x: int(interger.sub('',x))))
print order('is2 Thi1s T4est 3a')