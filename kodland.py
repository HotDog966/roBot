import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

atık_süreleri = {
    "plastik": "450 yıl",
    "cam şişe": "1 milyon yıl",
    "kağıt": "2-5 ay",
    "metal kutu": "200-500 yıl",
    "sigara izmariti": "1-5 yıl",
    "naylon poşet": "10-20 yıl",
    "karton": "3-6 ay",
    "alüminyum": "200-500 yıl",
    "muz kabuğu": "2-5 hafta"
}



@bot.event
async def on_ready():
    print(f'{bot.user} botu giriş yaptı!')

# Atık süresi sorgulama komutu
@bot.command(name='atık', help='Atığın doğada ne kadar süre kaldığını öğren.')
async def atik(ctx, *, atik_turu: str):
    atik_turu = atik_turu.lower()  # Girilen atık türünü küçük harfe çeviriyoruz
    if atik_turu in atık_süreleri:
        await ctx.send(f"{atik_turu.capitalize()} doğada {atık_süreleri[atik_turu]} kalır.")
    else:
        await ctx.send(f"Üzgünüm, {atik_turu} için bilgi bulamadım.")

bot.run('MTI4Mzg2NzM3NTMzODI1ODQ5Ng.Go6PDa.WcpycNJH8HRDXDLDDbWBzHq4zOE5vjeSQIpG0o')
