import config as cfg


_login_ = cfg.email['email']
_password_ = cfg.email['key']


keep_going = True

if __name__ == '__main__':
  try:
    while keep_going:
        print 'teest'
        keep_going = False

  except KeyboardInterrupt:
    print 'ERROOORRRRRR'