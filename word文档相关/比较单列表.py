import docx
from deepdiff import DeepDiff

def 取表格(文件名):
  文件 = docx.Document(文件名)
  首个表 = 文件.tables[0]
  值 = []
  for 行 in 首个表.rows:
    for 格 in 行.cells:
      值.append(格.text)
  print(文件名 + " -> " + str(值))
  return 值

表1 = 取表格('单列表1.docx')
表2 = 取表格('单列表2.docx')

print(DeepDiff(表1, 表2))


