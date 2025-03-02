import minecraft_launcher_lib as mc
import os
from distutils.dir_util import copy_tree

# create temporary directory for file comparison / transfer
# temp_dir = os.path.join("shared", ".temp")
# os.system("mkdir {}".format(temp_dir))

# get local minecraft directory path
mc_dir = mc.utils.get_minecraft_directory()

def update_saves():
  saves_dir = os.path.join(mc_dir, "saves")
  saves = [save.name for save in os.scandir(saves_dir) if save.is_dir()]

  print(saves)

  sth = input("Choose save: ")

  print(sth)

def show_files(file_type, server):
  print(file_type, server)

def update_files(file_type):
  # update_saves()
  print(file_type)

def upload_files(file_type):
  print(file_type)

def start():
  command_input = input()

  command_params = command_input.split()

  match command_params[0]:
    case "show":
      if len(command_params) != 3:
        print("Incorrect number of parameters. Type 'help' for a list of the available commands.")
        start()
      else:
        show_files(command_params[1], command_params[2])
    case "update":
      if len(command_params) != 2:
        print("Incorrect number of parameters. Type 'help' for a list of the available commands.")
        start()
      else:
        update_files(command_params[1])
    case "upload":
      if len(command_params) != 2:
        print("Incorrect number of parameters. Type 'help' for a list of the available commands.")
        start()
      else:
        upload_files(command_params[1])
    case "help":
      print("""
        1. show <saves/mods> <local/remote> - displays a list of the requested files

        2. update <saves/mods/all> - updates the requested files with the remote versions

        3. upload <saves/mods/all> - uploads the requested files to the remote server     
      """)
      start()
    case _:
      print("Unknown command. Type 'help' for a list of the available commands.")
      start()

def main():
  print("Update your local Minecraft files.")
  print("What would you like to update?")

  start()

if __name__=="__main__":
    main()