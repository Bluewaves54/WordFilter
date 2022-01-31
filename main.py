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
    finalcmd += (command + ' and ')
else:
  finalcmd = 'True'
filteredWords = [word for word in allWords if eval(finalcmd)]
print(word for word in filteredWords)
