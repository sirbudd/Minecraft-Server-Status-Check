from mcstatus import MinecraftServer

server = MinecraftServer.lookup("157.90.221.188:6055")
status = server.status()
print(f"The server has {status.players.online} players and replied in {status.latency} ms")
