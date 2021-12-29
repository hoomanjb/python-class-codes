import re

# print(re.search('foo-*bar', 'foo--bar'))
#
# print(re.search('foo-+bar', 'foo--bar'))
#
# print(re.search('^foo-+bar', 'foo--bar'))
#
# print(re.search('^foo-?bar', 'foo-bar'))

# print(re.match('^foo[1-9]*harchi', 'fooharchi'))
#
# print(re.match('^foo[1-9]+harchi', 'foo522harchi'))
#
# print(re.match('^foo[1-9]?harchi', 'foo233harchi'))

# print(re.search('<.+?>', '<111>'))

# print(re.search('he?$', 'he'))

# print(re.search('x-{,4}x', 'x-----x'))

# print(re.search('x-{2,4}?', 'x------xxxcx'))

# print(re.search('bar+', 'barrrrr'))
#
# print(re.search('(bar)?', 'barbarbar'))

# print(re.search('(ba[rz]){2,4}(ok)?', 'barbazbaz')) #[a-z]


# print(re.search('(foo(bar)?)+(\d\d\d)?', 'foobar123')) #\d digit , \D none digit

# print(re.search('(\W+),(\W+),(\W+)', ' ,@,#'))
#
# print(re.search('(\w+),(\w+),(\w+)', ' ,2,3'))


# print(re.fullmatch('\d+', '123'))

# print(re.findall('\d+', '123asda345dasd456asdasd987'))


# def is_exist_specific_text(text):
#     return re.search('^[a-zA-Z0-9].', text)
#
# print(is_exist_specific_text('!sd$hlk1239898n'))

# def text_match(text, pattern):
#     if re.search(pattern, text):
#         return 'ok'
#     else:
#         return 'not matched!'
#
# print(text_match('abbb', '^ab{2,3}?$'))
# print(text_match('abc', 'ab*?'))
# print(text_match('abb', 'ab*?'))
# print(text_match('ab123', 'ab*?'))


# ip = "192.168.08.005"
#
# string = re.sub('\.0*', '.', ip)
#
# print(string)



# patterns = ['fox', 'dog', 'horse']
# text = 'The quick brown fox jumps over the lazy dog.'
#
# for pattern in patterns:
#     print(f'search for {pattern} in {text}')
#     if re.search(pattern, text):
#         print(' ok')
#     else:
#         print('not matched')

# pattern = 'fox'
# text = 'The quick brown fox jumps over the lazy dog.'
#
# matched = re.search(pattern, text)
# start = matched.start()
# end = matched.end()
#
# print(f'found at {start} and {end}')

# text = 'hello world'

# print(text.replace(' ', '_'))
# print(re.sub(' ', '_', text))

# dt = '2021-01-01' #yyyy-mm-dd format to dd-mm-yyyy
#
# def convert_datetime(date):
#     return re.sub('(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
#
# print(convert_datetime(dt))

# text = "Ten 10, Twenty 20, Thirty 30"
# result = re.split('\D+', text)
# print(result)
# ---------------------------------









