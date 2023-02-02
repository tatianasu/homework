sequence_= input('введите последовательность чисел через пробел')
number_= int(input('введите любое число'))

sequence_ = sequence_.split()
for i in range(len(sequence_)):
    if sequence_[i].isdigit() == False:
        print('Введенные вами символ(ы) не являются числами')
        break
sequence = []
for i in range(len(sequence_)):
    sequence.append(int(sequence_[i]))


# Сортировка пузырьком 
def babble():
    for i in range(len(sequence)):
        for j in range(len(sequence)-i-1):
            if sequence[j] > sequence[j+1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]        
    print(sequence)

babble()

def check(left, right):
    if left > right or number_ > sequence[right] or number_ < sequence[left]:
        return False # значит элемент отсутствует

def binary_search(left, right):
    middle = (right+left) // 2
    if sequence[middle] < number_ and sequence[middle+1] >= number_ :
        return f'номер позиции элемента, удовлетворяющего условию задачи {middle}'
    elif number_ > sequence[middle] and sequence[middle+1] <= number_:
        return binary_search(middle+1, right)
    else: # иначе в левой
        return binary_search(left, middle-1)

if check(0, len(sequence)-1) == False:
    print('Нет числа, которое бы удовлетворяло условиям задачи')
else:
    print(binary_search(0, len(sequence)-1))