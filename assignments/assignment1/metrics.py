def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score
    
    TP=0
    TN=0
    FP=0
    FN=0
    total=len(prediction)
    
    for predicted, actual in zip(prediction, ground_truth):
        if predicted and actual:
            TP+=1
        if not(predicted and actual):
            TN+=1
        if predicted and not actual:
            FP+=1
        else:
            FN+=1
            
    precision = TP/sum(prediction)
    recall = TP/sum(ground_truth)
    accuracy = (TP+TN)/total
    f1 = 2*recall*precision/(precision+recall)
    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy
    return 0
