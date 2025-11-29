import discord
import random
import os

# Intents behövs för att se när nya medlemmar joinar
intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

# Lägg in dina roll-ID:n här (från din server)
RANDOM_ROLES = [
    1444234538313187338,
    1444234627966304377,
    1444234735206400043,
    1444234597792747611,
    1444234837061013567,
    1444234871579873320,
    1444234391210688673,
    1444234938080559114,
    1444234968602775708
]

@client.event
async def on_ready():
    print(f"Botten {client.user} är online!")

@client.event
async def on_member_join(member):
    try:
        # Välj slumpmässig roll
        role_id = random.choice(RANDOM_ROLES)
        role = member.guild.get_role(role_id)
        if role:
            await member.add_roles(role)
            print(f"Ga {member.name} rollen {role.name}")
        else:
            print(f"Role {role_id} hittades inte!")
    except Exception as e:
        print(f"Fel vid on_member_join: {e}")

# Kör boten med token från environment variable
client.run(os.getenv("DISCORD_TOKEN"))
