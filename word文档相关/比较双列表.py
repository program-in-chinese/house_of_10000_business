import docx
from deepdiff import DeepDiff
from pprint import pprint

def 取表格(文件名):
  文件 = docx.Document(文件名)
  首个表 = 文件.tables[0]
  值 = {}
  for 行 in 首个表.rows:
    格 = 行.cells
    值[格[0].text] = 格[1].text
  print(文件名 + " -> " + str(值))
  return 值

表1 = 取表格('双列表1.docx')
表2 = 取表格('双列表2.docx')

pprint(DeepDiff(表1, 表2), indent=2)


