import numpy as np
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True, help='input file // FORMAT --> Maestro .fst or .fasta export format compiled with break. See README for more.')
parser.add_argument("-o", "--output", required=True, help='output file // name and extension of your liking')
args = parser.parse_args()

file = open(str(args.input),'r')

file_list = list(file)

number_of_lines = np.arange(0,len(file_list),1)
new_file_list = []
for i in number_of_lines:
    one_line = file_list[i]
    new_file_list.append(one_line.strip('\n'))
    
newList = [element for item in new_file_list for element in item.split(',')]

if file_list[2]=='\n':
    accesion_numbers = newList[::10]
    seq_1s = newList[4::10]
    seq_2s = newList[7::10]
    #print('if')
else:
    accesion_numbers = newList[::7]
    seq_1s = newList[3::7]
    seq_2s = newList[5::7]
    #print('else')

ac_list_of_nums = np.arange(0,len(accesion_numbers),1)
for i in ac_list_of_nums:
    exec('acn_%s = accesion_numbers[%s]' %(i,i))

seq1_list_of_nums = np.arange(0,len(seq_1s),1)
for i in seq1_list_of_nums:
    exec('sq1_%s = seq_1s[%s]' %(i,i))

seq2_list_of_nums = np.arange(0,len(seq_2s),1)
for i in seq2_list_of_nums:
    exec('sq2_%s = seq_2s[%s]' %(i,i))



for i in seq1_list_of_nums:
    exec('a_%s = []' %(i))
    exec('for res in sq1_%s: a_%s.append(res)' %(i,i))
    exec('nirAltina_%s = []' %(i))
    exec('list1_%s = np.arange(len(a_%s))' %(i,i))

for i in seq2_list_of_nums:
    exec('b_%s = []' %(i))
    exec('for res in sq2_%s: b_%s.append(res)' %(i,i))
    exec('list2_%s = np.arange(len(b_%s))' %(i,i))

def Altina_Orion(list1or2_x, nirAltina_x, a, b, j):
    for j in list1or2_x:
        if a[j] != b[j]:
            nirAltina_x.append(j)

for i in seq1_list_of_nums:
    exec('Altina_Orion(list1_%s, nirAltina_%s, a_%s, b_%s, %s)' %(i,i,i,i,i))
    
f = open(str(args.output),"w+")
breakvar = "\n"
for i in seq1_list_of_nums:
    exec('f.write(str(acn_%s)+" "+str(len(nirAltina_%s))+breakvar)'%(i,i))
    f.close
