import discord
import json
import sys

client = discord.Client()
output_filename = "mutuals.json"

def build_users(guilds: list) -> dict:
    users = dict()
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
    return users

def filter_mutuals(users: dict) -> dict:
    mutuals = {m:users[m] for m in users if len(users[m]) > 1}
    if len(sys.argv) > 1:
        query_guilds = [g.strip() for g in " ".join(sys.argv[1:]).split(";")]
        mutuals = {m:users[m] for m in mutuals if all([g in users[m] for g in query_guilds])}
    return mutuals

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

    guilds = await client.fetch_guilds(limit=None).flatten()
    users = build_users(guilds)
    mutual_users = filter_mutuals(users)
    json_s = json.dumps(build_json_object(mutual_users))

    with open(output_filename, "w", encoding="utf-8") as fptr:
        fptr.write(json_s)

    print(f"Found {len(mutual_users)} mutual users")
    print(f"Results written to {output_filename}")
    await client.close()


with open("token.txt", "r") as fptr:
    token = fptr.read().strip().replace('"', "")

client.run(token, bot=False)
