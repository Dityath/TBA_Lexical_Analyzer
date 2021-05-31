# -*- coding: utf-8 -*-
"""TBA Big Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kcYeqFaFgsgWtGMFaAnljHDMS5JNt0R6
"""

#TBA Big Assigment
#Lexical Analyzer
#by :
#Ditya Athallah (1301194095),
#Dzaki Mahadika Gunarto (1301192286), 
#Pernanda Arya Bhagaskara S. M. (1301190184)

import string

#input example
sentence = input()
input_string = sentence.lower() + '#'

#initialization
alphabet_list = list(string.ascii_lowercase)
state_list = ['q0', 'q1', 'q2',	'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48', 'q49', 'q50', 'q51', 'q52', 'q53', 'q54', 'q55', 'q56', 'q57', 'q58']

transition_table = {}

for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state, alphabet)] = 'error'
    transition_table[(state, '#')] = 'error'
    transition_table[(state, '.')] = 'error'

#spaces before input string
transition_table['q0', ' '] = 'q0'

#update the transition table for the following token: awak
transition_table['q0', 'a'] = 'q1'
transition_table['q1', 'w'] = 'q2'
transition_table['q2', 'a'] = 'q3'
transition_table['q3', 'k'] = 'q4'
transition_table['q4', ' '] = 'q58'
transition_table['q4', '#'] = 'accept'
transition_table['q58', ' '] = 'q58'
transition_table['q58', '#'] = 'accept'

#update the transition table for the following token: bermain
transition_table['q0', 'b'] = 'q5'
transition_table['q5', 'e'] = 'q6'
transition_table['q6', 'r'] = 'q7'
transition_table['q7', 'm'] = 'q8'
transition_table['q8', 'a'] = 'q9'
transition_table['q9', 'i'] = 'q10'
transition_table['q10', 'n'] = 'q11'
transition_table['q11', ' '] = 'q58'
transition_table['q11', '#'] = 'accept'

#update the transition table for the following token: catur
transition_table['q0', 'c'] = 'q12'
transition_table['q12', 'a'] = 'q13'
transition_table['q13', 't'] = 'q14'
transition_table['q14', 'u'] = 'q15'
transition_table['q15', 'r'] = 'q16'
transition_table['q16', ' '] = 'q58'
transition_table['q16', '#'] = 'accept'

#update the transition table for the following token: karom
transition_table['q0', 'k'] = 'q17'
transition_table['q17', 'a'] = 'q18'
transition_table['q18', 'r'] = 'q19'
transition_table['q19', 'o'] = 'q20'
transition_table['q20', 'm'] = 'q21'
transition_table['q21', ' '] = 'q58'
transition_table['q21', '#'] = 'accept'

#update the transition table for the following token: kereta
transition_table['q0', 'k'] = 'q17'
transition_table['q17', 'e'] = 'q22'
transition_table['q22', 'r'] = 'q23'
transition_table['q23', 'e'] = 'q24'
transition_table['q24', 't'] = 'q25'
transition_table['q25', 'a'] = 'q26'
transition_table['q26', ' '] = 'q58'
transition_table['q26', '#'] = 'accept'

#update the transition table for the following token: komputer
transition_table['q0', 'k'] = 'q17'
transition_table['q17', 'o'] = 'q27'
transition_table['q27', 'm'] = 'q28'
transition_table['q28', 'p'] = 'q29'
transition_table['q29', 'u'] = 'q30'
transition_table['q30', 't'] = 'q31'
transition_table['q31', 'e'] = 'q32'
transition_table['q32', 'r'] = 'q33'
transition_table['q33', ' '] = 'q58'
transition_table['q33', '#'] = 'accept'

#update the transition table for the following token: memandu
transition_table['q0', 'm'] = 'q34'
transition_table['q34', 'e'] = 'q35'
transition_table['q35', 'm'] = 'q36'
transition_table['q36', 'a'] = 'q37'
transition_table['q37', 'n'] = 'q38'
transition_table['q38', 'd'] = 'q39'
transition_table['q39', 'u'] = 'q40'
transition_table['q40', ' '] = 'q58'
transition_table['q40', '#'] = 'accept'

#update the transition table for the following token: melihat
transition_table['q0', 'm'] = 'q34'
transition_table['q34', 'e'] = 'q35'
transition_table['q35', 'l'] = 'q41'
transition_table['q41', 'i'] = 'q42'
transition_table['q42', 'h'] = 'q43'
transition_table['q43', 'a'] = 'q44'
transition_table['q44', 't'] = 'q45'
transition_table['q45', ' '] = 'q58'
transition_table['q45', '#'] = 'accept'

#update the transition table for the following token: motosikal
transition_table['q0', 'm'] = 'q34'
transition_table['q34', 'o'] = 'q46'
transition_table['q46', 't'] = 'q47'
transition_table['q47', 'o'] = 'q48'
transition_table['q48', 's'] = 'q49'
transition_table['q49', 'i'] = 'q50'
transition_table['q50', 'k'] = 'q51'
transition_table['q51', 'a'] = 'q52'
transition_table['q52', 'l'] = 'q53'
transition_table['q53', ' '] = 'q58'
transition_table['q53', '#'] = 'accept'

#update the transition table for the following token: saya
transition_table['q0', 's'] = 'q54'
transition_table['q54', 'a'] = 'q55'
transition_table['q55', 'y'] = 'q56'
transition_table['q56', 'a'] = 'q57'
transition_table['q57', ' '] = 'q58'
transition_table['q57', '#'] = 'accept'

#transition for new token
transition_table['q58', 'a'] = 'q1'
transition_table['q58', 'b'] = 'q5'
transition_table['q58', 'c'] = 'q12'
transition_table['q58', 'k'] = 'q17'
transition_table['q58', 'm'] = 'q34'
transition_table['q58', 's'] = 'q54'

#lexical analysis
idx_char = 0
state = 'q0'
current_token = ''
while state != 'accept':
    current_char = input_string[idx_char]
    current_token += current_char
    state = transition_table[(state, current_char)]
    if state == 'q4' or state == 'q11' or state == 'q16' or state == 'q21' or state == 'q26' or state == 'q33' or state == 'q40' or state == 'q45' or state == 'q53' or state == 'q57':
        print('current token: ', current_token, ', valid')
        current_token = ''
    if state == 'error':
        print('error')
        break;
    idx_char = idx_char + 1

#conclusion
if state == 'accept':
    print('all tokens in the following sentence: ', sentence, ', valid')