import discord
import json

client = discord.Client()
output_filename = "mutuals.json"

def filter_mutuals(users: dict) -> dict:
    return {m:users[m] for m in users if len(users[m]) > 1}

def build_json_object(mutual_users: dict) -> dict:
    return {
        "users_total":len(mutual_users),
        "users":[
            {
                "name":m,
                "guilds_total":len(mutual_users[m]),
                "guilds":sorted(mutual_users[m])
            } for m in sorted(mutual_users)
        ]
    }

@client.event
async def on_ready():
    print("ready")
    users = dict()
    guilds = await client.fetch_guilds(limit=None).flatten()

    for i, g in enumerate(guilds):
        print(f"{i+1}/{len(guilds)} {g}")
        g = client.get_guild(g.id)
        for m in g.members:
            name = f"{m.name}#{m.discriminator}"
            if name in users:
                users[name].add(g.name)
            else:
                users[name] = {g.name}
        print(f"|____ {len(g.members)} users")
    print()

    mutual_users = filter_mutuals(users)
    json_s = json.dumps(build_json_object(mutual_users))
    with open(output_filename, "w", encoding="utf-8") as fptr:
        fptr.write(json_s)

    print(f"Found {len(mutual_users)} mutual users")
    print(f"Results written to {output_filename}")
    await client.close()


with open("token.txt", "r") as fptr:
    token = fptr.read().strip()

client.run(token, bot=False)
