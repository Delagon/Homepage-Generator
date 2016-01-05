ns = "&#160;"
#ns = ''

def run():
  states = ['GEN', 'CATS']
  data = {}
  model = {
        'bg':'#2E3436',
        'tx':'#FFFFFF',
        'ms':'Welcome Back',
        'lr':'justify',
        'js':'True',
        'br':',',
          }
  cats = []
  longstart = 0
  lens = []
  try:
    f = file('data.txt')
  except:
    data = None
  if data != None:
    l =  f.readline();
    state = "GEN"
    while l != '':
      l = l[:-1]
      if l in states:
        state = l
        print states
      else:
        if state == 'GEN':
          data[l.split('=')[0]] = l.split('=')[1]
          print l 
        else:
          if len(l.split(':')[0]) > longstart:
            longstart = len(l.split(':')[0])
          cats += [[l.split(':')[0], l.split(':')[1].split(';')]]
          tempLen = 0
          for u in l.split(';'):
            tempLen += len(u.split(' , ')[0])
          lens += [tempLen]
          print l
      l = f.readline()
    else:
      data = model
    for k in model.keys():
      if data.get(k) == None:
        data[k] = model[k]
    f.close()
    longest = max(lens)
    for i in data.keys():
      print i, data[i]
    print "Data Loaded, making css"
    s = "<!DOCTYPE html>\n"
    s += "<html>\n"
    s += "<style>\n"
    s += "body { \n"
    s += "  background-color: " + data['bg'] + ";\n"
    s += "  color: " + data['tx'] + ";\n"
    s += "  link : #000000;\n"
    s += "  text-align: " + data['lr'] + ";\n"
    s += "  font-family: courier;\n"
    s += "}\n"
    s += "a:link {\n  color: " + data['tx'] + ";\n"
    s +="  text-decoration: none;\n}\n"
    s += "a:visited {\n  color: " + data['tx'] + ";\n"
    s +="  text-decoration: none;\n}\n"
    s += "a:hover {\n  color: " + data['tx'] + ";\n"
    s +="  text-decoration: none;\n}\n"
    s += "a:active {\n  color: " + data['tx'] + ";\n"
    s +="  text-decoration: none;\n}\n"
    s += "</style>\n</head>\n<body>\n" + data['ms'] + ""*(longstart + longest - len(data['ms'])) + "\n<br>\n"
    pointer = 0;
    for c in cats:
      s += c[0] + ns*(longstart - len(c[0]))+ " : "
      for i in c[1]:
        print i
        s += "<a href=\"http://"+ i.split(" , ")[1] + "\">" + i.split(" , ")[0] + "</a> " + data['br']
      s = s[:-len(data['br'])] + ""*(longest - lens[pointer]) + "\n<br>\n"
      pointer += 1
    s += "</body>\n</html>"
    f = file("index.html",'w')
    f.write(s)
    f.close()

if __name__ == '__main__':
  run()
