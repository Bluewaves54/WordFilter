file = open('allWords.txt')
allWords = [word.strip() for word in file]
command, commands = None, list()
while True:
  command = input('>')
  if command == 'finish':
    break
  commands.append(command)
finalcmd = str()
if len(commands) > 0:
  for command in commands:
      finalcmd += (command + ' and ') if command != commands[-1] else command
else:
  finalcmd = 'True'
filteredWords = [word for word in allWords if eval(finalcmd)]
for word in filteredWords:
  print(word)
