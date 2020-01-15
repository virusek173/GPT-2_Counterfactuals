import pandas as pd

# pd1 = Readcsv1
# path_contr = 'gpt2_csv_data/gpt2_contrfactual_final_01.csv'
path_contr = 'final_csv_data/train_original.csv'
df_contr = pd.read_csv(path_contr)
# pd2 = readcsv2
# path_non_contr = 'gpt2_csv_data/gpt2_non_contrfactual_final.csv'
path_non_contr = 'final_csv_data/gpt2_generated_final.csv'
df_non_cont = pd.read_csv(path_non_contr)
# concat to one df
together_df = pd.concat([df_contr, df_non_cont])
# suffle 
together_df = together_df.sample(frac=1).reset_index(drop=True)
# Przejęcie  sentenceID od index
together_df['sentenceID'] = together_df.index
# Write to new csv file.
# file_name = 'gpt2_csv_data/gpt2_together_final.csv'
file_name = 'final_csv_data/gpt2_and_original_together_final.csv'
together_df.to_csv(file_name, index=False)
    