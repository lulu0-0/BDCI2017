file = open("./data/user_dict.txt","w",encoding = "UTF-8")
lines_seen = set()
result = ''

for line in open('./data/train_cut.txt',encoding = "UTF-8"):
	seg = line.split(' ')
	for index in range(len(seg)):
		word = seg[index].split('/')
		if(word[0] not in lines_seen and word[0] != ''):
			lines_seen.add(word[0])
			result = result + '\n' + word[0] + ' ' + word[1]			
		else:
			break

file.write(result[1:])
file.close()

