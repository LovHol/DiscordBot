import discord
import random

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

# Lägg in dina roll-ID:n här
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
    print(f"The Bot {client.user} Is Online!")

@client.event
async def on_member_join(member):
    # Välj en slumpmässig roll
    role_id = random.choice(RANDOM_ROLES)
    role = member.guild.get_role(role_id)

    # Ge rollen
    await member.add_roles(role)
    print(f"Ga {member.name} rollen {role.name}")

client.run(os.getenv("DISCORD_TOKEN"))
