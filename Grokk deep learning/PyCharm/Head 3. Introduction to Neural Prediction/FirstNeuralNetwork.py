def neural_network_num_one(input, weight):
    '''
    This neural network makes a prediction of the outcome
     of the match from number of games played
    -------------------------------------------------
    Эта нейронная сеть делает прогноз матча исхода из
    количества сыгранных игр
    '''
    predict = input * weight
    return  predict

def program_launch():
    weight = 0.1
    number_of_toes = [8.5,9.5,10,9]
    input = number_of_toes[0]
    pred = neural_network_num_one(input, weight)
    print(pred)

