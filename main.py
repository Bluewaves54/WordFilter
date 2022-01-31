file = open('allWords.txt')

allWords = list()
for word in file:
  allWords.append(word.strip())

filteredWords = list()

command = None
commands = list()
while command != 'finish':
  command = input('>')
  commands.append(command)

finalcmd = str()
for command in commands:
  finalcmd += command
  try:
    if command == commands[-2]:
      break
    else:
      finalcmd += ' and '
  except IndexError:
    finalcmd = 'True'

for word in allWords:
  if eval(finalcmd):
    filteredWords.append(word)
  else:
    continue

for word in filteredWords:
  print(word)
