import discord
from utils import random_groups, random_names
from datetime import datetime
import os

TOKEN = os.environ["discord_token"]

colors = ("Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Purple",
          "Pink", "White", "Black")
animals = ("Lobster", "Cat", "Duck", "Lizard", "Fish", "Bird", "Octopus",
           "Axolotl", "Fox", "Rooster")

class Client(discord.Client):
    def get_members(self):
        membs = []
        for guild in self.guilds:
            for member in guild.members:
                membs.append(str(member))
        return membs

    async def on_ready(self):
        print('si', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        user_message = str(message.content)
        print(user_message)
        "\c COMANDO ARGUMENTO"
        "\c COMANDO"
        "Python Funcion que parte una oracion en un caracter y te devuelve la lista de particiones"
        "\c COMANDO ARGUMENTO [\c, COMANDO, ARGUMENTO]"
        if user_message[:3] == "\c ":
            command = user_message[3:]
            if command == "classmates":
                await message.channel.send(self.get_members())
            #elif command == "random_groups":
            #await message.channel.send(random_groups(self.get_members(), 5))
            #elif command == "random_names":
            #await message.channel.send(random_names(random_groups(self.get_members(), 4)))
            else:
                await message.channel.send("No reconocí este comando.")


intents = discord.Intents.default()
intents.members = True
client = Client(intents=intents)
client.run(TOKEN)

print(datetime.now())
"""
Use cases (Heysen):

- Recordatorio de exámenes o tareas próximas.
    Pasarle parametro al bot de cuando y que
    Como el bot sabe la hora
- Poner alarma de ping en algún momento.
    Como el bot sabe la hora
    Spam
- Que cada uno pueda poner su horario y que otros puedan ver el de los demás.
    - user X, coger calendario de X (google calendar) y ver si esta libre esta tarde.
- Llevar un puntaje de cada miembro en base a su compromiso en trabajos en grupo (por ejemplo, si hay alguna coevaluación grupal)
    - coevaluaciones
- Leer texto en voz alta.
    - revisar esto.
"""
"""
VSCode
Terminal
Git
Heroku
"""
