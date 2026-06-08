# GTAV-Online-MOD-MENU-Game-Crash-Protection
This application was explicitly designed to intercept the outgoing packets in GTA V Online that trigger the game-crash exploit currently being abused by cheaters and modders.

To run, this script requires the following additional components: python3, WinDivert, and npcap.

1. download and install https://github.com/basil00/WinDivert/releases the latest WinDivert.
2. Make sure the following files are located in the apllication python folder or in the same folder as the script: WinDivert.dll, WinDivert64.dll, WinDivert.sys, WinDivert64.sys.
3. install pydivert: pip install pydivert

You could potentially create a batch file for this that you can run as an administrator, since this tool requires admin rights to access your network interface.
This tool/analysis tool has no impact on BattlEye or anti-cheat systems in general and can therefore be used without concern.

Potential downsides: activating the blocking feature might cause you to block legitimate traffic (though the likelihood of this is low). This could result in you ending up in a sparsely populated or completely empty session, but the modder will no longer be able to terminate your game.

This script is in the beta phase and will undergo further development over time. If connection problems occur after it has been running for an extended period, ensure that the process is terminated via the Task Manager; everything should then function normally again.

Unfortunately, cheaters/modders can still boot you into empty lobbies or kick you out of the session. I am already working on putting a stop to that as well.

This script is clean. there are no risks for you.

Best regards, BlackEndless :)
