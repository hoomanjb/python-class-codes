# a = 'test123test'
#
# email = 'test@test.com'

import re

# email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# 09304857238, 989304857238, +989304857238
# text = 'test123'
# a = re.search(pattern='123', string=text)
# print(a)

# text = 'test653test'
# a = re.search(pattern='[0-9][0-9][0-9]', string=text)
# print(a)


# text = 'test63test'
# a = re.search(pattern='6.+3', string=text)
# print(a)
#
# text = 'test63test'
# a = re.search(pattern='6.*3', string=text)
# print(a)

# text = 'test63test'
# a = re.search(pattern='6?3', string=text)
# print(a)

# text = 'test663test'
# a = re.search(pattern='6+', string=text)
# print(a)

# text = 'a'
# a = re.fullmatch(pattern='a?', string=text)
# print(a)

# text = 'foobarqux'
# a = re.search(pattern='ba[artz]', string=text)
# print(a)

# text = 'foobarqux'
# a = re.search(pattern='^foo', string=text)
# print(a)

# text = '1234'
# a = re.search(pattern='[^0-9]', string=text)
# print(a)

text = '123asdasdasd45'
a = re.search(pattern='^1.+5$', string=text)
print(a)

