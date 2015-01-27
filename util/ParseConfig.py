import ConfigParser
import sys

class ParseConfig():

  def __init__(self, config_file):
    self.config_dict = dict()
    self.config_file = config_file
    self.config = ConfigParser.RawConfigParser(allow_no_value=True)
    self.__read_config()

  def __read_config(self):
    try:
      self.config.read(self.config_file)
    except IOError:
      print >>sys.stderr, 'ERROR: can\'t find config file: ' + self.config_file
      sys.exit()


  def get_dict(self):
    for key in self.config.sections():
      print "[%s]" % key
      for opt, val in self.config.items(key):
        print >>sys.stderr, opt + ' = ' + val
        self.config_dict[opt] = val
    return self.config_dict
        

  #def get_dict(self):
  #  return self.config_dict


def main():

  pc = ParseConfig(sys.argv[1])
  d = pc.get_dict()
  for t in d:
    print t + ' - ' + d[t]


if __name__ == '__main__':
  main()
