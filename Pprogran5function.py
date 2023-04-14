def get_square(number):
    result = number*number

for num in range(0,30,2):
    sq = get_square(num)
    print(num,"square of",sq)