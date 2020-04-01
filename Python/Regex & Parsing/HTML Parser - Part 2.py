import sys
from html.parser import HTMLParser

class Solution(HTMLParser):
  def handle_comment(self, data):
      c = 'Multi' if '\n' in data else 'Single'
      print('>>> {}-line Comment\n{}'.format(c, data.rstrip()))
      
  def handle_data(self, data):
    if len(data) > 2:
      print('>>> Data\n{}'.format(data.rstrip()))

Answer = Solution()
Answer.feed(sys.stdin.read())
