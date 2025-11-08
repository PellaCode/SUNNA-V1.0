import redis

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

def push_command(cmd: str, chat_id: int, arg: str = None):
    data = f"{cmd}|{chat_id}|{arg or ''}"
    r.lpush("sunna_commands", data)

def pop_command():
    data = r.rpop("sunna_commands")
    if data:
        parts = data.split("|", 2)
        cmd, chat_id, arg = parts[0], int(parts[1]), parts[2]
        return cmd, chat_id, arg
    return None
