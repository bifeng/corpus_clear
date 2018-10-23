from mysqlconn import Mysql
import pandas as pd
from read_dict import dirty_word
from datetime import datetime

mysql = Mysql()
rows = mysql.getAll("select * from question_answer  where id > 654447;")

raw = pd.DataFrame(rows)

raw['answer'] = raw.apply(lambda row: row['answer'].decode(), axis=1)
raw['question'] = raw.apply(lambda row: row['question'].decode(), axis=1)


current = datetime.now()
corpus_index = []
for index, row in raw.iterrows():
    if any([True for i in dirty_word if i in row['answer']+row['question']]):
        corpus_index.append(index)
print('elapse {x}'.format(x=datetime.now()-current))


new_raw = raw.iloc[corpus_index, ].copy()



