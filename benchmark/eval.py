import json
import re

def extract_first_number(string):
    # This regular expression will match any number including decimals and negative numbers,
    # and possibly followed by a percentage sign.
    match = re.search(r'-?\d+\.?\d*%?', string)
    if match:
        return match.group()
    else:
        return None


def calc_acc(data):
    pred = [x['pred'].lower() for x in data]
    gold = [x['answer'].lower() for x in data]

    error_scale = 0.03
    
    correct_num = 0
    for idx, i in enumerate(pred):        
        if data[idx]['meta_data']['question_type'] == 'numerical':
            if gold[idx][-1] != '%':
                gold_float = float(gold[idx])
            else:
                gold_float = float(gold[idx][:-1]) / 100

            try:
                pred_float = extract_first_number(i)
                if pred_float[-1] != '%':
                    pred_float = float(pred_float)
                else:
                    pred_float = float(pred_float[:-1]) / 100

                lower_bound = min(gold_float * (1-error_scale), gold_float * (1+error_scale))
                upper_bound = max(gold_float * (1-error_scale), gold_float * (1+error_scale))
                if lower_bound < pred_float and upper_bound > pred_float:
                    correct_num += 1
            except:
                # cannot extract number from the prediction
                continue
                
        else:  # question type is multiple choice 
            if gold[idx] == i[:len(gold[idx])]:
                correct_num += 1

    return correct_num / len(pred)

data = json.load(open('tmp.json', 'r'))
print(calc_acc(data))