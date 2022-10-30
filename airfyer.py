import math
import numpy as np

weights = {
    0: 1.0, # liters
    1: 1.0, # rate
    2: 1.0, # watts
    3: 1.0, # price
}

def multiplier(value):
    return 300*math.exp(-0.013*value) + 1

def method1():
    file = open('ops1.txt', 'r')
    results = {}
    for line in file:
        line_parts = line.split(' ')
        if len(line_parts) != (len(weights) + 1):
            print("Houston, we have a problem")
            continue
        params = list(map(lambda x: float(x), line_parts[1:]))
        normalized = []
        for i in range(len(params)):
            value = params[i]
            normalized.append((value*multiplier(value))*weights.get(i))
        line_result = np.sum(normalized)
        link = line_parts[0]
        results.update({link: line_result})
    
    for link in results:
        print(f'{link} -> {results.get(link)}')
    file.close()

params = {
    0: (0.0, 5.0, '+', 1.0), # liters
    1: (0.0, 5.0, '+', 2.0), # rate
    2: (200.0, 500.0, '-', 1.5), # price
}

def method2():
    file = open('ops2.txt', 'r')
    results = {}
    best = ['', 0.0]
    for line in file:
        line_parts = line.split(' ')
        if len(line_parts) != (len(params) + 1):
            print("Houston, we have a problem")
            continue
        par_values = list(map(lambda x: float(x), line_parts[1:]))
        weighted_values = []
        for i in range(len(par_values)):
            value = par_values[i]
            param = params[i]
            normalized = (value - param[0]) / (param[1] - param[0])
            if param[2] == '-':
                normalized = 1 - normalized
            weighted_values.append(normalized*param[3])
        line_result = np.sum(weighted_values)
        link = line_parts[0]
        results.update({link: line_result})

        if line_result > best[1]:
            best = [link, line_result]
    
    file.close()
    
    print('Pontuations:')
    for link in results:
        print(f'{link} -> {results.get(link)}')
    
    print(' ---------- Final Result ----------- ')
    print('Best option:')
    print(f'{best[0]} -> {best[1]}')


if __name__ == '__main__':
    method2()