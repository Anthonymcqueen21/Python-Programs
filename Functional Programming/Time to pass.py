def greet_users(names):
"""Time to print a simple greet from monster island"""
for name in names
   msg = "Hey there, " + name.title() + "!"
   print(msg)
   
usernames = ['Godzilla', 'ty', 'King of the monsters']
greet_users(usernames)
