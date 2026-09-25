player.onItemInteracted(WOODEN_AXE, function () {
    if (MODWEwandselectedpos == 1) {
        MODWEwandselectedpos += 1
        if (MODWEwand_enabled) {
            MODWEpos1 = player.position()
            ActionBar("Pos 1 set to " + player.position(), "§5", "@p")
        } else {
            ActionBar("Not Enabled, Enable with \\we 1", "§5", "@p")
        }
    } else if (MODWEwandselectedpos == 2) {
        MODWEwandselectedpos = 1
        if (MODWEwand_enabled) {
            MODWEpos2 = player.position()
            ActionBar("Pos 2 set to " + player.position(), "§5", "@p")
        } else {
            ActionBar("Not Enabled, Enable with \\we 1", "§5", "@p")
        }
    }
})
player.onChat("\\we", function (MODWEcmdwe_arg1) {
    if (MODWEcmdwe_arg1 == 1) {
        player.say("Cmds:")
        player.say("\\we")
        player.say("Show basic WorldEdit cmds")
        player.say("\\\\wand")
        player.say("Summon a wand")
    } else if (MODWEcmdwe_arg1 == 2) {
        MODWEwand_enabled = true
        ActionBar("Wand enabled", "§5", "@p")
    } else if (MODWEcmdwe_arg1 == 2) {
        MODWEwand_enabled = false
        ActionBar("Wand disabled", "§5", "@p")
    } else {
        player.say("Cmds:")
        player.say("\\we help(1)")
        player.say("\\we enable(2)")
        player.say("\\we disable(4)")
        player.say("Ex \"\\we 1\" we would be \\we help")
    }
})
loops.runInBackground(function () {
    MODWEruntime += 1
})
function GetTextArg (cmd: string) {
    MODWEGetTextArgsarray = []
    MODWEGetTextArgsarray = cmd.split(" ")
    return MODWEGetTextArgsarray.pop()
}
events.onPlayerMessage(function (message, sender, receiver, messageType) {
    if (message.includes("\\\\set")) {
        if (MODWEcmdsetworking == false) {
            MODWEcmdsetworking = true
            blocks.fill(
            blocks.blockByName(GetTextArg(message)),
            MODWEpos1,
            MODWEpos2,
            FillOperation.Replace
            )
            MODWEcmdsetworking = false
        }
    }
})
player.onChat("\\\\wand", function () {
    mobs.give(
    mobs.target(NEAREST_PLAYER),
    WOODEN_AXE,
    1
    )
})
function ActionBar (text: string, color: string, people: string) {
    player.execute(
    "title " + people + " actionbar " + color + text
    )
}
let MODWEGetTextArgsarray: string[] = []
let MODWEruntime = 0
let MODWEwand_enabled = false
let MODWEpos2: Position = null
let MODWEpos1: Position = null
let MODWEwandselectedpos = 0
let MODWEcmdsetworking = false
MODWEcmdsetworking = false
MODWEwandselectedpos = 1
MODWEpos1 = world(0, 0, 0)
MODWEpos2 = world(0, 0, 0)
MODWEwand_enabled = true
let MODWEversion = "Beta v1.1.6"
ActionBar("Welcome to WorldEdit", "§5", "@a")
loops.pause(200)
ActionBar("You are on version " + MODWEversion, "§5", "@a")
