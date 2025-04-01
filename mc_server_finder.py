##########   Import Libraries
import random
from threading import Thread
from mcstatus import JavaServer
from termcolor import colored
import datetime

##########   EDITABLE VARIABLES
wanted_versions = ['1.21.4','Spigot 1.21.4','Paper 1.21.4']    # For categorization colours
threads = 10000                                                # How many threads are open for searching
port = 25565                                                   # Server Port. Usually 25565
trials = 1000                                                   # How many IPs are going to be tested by each thread.

##########   Variables
ip = [0,0,0,0]                                                 # The IPv4 is comprised of 4 numbers from 0 to 255.

##########   Categorize Server
def categorize(version, online_players):
   if version in wanted_versions and online_players > 0:
      color = 'green'
   elif version in wanted_versions and online_players == 0:
      color = 'yellow'
   elif version not in wanted_versions and online_players > 0:
      color = 'blue'
   else:
      color = 'red'
   return color

##########   Connection function
def connect():

   # Repeat for trials times
   for i in range(trials):

      # Generate IP. name is just the ip, and ip_name has the port attached.
      name = ""
      for j in ip:
         j = random.randint(0, 255)
         name += str(j) + "."
      name = name[:-1]
      ip_name = name+":"+str(port)

      # Check if IP is a minecraft server
      tell = True
      try:
         server = JavaServer.lookup(ip_name)
         status = server.status()
         online_players = status.players.online
         version = status.version.name
      except:
         tell = False
      
      # Categorize and Display Minecraft Server
      if tell:
         color = categorize(version, online_players)
         print(colored("[*]   Time: "+ datetime.datetime.now().strftime("%H:%M:%S") +"   ||   IP: " + ip_name + " " * (25-len(ip_name)) + "Players Online: "+ str(online_players) + \
            " " * (7-len(str(online_players))) + "Version: " + str(version) , color))


##########   Start Program - Information
print(colored("\nInformation:\n", 'white', attrs=['bold']))
print(colored('[*]  Green: Wanted Version and has online players', 'green'))
print(colored('[*]  Yellow: Wanted Version and has NO online players', 'yellow'))
print(colored('[*]  Blue: Unwanted Version and has online players', 'blue'))
print(colored('[*]  Red: Unwanted Version and has NO online players', 'red'),'\n')
print(colored("Starting search with "+str(threads)+" open threads and " + str(trials) + " trials per thread, for a total of " + str(threads*trials) + " IP checks:\n", 'white', attrs=['bold']))


##########   Run Threads
for i in range(threads):
   Thread(target = connect).start()