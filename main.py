import os
import time
import random
import discord
from discord.ext import commands
from colorama import Fore, init

init(autoreset=True)

TOKEN = ""
bot = None

def start_bot(token):
    global bot, TOKEN
    TOKEN = token
    bot = commands.Bot(command_prefix=".", self_bot=True)

    @bot.event
    async def on_ready():
        print(f"\nLogged {bot.user.name}\n")
        time.sleep(1)

    @bot.command()
    async def pfp(ctx, user: discord.User):
        try:
            await ctx.send(user.avatar.url)
            await ctx.message.delete()
        except Exception as e:
            print(f"Error: {e}")

    @bot.command()
    async def gay(ctx, user: discord.User):
        try:
            result = random.choice(["Yes", "No"])
            response = f"Yes, {user.name} is gay." if result == "Yes" else f"No, {user.name} is not gay."
            await ctx.send(response)
            await ctx.message.delete()
        except Exception as e:
            print(f"Error: {e}")

    @bot.command()
    async def math(ctx, *, equation: str):
        try:
            result = eval(equation)
            await ctx.send(f"The answer to {equation} is {result}")
            await ctx.message.delete()
        except Exception as e:
            print(f"Error: {e}")

    @bot.command()
    async def spam(ctx, count: int, *, text: str):
        try:
            if 1 <= count <= 500:
                for _ in range(count):
                    await ctx.send(text)
            else:
                await ctx.send("Count must be between 1 and 500.")
            await ctx.message.delete()
        except Exception as e:
            print(f"Error: {e}")

    @bot.command()
    async def ask(ctx, *, prompt: str):
        try:
            answer = ask_huggingface(prompt)
            await ctx.send(answer)
            await ctx.message.delete()
        except Exception as e:
            print(f"Error: {e}")

    @bot.command()
    async def help(ctx):
        help_text = (
            ".pfp - Sends the profile picture of the mentioned user\n"
            ".gay - Determines if the user is gay or not\n"
            ".math - Solves a math equation\n"
            ".spam - Spams a message a specified number of times\n"
            ".ask - Ask a question using Huggingface's Qwen model"
        )
        await ctx.send(help_text)
        await ctx.message.delete()

    bot.run(TOKEN)


def ask_huggingface(prompt):
    import requests
    HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-Coder-32B-Instruct"
    HUGGINGFACE_API_KEY = "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"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    try:
        response = requests.post(HUGGINGFACE_API_URL, headers=headers, json={"inputs": prompt})
        response.raise_for_status()
        output = response.json()
        return output[0]['generated_text']
    except Exception as e:
        return f"Error: {e}"


def print_green(text):
    print(f"{Fore.LIGHTGREEN_EX}{text}")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def start_ui():
    clear_screen()

    print(F"{Fore.LIGHTGREEN_EX}███████╗██████╗ ███████╗███████╗")
    time.sleep(0.1)
    print(F"{Fore.GREEN}██╔════╝██╔══██╗██╔════╝██╔════╝")
    time.sleep(0.1)
    print(F"{Fore.LIGHTGREEN_EX}█████╗  ██████╔╝███████╗█████╗  ")
    time.sleep(0.1)
    print(F"{Fore.GREEN}██╔══╝  ██╔═══╝ ╚════██║██╔══╝  ")
    time.sleep(0.1)
    print(F"{Fore.LIGHTGREEN_EX}██║     ██║     ███████║███████╗")
    time.sleep(0.1)
    print(F"{Fore.GREEN}╚═╝     ╚═╝     ╚══════╝╚══════╝")
    time.sleep(0.1)
    print(F"{Fore.LIGHTGREEN_EX}FREE BOT!")
    print("\n" + "=" * 60)
    print(F"{Fore.GREEN}Select an option:")
    print(F"{Fore.GREEN}[1] Discord Token Selfbot")
    print("=" * 60)

    option = input("Select an option : ").strip()
    if option == "1":
        token = input("\nEnter your Discord Token: ").strip()
        print_green("\nStarting the bot...")
        time.sleep(2)
        start_bot(token)
    else:
        print("\nInvalid option. Exiting...\n")
        time.sleep(1)


start_ui()
