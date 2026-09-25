def on_item_interacted_wooden_axe():
    global MODWEwandselectedpos, MODWEpos1, MODWEpos2
    if MODWEwandselectedpos == 1:
        MODWEwandselectedpos += 1
        if MODWEwand_enabled:
            MODWEpos1 = player.position()
            ActionBar("Pos 1 set to " + str(player.position()), "§5", "@p")
        else:
            ActionBar("Not Enabled, Enable with \\we 1", "§5", "@p")
    elif MODWEwandselectedpos == 2:
        MODWEwandselectedpos = 1
        if MODWEwand_enabled:
            MODWEpos2 = player.position()
            ActionBar("Pos 2 set to " + str(player.position()), "§5", "@p")
        else:
            ActionBar("Not Enabled, Enable with \\we 1", "§5", "@p")
player.on_item_interacted(WOODEN_AXE, on_item_interacted_wooden_axe)

def on_on_chat(MODWEcmdwe_arg1):
    global MODWEwand_enabled
    if MODWEcmdwe_arg1 == 1:
        player.say("Cmds:")
        player.say("\\we")
        player.say("Show basic WorldEdit cmds")
        player.say("\\\\wand")
        player.say("Summon a wand")
    elif MODWEcmdwe_arg1 == 2:
        MODWEwand_enabled = True
        ActionBar("Wand enabled", "§5", "@p")
    elif MODWEcmdwe_arg1 == 2:
        MODWEwand_enabled = False
        ActionBar("Wand disabled", "§5", "@p")
    else:
        player.say("Cmds:")
        player.say("\\we help(1)")
        player.say("\\we enable(2)")
        player.say("\\we disable(4)")
        player.say("Ex \"\\we 1\" we would be \\we help")
player.on_chat("\\we", on_on_chat)

def on_run_in_background():
    global MODWEruntime
    MODWEruntime += 1
loops.run_in_background(on_run_in_background)

def GetTextArg(cmd: str):
    global MODWEGetTextArgsarray
    MODWEGetTextArgsarray = []
    MODWEGetTextArgsarray = cmd.split(" ")
    return "0"

def on_player_message(message, sender, receiver, messageType):
    global MODWEcmdsetworking
    if message.includes("\\\\set"):
        if MODWEcmdsetworking == False:
            MODWEcmdsetworking = True
            blocks.fill(blocks.block_by_name(GetTextArg(message)),
                MODWEpos1,
                MODWEpos2,
                FillOperation.REPLACE)
            MODWEcmdsetworking = False
events.on_player_message(on_player_message)

def on_on_chat2():
    mobs.give(mobs.target(NEAREST_PLAYER), WOODEN_AXE, 1)
player.on_chat("\\\\wand", on_on_chat2)

def ActionBar(text: str, color: str, people: str):
    player.execute("title " + people + " actionbar " + color + text)
MODWEGetTextArgsarray: List[str] = []
MODWEwand_enabled = False
MODWEpos2: Position = None
MODWEpos1: Position = None
MODWEwandselectedpos = 0
MODWEcmdsetworking = False
MODWEcmdsetworking = False
MODWEruntime = 0
MODWEwandselectedpos = 1
MODWEpos1 = world(0, 0, 0)
MODWEpos2 = world(0, 0, 0)
MODWEwand_enabled = True
MODWEversion = "Beta v1.1.6"
ActionBar("Welcome to WorldEdit", "§5", "@a")
loops.pause(200)
ActionBar("You are on version " + MODWEversion, "§5", "@a")
