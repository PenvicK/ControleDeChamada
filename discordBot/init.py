from unicodedata import name
from urllib import response
from xmlrpc.client import ResponseError
from django.http import Http404
import requests
import discord
from discord.ext import commands

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f"Estou Pronto! {bot.user}")

@bot.command(name="cargo")
async def get_hole_professor(ctx):
    # author = ctx.author.name + "#" + ctx.author.discriminator
    response = requests.get(f"http://127.0.0.1:8000/usuario/discord/{ctx.author.name}/{ctx.author.discriminator}")
    data = response.json()
    if data[0]['fields']['role'] == "professor":
        role = ctx.guild.get_role(988560275391254528)
        await ctx.author.add_roles(role)
        await ctx.send("Cargo atualizado para Professor!!")
    elif data[0]['fields']['role'] == "aluno":
        role = ctx.guild.get_role(991096275346792529)
        await ctx.author.add_roles(role)
        await ctx.send("Cargo atualizado para Aluno!!")
    else:
        await ctx.send("Aluno não cadastrado!!")

@bot.command(name="presenca")
async def get_hole_professor(ctx):
    author = ctx.author.name + "#" + ctx.author.discriminator
    nmAula = "Projeto integrador - Engenharia de Software - 5° Período"
    body = {"discordID": author, "nmAula": nmAula}
    response = requests.post("http://127.0.0.1:8000/presenca/discord/nova/", json=body)
    data = response.json()
    if not data:
        await ctx.send("Aluno não cadastrado!!")
    else: 
        await ctx.send("Presença concluida!!")

    # if data[0]['fields']['role'] == "professor":
    #     role = ctx.guild.get_role(988560275391254528)
    #     await ctx.author.add_roles(role)
    #     await ctx.send("Cargo atualizado para Professor!!")
    # elif data[0]['fields']['role'] == "aluno":
    #     role = ctx.guild.get_role(991096275346792529)
    #     await ctx.author.add_roles(role)
    #     await ctx.send("Cargo atualizado para Aluno!!")
    # else:
    #     await ctx.send("Aluno não cadastrado!!")

# @bot.command(name="oi")
# async def send_hello(ctx):
#     name = ctx.author.name
#     response = "Olá, " + name
#     await ctx.send(response) 

# @bot.command(name="get")
# async def teste(ctx):
#     try:
#         response = requests.get(f"http://localhost:8080/api/clients/")
#         data = response.json()
#         count = 0
#         for n in data:
#             if count == 0:
#                 name = n.get("name").upper()
#             else:
#                 name += ", " + n.get("name").upper()
#             count = count + 1
           
#         # print(name)
#         if name:
#             print(name)
#             await ctx.send(name)
#         else:
#             await ctx.send("Not found")
#     except Exception as error:
#         await ctx.send("Erro")
#         print(error)

bot.run("OTg4NTE1Njk3NzQ5NTQ5MTg4.GWVjnF.ECJ4BTPgHomyOaM8sFW-Q0jwCUwWYqHy4PtTII")
