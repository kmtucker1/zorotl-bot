import hikari
import lightbulb

bot = lightbulb.BotApp(
    token='OTg1NzIyMzQwMDk4ODUwODE4.G_osyZ.OQs4mGElFxr52UozO-lMRF2rdw4Ni--9JJWYBg', 
    default_enabled_guilds=(776597904303063050) 
    )

@bot.command
@lightbulb.command('hello', 'says hello!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('hello!')
    

bot.run()