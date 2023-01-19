import linecache
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# 用于预测12个问题
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

tokenizer = T5Tokenizer.from_pretrained('castorini/doc2query-t5-base-msmarco')
model = T5ForConditionalGeneration.from_pretrained('castorini/doc2query-t5-base-msmarco')
model.to(device)

passage_path = '/data/students/nieyj/code/docT5query/check/dureader_trans_data.txt00'
print(passage_path)
output_path = '/data/students/nieyj/code/docT5query/check/predicted_queries.txt00'

i = 37246 #就是中断没有数据的那行
while i <= 2024167:  # 
    doc_text = linecache.getline(passage_path, i)
    i = i+1
        
    input_ids = tokenizer.encode(doc_text, truncation=True, return_tensors='pt').to(device)
    outputs = model.generate(
        input_ids=input_ids,
        max_length=64,
        do_sample=True,
        top_k=20,  #10
        num_return_sequences=12)  #3

    for i in range(12):   #3
    #print(f'sample {i + 1}: {tokenizer.decode(outputs[i], skip_special_tokens=True)}')
        query = tokenizer.decode(outputs[i], skip_special_tokens=True)
        if query and (query[-1] != '?'):
            query = query + '?'
            #print(query)
        query = query + ' '
        with open(output_path, 'a+', encoding="utf-8") as f2:
            f2.write(query)
    with open(output_path, 'a+', encoding="utf-8") as f2:
        f2.write('\n')
        

print("预测完成")