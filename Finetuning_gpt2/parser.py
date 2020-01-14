import pandas as pd
import re 

# Convert from csv to plain text for transformer finetuning.
def data_to_text_parser(df, gold_label):
    df = df.loc[df['gold_label'] == gold_label]
    
    print('df z tylko 0: {}'.format(df))

    text = ' '.join(df.sentence)

    return text

def csv_to_raw_text():
    path = 'data/train.csv'
    df = pd.read_csv(path)
    # positive_text = data_to_text_parser(df, 1)    
    negative_text = data_to_text_parser(df, 0)    
    # print('positive_text: {}'.format(positive_text))

    # with open("contrfactual_text.raw", "w") as text_file:
        # text_file.write(positive_text)

    with open("non_contrfactual_text.raw", "w") as text_file:
        text_file.write(negative_text)

# csv_to_raw_text()

def raw_text_to_csv():
    path = 'gpt2_generated_raw_data/02_gpt2_contrfactual_generated.txt'
    sentences_array = []
    new_sentences_array = []

    with open(path, 'r') as myfile:
        data = myfile.read()
        data = data.rstrip()
        sentences_array = data.split("====================")
        # to list sep .
        for x in sentences_array:
            # print('x: {}'.format(x))
            # print('x.rstrip(): {}'.format(x.rstrip()))
            y = re.sub('[\n]', '', x)
            y_arr = y.split(".")
            del y_arr[-1]
            final_y = '. '.join(y_arr)

            print('final_y: {}'.format(final_y))
            if len(final_y) > 50:
                final_y += '.'
                new_sentences_array.append(final_y)
        # new_sentences_array = [x.rstrip() for x in sentences_array]
        
        # print('data: {}'.format(data))
        # print('sentences_array: {}'.format(sentences_array))
        print('new_sentences_array: {}'.format(new_sentences_array))
        # print('new_sentences_array first el: {}'.format(new_sentences_array[3]))
        print('new_sentences_array len: {}'.format(len(new_sentences_array)))
   
    
    # add columns with values sentenceID, gold_label and sentences

    senIds = range(len(new_sentences_array))
    gold_labels = [1 for _ in range(len(new_sentences_array))]
    d = {'sentenceID': senIds, 'gold_label': gold_labels, 'sentences': new_sentences_array}

    df = pd.DataFrame(data=d)

    print('df: {}'.format(df))

    file_name = 'gpt2_csv_data/gpt2_contrfactual_final_01.csv'
    df.to_csv(file_name, index=False)

    # save created df as csv file

    # with open("gpt2_generated.csv", "w") as text_file:
        # text_file.write(negative_text)

raw_text_to_csv()

