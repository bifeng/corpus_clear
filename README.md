# corpus_clear

语料过滤，取决于语料本身的质量及语料的用途。  
譬如闲聊语料：
可针对技能包括本地化生活（天气、周围的服务设施）、笑话、诗等场景，抽取或整理相关语料
可针对问答类型包括为什么、是什么、怎么样等问答，抽取或整理相关语料
再根据敏感词等字典方法，过滤相关语料


语料过滤的几种方法：  
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

