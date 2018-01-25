
training = open('Training.txt','r')
output = open('result.txt','w+')

index = -1

while True:
    title_line = training.readline()
    title_line = title_line.strip('\n').split(',')
    index += 1

    if index == 0:
        output.write(','.join(title_line)+'\n')
        continue
    else:
        # line = training.readline()
        # line = line.strip('\n').split(',')
        temp_list = []
        if float(title_line[len(title_line) - 1]) >= 15:
            temp_list.append(str(1))
        else:
            temp_list.append(str(0))
        title_line.pop(5)

        while len(temp_list) < 10:
            line = training.readline()
            line = line.strip('\n').split(',')
            if float(line[len(line) - 1]) >= 15:
                temp_list.append(str(1))
            else:
                temp_list.append(str(0))

        for item in temp_list:
            title_line.append(item)

        output.write(','.join(title_line))
        output.write('\n')
        print(','.join(title_line))
        continue

output.close()
training.close()


