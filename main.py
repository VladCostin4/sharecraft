import minecraft_launcher_lib as mc
import subprocess

mc_dir = mc.utils.get_minecraft_directory()
all_versions_info = mc.utils.get_available_versions(mc_dir)

versions_list = []
available_versions_list = []
