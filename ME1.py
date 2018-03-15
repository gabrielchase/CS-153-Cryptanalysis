import csv
from decimal import *
import string

LETTER_FREQUENCIES = {}
CIPHER_TEXT_1 = """ed’qd cp zvqxcudqz vp apgd. rpk bcpe vwd qkadz xct zp tp l. x mkaa
ypoolvodcv lz ewxv l’o vwlcblcu pm. rpk epkatc’v udv vwlz mqpo xcr
pvwdq ukr. l jkzv excv vp vdaa rpk wpe l’o mddalcu. l upv vp oxbd
rpk kctdqzvxct.
ed’gd bcpec dxyw pvwdq mpq zp apcu. rpkq wdxqv’z nddc xywlcu, nkv
rpk’qd vpp zwr vp zxr lv. lczltd, ed npvw bcpe ewxv’z nddc uplcu pc.
ed bcpe vwd uxod xct ed’qd upccx iaxr lv. xct lm rpk xzb od wpe l’o
mddalcu, tpc’v vdaa od rpk’qd vpp nalct vp zdd. cdgdq upccx ulgd rpk
ki, cdgdq upccx adv rpk tpec, cdgdq upccx qkc xqpkct xct tdzdqv rpk.
cdgdq upccx oxbd rpk yqr, cdgdq upccx zxr upptnrd, cdgdq upccx vdaa
x ald xct wkqv rpk."""


def get_letter_frequencies():
    with open('letter_frequencies.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        for letter, percentage in reader:
            if len(letter) == 1:
                LETTER_FREQUENCIES[letter.lower()] = Decimal(percentage)

def get_cipher_text_letter_frequency(cipher_text):
    alphabet = string.ascii_lowercase
    letter_frequency_dict = {}
    
    for letter in alphabet:
        letter_frequency_dict[letter] = cipher_text.count(letter)
    
    return letter_frequency_dict

def replace_letter(source, before, after):
    return source.replace(before, after)

# get_letter_frequencies()
# print(get_cipher_text_letter_frequency(CIPHER_TEXT_1))
# print(replace_letter(CIPHER_TEXT_1, 'e', 'f'))
