for i in range(1, 16+1):
    print('fizz'*(i%3==0) + 'buzz'*(i%5==0) or i)
