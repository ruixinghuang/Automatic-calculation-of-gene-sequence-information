#!/usr/bin/env python3
# -*-coding:utf-8-*-

import itertools
import csv
s = 'gtattcaacatttccgtgtcgcccttattcccttttttgcggcattttgccttcctgtttttgctcacccagaaacgctggtgaaagtaaaagatgctgaagatcagttgggtgcacgagtgggttacatcgaactggatctcaacagcggtaagatccttgagagttttcgccccgaagaacgttttccaatgatgagcacttttaaagttctgctatgtggcgcggtattatcccgtattgacgccgggcaagagcaactcggtcgccgcatacactattctcagaatgacttggttgagtactcaccagtcacagaaaagcatcttacggatggcatgacagtaagagaattatgcagtgctgccataaccatgagtgataacactgcggccaacttacttctgacaacgatcggaggaccgaaggagctaaccgcttttttgcacaacatgggggatcatgtaactcgccttgatcgttgggaaccggagctgaatgaagccataccaaacgacgagcgtgacaccacgatgcctgtagcaatggcaacaacgttgcgcaaactattaactggcgaactacttactctagcttcccggcaacaattaatagactggatggaggcggataaagttgcaggaccacttctgcgctcggcccttccggctggctggtttattgctgataaatctggagccggtgagcgtgggtctcgcggtatcattgcagcactggggccagatggtaagccctcccgtatcgtagttatctacacgacggggagtcaggcaactatggatgaacgaaatagacagatcgctgagataggtgcctcactgattaagcat'
s = s.upper()
letter_list = ['A', 'T', 'C', 'G']

def get_number(target):
    num = 0
    index = 0
    while index < len(s):
        if s[index:].startswith(target):
            num += 1
        index += 1
    return num


def write_data(target_list, row_num=0):
    number_list = list(map(lambda item: get_number(item), target_list))
    number_list += [sum(number_list)]
   
    percentage_list = list(map(lambda index: round(number_list[index] / float(number_list[-1]), 4), range(len(target_list))))
    if row_num == 0:
        writer.writerow(target_list + ['total']) 
        writer.writerow(number_list)  
        writer.writerow(percentage_list)  
    else:
        target_list = target_list + ['total']
        step = int(len(target_list) / row_num)
        for i in range(row_num):
            start_index = i*step
            end_index = (i+1) * step
            if i == row_num - 1:  
                end_index = None
            writer.writerow(target_list[start_index:end_index])
            writer.writerow(number_list[start_index:end_index])
            writer.writerow(percentage_list[start_index:end_index])


with open("dna.csv", "w") as csvfile:
    writer = csv.writer(csvfile)

    write_data(letter_list)


    two_combine = list(itertools.product(letter_list, repeat=2))
    two_combine_list = list(map(lambda letters: "".join(letters), two_combine))
    write_data(two_combine_list)

    three_combine = list(itertools.product(letter_list, repeat=3))
    three_combine_list = list(map(lambda letters: "".join(letters), three_combine))
    write_data(three_combine_list, row_num=4) 

print("finish")


