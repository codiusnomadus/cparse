def switcher(x):
    return {
        'John': 'Baptist',
        'Jack': 'Beanstalk'
    }.get(x, 'Jill')


print(switcher('John'))
