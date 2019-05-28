import unittest
from app.moodels import News

class NewsTest(unittest.TestCase):
  '''
  Test Class to test the behaviour of the News Class
  '''

  def setUp(self):
    '''
    Set up method that will run before every test
    '''
    self.new_news = News('name', 'author', 'title', 'description', 'url','publishedAt','content')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_news, News))