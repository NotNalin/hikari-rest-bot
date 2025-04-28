import hikari
import arc
import os
from dotenv import load_dotenv

load_dotenv()

# Create bot instance with public key for verifying interactions
bot = hikari.RESTBot(
    token=os.getenv("DISCORD_TOKEN"),
    public_key=os.getenv("PUBLIC_KEY"),  # Required for interaction verification
)

# Create arc client
client = arc.RESTClient(bot)


@client.include
@arc.slash_command("hi", "Say hi to someone!")
async def hi_slash(
    ctx: arc.RESTContext,
    user: arc.Option[hikari.User, arc.UserParams("The user to say hi to.")],
) -> None:
    await ctx.respond(f"Hey {user.mention}!")


@client.include
@arc.user_command("Say hi to someone!")
async def hi_user(ctx: arc.RESTContext, user: hikari.User) -> None:
    await ctx.respond(f"Hey {user.mention}!")


@client.include
@arc.message_command("Say hi to someone!")
async def hi_message(ctx: arc.RESTContext, message: hikari.Message) -> None:
    await ctx.respond(f"Hey {message.author.mention}!")


@client.include
@arc.slash_command("ping", "Return pong")
async def ping(ctx: arc.RESTContext):
    await ctx.respond("Pong")


@client.include
@arc.slash_command("test", "Test command")
async def test(ctx: arc.RESTContext):
    await ctx.respond("hello world 💿")


@client.include
@arc.slash_command("nigesh")
async def nigesh(ctx: arc.RESTContext):
    await ctx.respond(
        "https://tenor.com/view/suresh-gopi-very-angry-gif-14759864761966067764"
    )


# User Info Command
@client.include
@arc.slash_command("userinfo", "Get information about a user")
async def userinfo(
    ctx: arc.RESTContext,
    user: arc.Option[hikari.User, arc.UserParams("The user to get info about")] = None,
):
    target = user or ctx.author
    await ctx.respond(
        f"**User Info for {target.username}**\n"
        f"🆔 ID: {target.id}\n"
        f"🤖 Bot: {'Yes' if target.is_bot else 'No'}\n"
        f"📅 Created: <t:{int(target.created_at.timestamp())}:R>"
    )


# Server Info Command
@client.include
@arc.slash_command("serverinfo", "Get information about the server")
async def serverinfo(ctx: arc.RESTContext):
    guild = await ctx.fetch_guild()
    await ctx.respond(
        f"**Server Info for {guild.name}**\n"
        f"👥 Members: {guild.approximate_member_count}\n"
        f"📅 Created: <t:{int(guild.created_at.timestamp())}:R>"
    )


# Random Choice Command
@client.include
@arc.slash_command("choose", "Make a random choice")
async def choose(
    ctx: arc.RESTContext,
    options: arc.Option[str, arc.StrParams("Comma-separated choices")],
):
    import random

    choices = [choice.strip() for choice in options.split(",")]
    await ctx.respond(f"I choose: **{random.choice(choices)}**")


# Avatar Command
@client.include
@arc.slash_command("avatar", "Get user's avatar")
async def avatar(
    ctx: arc.RESTContext,
    user: arc.Option[hikari.User, arc.UserParams("The user to get avatar from")] = None,
):
    target = user or ctx.author
    await ctx.respond(f"**{target.username}'s Avatar**\n{target.avatar_url}")


# Local development runner
if __name__ == "__main__":
    bot.run()
