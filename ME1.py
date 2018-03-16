import csv
import string
import re

from decimal import *

LETTER_FREQUENCIES = {}
CIPHER_TEXT_1 = """\
    ed’qd cp zvqxcudqz vp apgd. rpk bcpe vwd qkadz xct zp tp l. x mkaa
    ypoolvodcv lz ewxv l’o vwlcblcu pm. rpk epkatc’v udv vwlz mqpo xcr
    pvwdq ukr. l jkzv excv vp vdaa rpk wpe l’o mddalcu. l upv vp oxbd
    rpk kctdqzvxct.
    ed’gd bcpec dxyw pvwdq mpq zp apcu. rpkq wdxqv’z nddc xywlcu, nkv
    rpk’qd vpp zwr vp zxr lv. lczltd, ed npvw bcpe ewxv’z nddc uplcu pc.
    ed bcpe vwd uxod xct ed’qd upccx iaxr lv. xct lm rpk xzb od wpe l’o
    mddalcu, tpc’v vdaa od rpk’qd vpp nalct vp zdd. cdgdq upccx ulgd rpk
    ki, cdgdq upccx adv rpk tpec, cdgdq upccx qkc xqpkct xct tdzdqv rpk.
    cdgdq upccx oxbd rpk yqr, cdgdq upccx zxr upptnrd, cdgdq upccx vdaa
    x ald xct wkqv rpk.\
"""
CIPHER_TEXT_2 = """
    xi xh xbedhhxqat udg p rjqt id qt iwt hjb du ild rjqth, p udjgiw edltg
    id qt iwt hjb du ild udjgiw edltgh, dg xc vtctgpa udg pcn cjbqtg iwpi
    xh p edltg vgtpitg iwpc iwt htrdcs id qt iwt hjb du ild axzt edltgh. x
    wpkt sxhrdktgts p igjan bpgktadjh stbdchigpixdc du iwxh egdedhxixdc
    iwpi iwxh bpgvxc xh idd cpggdl id rdcipxc
"""
CIPHER_TEXT_3 = """
    ts tl p zlrorll otyr smps tl cjs djclrdepsrk sj p ferps tkrpo. ts tl
    othr p lsjcr nplsrk jc smr ytrok ntsmjzs wrdjvtcf p qpes jy pcb rktytdr.
"""

CIPHER_TEXT_1 = re.sub( '\s+', ' ', CIPHER_TEXT_1).strip()
CIPHER_TEXT_2 = re.sub( '\s+', ' ', CIPHER_TEXT_2).strip()
CIPHER_TEXT_3 = re.sub( '\s+', ' ', CIPHER_TEXT_3).strip()

replaced_indexes = []


def get_letter_frequencies():
    with open('letter_frequencies.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        for letter, percentage in reader:
            if len(letter) == 1:
                LETTER_FREQUENCIES[letter.lower()] = Decimal(percentage)

get_letter_frequencies()

def get_cipher_text_letter_frequency(cipher_text):
    alphabet = string.ascii_lowercase
    letter_frequency_dict = {}
    
    for letter in alphabet:
        letter_frequency_dict[letter] = cipher_text.count(letter)
    
    return letter_frequency_dict

def replace_letter(source, before, after):
    new_src = source
    
    for idx, ch in enumerate(new_src):
        if ch == before and idx not in replaced_indexes:
            new_src = new_src[:idx] + after + new_src[idx + 1:]
            replaced_indexes.append(idx)

    return new_src

def sort_by_frequency(data):
    sorted_list = {}
    
    for key, val in sorted(data.items(), key=lambda x:x[1], reverse=True):
        sorted_list[key] = val

    return sorted_list

def one_b():
    cipher_text_letter_frequency = get_cipher_text_letter_frequency(CIPHER_TEXT_1)

    new_src = replace_letter(CIPHER_TEXT_1, 'l', 'i') 
    new_src = replace_letter(new_src, 'v', 't') 
    new_src = replace_letter(new_src, 'o', 'm') 
    new_src = replace_letter(new_src, 'd', 'e') 
    new_src = replace_letter(new_src, 'p', 'o') 
    new_src = replace_letter(new_src, 'g', 'v') 
    new_src = replace_letter(new_src, 'y', 'c') 
    new_src = replace_letter(new_src, 'c', 'n') 
    new_src = replace_letter(new_src, 'w', 'h') 
    new_src = replace_letter(new_src, 'z', 's') 
    new_src = replace_letter(new_src, 'u', 'g')
    new_src = replace_letter(new_src, 'b', 'k') 
    new_src = replace_letter(new_src, 'm', 'f') 
    new_src = replace_letter(new_src, 'a', 'l') 
    new_src = replace_letter(new_src, 'e', 'w') 
    new_src = replace_letter(new_src, 'x', 'a') 
    new_src = replace_letter(new_src, 'k', 'u') 
    new_src = replace_letter(new_src, 'r', 'y') 
    new_src = replace_letter(new_src, 'q', 'r') 
    new_src = replace_letter(new_src, 'm', 'v') 
    new_src = replace_letter(new_src, 't', 'd') 
    new_src = replace_letter(new_src, 'q', 'r') 
    new_src = replace_letter(new_src, 'n', 'b') 
    new_src = replace_letter(new_src, 'i', 'p') 
    new_src = replace_letter(new_src, 'q', 'r') 
    
    """
        we’re no strangers to love. you know the rules and so do i. 
        a full commitment is what i’m thinking of. you wouldn’t get 
        this from any other guy. i just want to tell you how i’m feeling. 
        i got to make you understand. we’ve known each other for so long. 
        your heart’s been aching, but you’re too shy to say it. inside, we 
        both know what’s been going on. we know the game and we’re gonna play it. 
        and if you ask me how i’m feeling, don’t tell me you’re too blind to see. 
        never gonna give you up, never gonna let you down, never 
        gonna run around and desert you. never gonna make you cry, 
        never gonna say goodbye, never gonna tell a lie and hurt you.
    """

    return new_src

def two_a():
    cipher_text_letter_frequency = get_cipher_text_letter_frequency(CIPHER_TEXT_2)

    new_src = replace_letter(CIPHER_TEXT_2, 'p', 'a') 
    new_src = replace_letter(new_src, 'x', 'i') 
    new_src = replace_letter(new_src, 'd', 'o') 
    new_src = replace_letter(new_src, 'i', 't') 
    new_src = replace_letter(new_src, 'l', 'w') 
    new_src = replace_letter(new_src, 'u', 'f') 
    new_src = replace_letter(new_src, 'h', 's') 
    new_src = replace_letter(new_src, 'w', 'h') 
    new_src = replace_letter(new_src, 'g', 'r') 
    new_src = replace_letter(new_src, 't', 'e') 
    new_src = replace_letter(new_src, 'q', 'b') 
    new_src = replace_letter(new_src, 'j', 'u') 
    new_src = replace_letter(new_src, 'a', 'l') 
    new_src = replace_letter(new_src, 'b', 'm') 
    new_src = replace_letter(new_src, 'e', 'p') 
    new_src = replace_letter(new_src, 'r', 'c') 
    new_src = replace_letter(new_src, 'c', 'n') 
    new_src = replace_letter(new_src, 'v', 'g') 
    new_src = replace_letter(new_src, 'n', 'y') 
    new_src = replace_letter(new_src, 's', 'd') 
    new_src = replace_letter(new_src, 'k', 'v') 
    new_src = replace_letter(new_src, 'z', 'k') 

    """
        it is impossible for a cube to be the sum of two cubes, 
        a fourth power to be the sum of two fourth powers, or in general
        for any number that is a power greater than the second to be 
        the sum of two like powers. i have discovered a truly marvelous 
        demonstration of this proposition that this margin is too narrow 
        to contain
    """    
    
    return new_src

def three_a():
    cipher_text_letter_frequency = get_cipher_text_letter_frequency(CIPHER_TEXT_3)
    
    new_src = replace_letter(CIPHER_TEXT_3, 'p', 'a') 
    new_src = replace_letter(new_src, 't', 'i') 
    new_src = replace_letter(new_src, 's', 't') 
    new_src = replace_letter(new_src, 'l', 's') 
    new_src = replace_letter(new_src, 'c', 'n') 
    new_src = replace_letter(new_src, 'j', 'o') 
    new_src = replace_letter(new_src, 'm', 'h') 
    new_src = replace_letter(new_src, 'r', 'e') 
    new_src = replace_letter(new_src, 'k', 'd') 
    new_src = replace_letter(new_src, 'o', 'l') 
    new_src = replace_letter(new_src, 'z', 'u') 
    new_src = replace_letter(new_src, 'y', 'f') 
    new_src = replace_letter(new_src, 'h', 'k') 
    new_src = replace_letter(new_src, 'n', 'w') 
    new_src = replace_letter(new_src, 'b', 'y') 
    new_src = replace_letter(new_src, 'd', 'c') 
    new_src = replace_letter(new_src, 'e', 'r') 
    new_src = replace_letter(new_src, 'f', 'g') 
    new_src = replace_letter(new_src, 'q', 'p') 
    new_src = replace_letter(new_src, 'v', 'm') 
    new_src = replace_letter(new_src, 'w', 'b') 

    """ 
        it is a useless life that is not consecrated to a great ideal. 
        it is like a stone wasted on the field without becoming a part of any edifice.
    """

    return new_src


if __name__ == '__main__':
    one_a = get_cipher_text_letter_frequency(CIPHER_TEXT_1)
    one_b = one_b()
    
    replaced_indexes = []
    two_a = two_a()
    replaced_indexes = []
    three_a = three_a()

    print('(1A) {}\n'.format(one_a))
    print('(1B) {}\n'.format(one_b))
    print('(2A) {}\n'.format(two_a))
    print('(3A) {}\n'.format(three_a))
