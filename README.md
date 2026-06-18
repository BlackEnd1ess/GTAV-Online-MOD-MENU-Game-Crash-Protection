# GTAV-Online-MOD-MENU-Game-Crash-Protection

# V2.0 -> (18.06.2026) UPDATE!
# by enable RELAY_ONLY you can probaly hide you IP behind Rockstars relay-servers and force NAT type to STRICT.
# This means that peering between you and the player is prevented, and all data traffic is routed via a relay.
# This makes it more difficult for the modder/cheater to route spoofed or faked logout/crash packets through the players.
# A disadvantage is that this could lead to increased latency and possibly longer loading times.

---------------------------------------------------------------------------
How this project came about: 
For quite some time, a large number of players have noticed a massive increase in game crashes, session kicks, and unexpected teleports.
This is simply because the game uses a P2P connection, which opens up the possibility for *anyone* to manipulate data packets at the game level.
Through an analysis spanning at least several weeks, I determined that all game crashes, session kicks, or unexpected BattlEye kicks were triggered in an unnatural manner.
Furthermore, it is very easy for the user of this type of mod menu to track down IP addresses, Rockstar IDs, and associated accounts.
This makes it very easy for the modder to stalk a player and harass them for days or even weeks or months. 
Since these incidents have increased dramatically, I have started looking for a way to build up at least some immunity against these game crashes. Unfortunately, using a VPN does not help those affected, the packets sent by the mod menu usually go directly to the player or are routed via the relay. 
Protecting oneself 100% against this would therefore also require significant interventions on the part of the game operators.
It is important to inform as many players as possible about this and to offer them the opportunity to take action against this type of oppression.
---------------------------------------------------------------------------

This application was explicitly designed to intercept the outgoing packets in GTA V Online that trigger the game-crash exploit currently being abused by cheaters and modders.
This script was created with the help of ChatGPT, thanks to a truly professional AI that sped up the process significantly.

To run, this script requires the following additional components: python3, WinDivert, and npcap.

1. download and install https://github.com/basil00/WinDivert/releases the latest WinDivert.
2. Make sure the following files are located in the apllication python folder or in the same folder as the script: WinDivert.dll, WinDivert64.dll, WinDivert.sys, WinDivert64.sys.
3. install pydivert: pip install pydivert

You could potentially create a batch file for this that you can run as an administrator, since this tool requires admin rights to access your network interface.
This tool/analysis tool has no impact on BattlEye or anti-cheat systems in general and can therefore be used without concern.

Potential downsides: activating the blocking feature might cause you to block legitimate traffic (though the likelihood of this is low). This could result in you ending up in a sparsely populated or completely empty session, but the modder will no longer be able to terminate your game.

This script is in the beta phase and will undergo further development over time. If connection problems occur after it has been running for an extended period, ensure that the process is terminated via the Task Manager; everything should then function normally again.

Unfortunately, cheaters/modders can still boot you into empty lobbies or kick you out of the session. I am already working on putting a stop to that as well.

This script does not modify GTA V files and only filters selected network packets locally. However, incorrect filtering may still cause connection issues or empty sessions.

Best regards, BlackEndless :)
