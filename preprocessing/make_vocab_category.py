morph_dic = dict()
syl_dic = dict()
def add_dic(word_list):
    for i in word_list:
        if len(i) >= 3 and i[0:3] == '###':
            tmp = i[3:]
            for j in tmp:
                if j in syl_dic:
                    syl_dic[j] += 1
                else:
                    syl_dic[j] = 1
        elif len(i) >= 1 and i[0] == '#':
            tmp = i[1:]
            for j in tmp:
                if j in syl_dic:
                    syl_dic[j] += 1
                else:
                    syl_dic[j] = 1
        else:
            if i in morph_dic:
                morph_dic[i] += 1
            else:
                morph_dic[i] = 1

f = open('./raw_data/category_main_train_data_v3.txt', 'r', encoding='utf8')
while True:
    line = f.readline()
    if not line: break
    lineArr = line.split('\t')[0].split('__eou__')
    add_dic(lineArr[0].split(' '))
    add_dic(lineArr[1].split(' '))
    add_dic(lineArr[2].split(' '))
f.close()

fout_mix = open('./raw_data/dec_mix_vocab_category.txt', 'w', encoding='utf8')
fout_mor = open('./raw_data/enc_mor_vocab_category.txt', 'w', encoding='utf8')
fout_syl = open('./raw_data/enc_syl_vocab_category.txt', 'w', encoding='utf8')

morph_dic = {k: v for k, v in sorted(morph_dic.items(), key=lambda item: item[1], reverse=True)}
syl_dic = {k: v for k, v in sorted(syl_dic.items(), key=lambda item: item[1], reverse=True)}

for k in sorted(morph_dic, key=morph_dic.get, reverse=True):
    fout_mor.write(k+'\n')
    fout_mix.write(k+'\n')
for k in sorted(syl_dic, key=syl_dic.get, reverse=True):
    fout_syl.write(k+'\n')
    fout_mix.write('#'+k+'\n')

fout_mix.close()
fout_mor.close()
fout_syl.close()