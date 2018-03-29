
import collections

#DIFFERENT USEFULL INFOS
TOKEN = 'xd'
PREFIX = '^^'
BOTID = 421755194972569600
OWNERID = 304530498112192513
WHITELIST = ['304530498112192513', "id's"] #todo something
TRACKER_KEY =  "ptdr"


#COLOR OF EMBEDS
COLOR = 0x28ff64
COLOR_E = 0xff2e00

#COGS:
initial_commands = {
    "help" : (
        "cogs.general.help", "Type ^^help <command> to get more info in a specific command"),
    "ping" : (
        "cogs.general.ping", "Test the latency of the Bot"),
    "poke" : (
        "cogs.general.poke", "To poke somebody ! *args : <user id>*"),
    "fortnite" : (
        "cogs.games.fortnite", "Get Fortnite stats, *args : <mode> <username> <platform>*"),
    "clear" : (
        "cogs.admin.clear", "Purge a channel, *args : <number of message>*"),
    "reload" : (
        "cogs.owner.reload", "Reload a module = update a command, *args : <command name>*"),
    "shutdown" : (
        "cogs.owner.shutdown", "Shutdown the Bot")
}

initial_name = []
initial_extension = []

initial_folder_general = collections.OrderedDict()
initial_folder_games = collections.OrderedDict()
initial_folder_admin = collections.OrderedDict()

for name in initial_commands:
    initial_name.append(name)
    initial_extension.append(initial_commands[name][0])

    folder = (initial_commands[name][0]).split('.')[1]
    description = initial_commands[name][1]
    if folder == 'general':
        initial_folder_general[name] = description
    elif folder == 'games':
        initial_folder_games[name] = description
    elif folder == 'admin':
        initial_folder_admin[name] = description
    else:
        continue

    value_general = value_games = value_admin = str()
    for k, v in initial_folder_general.items():
        value_general += '**' + k + '**' + ' - ' + v + '\n'
    for k, v in initial_folder_games.items():
        value_games += '**' + k + '**' + ' - ' + v + '\n'
    for k, v in initial_folder_admin.items():
        value_admin += '**' + k + '**' + ' - ' + v + '\n'
