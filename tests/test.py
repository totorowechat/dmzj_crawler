import json

l = ['1', '中文', '3']

j = json.dumps(l, ensure_ascii=False)
jj = json.loads(j)
print(jj)