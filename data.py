import numpy as np
import requests

def find_string_with_character(strings, index):
    for i,string in enumerate(strings):
        if i < index:
            continue
        elif string.find(':')!=-1:  
            return i

def creat_dataset(url):
    #Get reponse from request
    response = requests.get(url)

    #Create Dataset
    dataset = {}
    line = response.text.split('\n')[1:]
    index = 0
    indexNxt = 0
    print(line[0])
    for i in range(13):
        index = indexNxt+1
        indexNxt = find_string_with_character(line, index)
        dataset.update({line[index-1]:line[index:indexNxt]})

    dataset.update({line[indexNxt]:line[index:len(line)]})
    return dataset


if __name__ == '__main__':
    url = 'https://www.cs.fsu.edu/~liux/courses/deepRL/assignments/word-test.v1.txt'
    dataset = creat_dataset(url)
