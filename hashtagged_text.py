import sys


class Letter:
    def __init__(self, top, midtop, mid, midbottom, bottom):
        self.top = top
        self.midtop = midtop
        self.mid = mid
        self.midbottom = midbottom
        self.bottom = bottom


def s2c(str):
    return getattr(sys.modules[__name__], str)


def text_to_hashtag(text):
    text = text.upper()
    for i, letter in enumerate(text):
        if letter == ' ':
            letter = 'Space'
        if i == 0:
            line_1 = s2c(letter).top
            line_2 = s2c(letter).midtop
            line_3 = s2c(letter).mid
            line_4 = s2c(letter).midbottom
            line_5 = s2c(letter).bottom
        else:
            line_1 = line_1 + s2c(letter).top
            line_2 = line_2 + s2c(letter).midtop
            line_3 = line_3 + s2c(letter).mid
            line_4 = line_4 + s2c(letter).midbottom
            line_5 = line_5 + s2c(letter).bottom
    full_text = line_1 + '\n' + line_2 + '\n' + line_3 + '\n' + line_4 + '\n' + line_5
    return full_text


def boxed_text_to_hashtag(text):
    text = text.upper()
    for i, letter in enumerate(text):
        if letter == ' ':
            letter = 'Space'
        if letter == '+':
            letter = 'Plus'
        if letter == '|':
            letter = 'Bar'
        if i == 0:
            line_1 = '#   ' + s2c(letter).top
            line_2 = '#   ' + s2c(letter).midtop
            line_3 = '#   ' + s2c(letter).mid
            line_4 = '#   ' + s2c(letter).midbottom
            line_5 = '#   ' + s2c(letter).bottom
        else:
            line_1 = line_1 + s2c(letter).top
            line_2 = line_2 + s2c(letter).midtop
            line_3 = line_3 + s2c(letter).mid
            line_4 = line_4 + s2c(letter).midbottom
            line_5 = line_5 + s2c(letter).bottom
    line_1 = line_1 + '#'
    line_2 = line_2 + '#'
    line_3 = line_3 + '#'
    line_4 = line_4 + '#'
    line_5 = line_5 + '#'
    for i in range(int((len(line_1) + 1) / 2)):
        if i == 0:
            line_0a = '# '
            line_0b = '# '
        elif i == int((len(line_1) + 1) / 2 - 1):
            line_0a = line_0a + '#'
            line_0b = line_0b + '#'
        else:
            line_0a = line_0a + '# '
            line_0b = line_0b + '  '
    full_text = line_0a + '\n' + line_0b + '\n' + line_1 + '\n' + line_2 + '\n' + line_3 + '\n' + line_4 + '\n' + \
                line_5 + '\n' + line_0b + '\n' + line_0a
    return full_text


A = Letter('  # # #     ',
           '#       #   ',
           '# # # # #   ',
           '#       #   ',
           '#       #   ')

B = Letter('# # # #     ',
           '#       #   ',
           '# # # #     ',
           '#       #   ',
           '# # # #     ')

C = Letter('  # # # #   ',
           '#           ',
           '#           ',
           '#           ',
           '  # # # #   ')

D = Letter('# # # #     ',
           '#       #   ',
           '#       #   ',
           '#       #   ',
           '# # # #     ')

E = Letter('# # # # #   ',
           '#           ',
           '# # # #     ',
           '#           ',
           '# # # # #   ')

F = Letter('# # # # #   ',
           '#           ',
           '# # # #     ',
           '#           ',
           '#           ')

G = Letter('  # # # #   ',
           '#           ',
           '#   # # #   ',
           '#       #   ',
           '  # # #     ')

H = Letter('#       #   ',
           '#       #   ',
           '# # # # #   ',
           '#       #   ',
           '#       #   ')

I = Letter('# # # # #   ',
           '    #       ',
           '    #       ',
           '    #       ',
           '# # # # #   ')

J = Letter('# # # # #   ',
           '    #       ',
           '    #       ',
           '#   #       ',
           '  #         ')

K = Letter('#       #   ',
           '#     #     ',
           '# # #       ',
           '#     #     ',
           '#       #   ')

L = Letter('#           ',
           '#           ',
           '#           ',
           '#           ',
           '# # # # #   ')

M = Letter('#       #   ',
           '# #   # #   ',
           '#   #   #   ',
           '#       #   ',
           '#       #   ')

N = Letter('#       #   ',
           '# #     #   ',
           '#   #   #   ',
           '#     # #   ',
           '#       #   ')

O = Letter('  # # #     ',
           '#       #   ',
           '#       #   ',
           '#       #   ',
           '  # # #     ')

P = Letter('# # # #     ',
           '#       #   ',
           '# # # #     ',
           '#           ',
           '#           ')

Q = Letter('  # # #     ',
           '#       #   ',
           '#   #   #   ',
           '#     # #   ',
           '  # # # #   ')

R = Letter('# # # #     ',
           '#       #   ',
           '# # # #     ',
           '#     #     ',
           '#       #   ')

S = Letter('  # # # #   ',
           '#           ',
           '  # # #     ',
           '        #   ',
           '# # # #     ')

T = Letter('# # # # #   ',
           '    #       ',
           '    #       ',
           '    #       ',
           '    #       ')

U = Letter('#       #   ',
           '#       #   ',
           '#       #   ',
           '#       #   ',
           '  # # #     ')

V = Letter('#       #   ',
           '#       #   ',
           '  #   #     ',
           '  #   #     ',
           '    #       ')

W = Letter('#       #   ',
           '#       #   ',
           '#   #   #   ',
           '# #   # #   ',
           '#       #   ')

X = Letter('#       #   ',
           '  #   #     ',
           '    #       ',
           '  #   #     ',
           '#       #   ')

Y = Letter('#       #   ',
           '  #   #     ',
           '    #       ',
           '    #       ',
           '    #       ')

Z = Letter('# # # # #   ',
           '      #     ',
           '    #       ',
           '  #         ',
           '# # # # #   ')

Space = Letter('            ',
               '            ',
               '            ',
               '            ',
               '            ')

Plus = Letter('    #       ',
              '    #       ',
              '# # # # #   ',
              '    #       ',
              '    #       ')

Bar = Letter('    #       ',
             '    #       ',
             '    #       ',
             '    #       ',
             '    #       ')
