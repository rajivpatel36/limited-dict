from distutils.core import setup
setup(
  name = 'limited_dict',
  packages = ['limited_dict'], # this must be the same as the name above
  version = '0.1',
  description = 'A dictionary-like object which only stores the highest or lowest N values',
  author = 'Rajiv Patel',
  author_email = 'rajivpatel36@gmail.com',
  url = 'https://github.com/rajivpatel36/limited-dict', # use the URL to the github repo
  download_url = 'https://github.com/rajivpatel36/limited-dict/tarball/0.1', # I'll explain this in a second
  keywords = ['dict', 'limited', 'sorted', 'sorteddict'], # arbitrary keywords
  classifiers = [],
)
