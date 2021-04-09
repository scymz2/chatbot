import jieba.analyse

text = 'Do you like basketball? How do you feel about the weather'

keywords = jieba.analyse.extract_tags(text, topK=5, withWeight=False, allowPOS=())
print(keywords)
