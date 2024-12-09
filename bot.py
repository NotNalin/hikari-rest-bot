import hikari
import arc
import os

# Create an instance of a RESTBot
# Paste your token from the dev portal in here
bot = hikari.RESTBot(os.environ["TEST_TOKEN"])

# Pass it to arc
client = arc.RESTClient(bot)


@client.include # Add it to the client
@arc.slash_command("hi", "Say hi to someone!") # Define a new command
async def hi_slash(
    ctx: arc.RESTContext,
    # Add a new slash option that asks for a user
    user: arc.Option[hikari.User, arc.UserParams("The user to say hi to.")]
) -> None:
    await ctx.respond(f"Hey {user.mention}!")

@client.include
@arc.slash_command("ping", "Return pong")
async def ping(ctx: arc.RESTContext):
    await ctx.respond("Pong")

@client.include
@arc.slash_command("test", "Test command")
async def test(ctx: arc.RESTContext):
    await ctx.respond("hello world 💿")

# This should be the last line, no code will be run after this
bot.run()