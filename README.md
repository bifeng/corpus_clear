# corpus_clear

过滤的几种方法：  
1). 布尔值过滤  
a). 字符逐一比较  

    f = DFAFilter()
    f.add("sexy")
    f.filter("hello sexy baby")
    'hello **** baby' 
     
b). 整个字符是否在字符串中  

    "hello sexy baby".replace('sexy','****') if 'sexy' in "hello sexy baby" else 'hello sexy baby'
    'hello **** baby'


2). 先分词，再布尔值过滤  
长脏字和短脏字  

