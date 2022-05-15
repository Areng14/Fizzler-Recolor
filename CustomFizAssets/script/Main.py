from base64 import decode
from codecs import encode
from errno import EDEADLK
from tracemalloc import stop
import vpk
import glob
import os
import shutil
import random
import time
#Imports shit

var1 = input("Is the .exe and assets in the portal 2 directory? (yes/no): ")
if var1 == "yes":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    dlcfolderint = int(input("What is your highest dlc folder? (interger) "))
    Color = input("RGB Color code (r for random): ")
    if Color == "r":
        Random1 = random.randint(0,255)
        Random2 = random.randint(0,255)
        Random3 = random.randint(0,255)
        Color = str(Random1) + " " + str(Random2) + " " + str(Random3)
    dlcfolderint += 1
    dlcfolder = "portal2_dlc" + str(dlcfolderint)
    
    content = ""
    def editfiles(FileName):
        Directory = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/" + dlcfolder + "/pak01_dir/materials/effects/"
        FileName2 = Directory + FileName + ".vmt"
        Fizzler = open(FileName2,'w')
        Fizzler.write('SolidEnergy\n')
        Fizzler.write('{\n')
        Fizzler.write('$basetexture "effects/fizzler_ripples_dim"\n')
        Fizzler.write('$flowmap "effects/fizzler_flow"\n')
        Fizzler.write('$flowbounds "effects/fizzler_bounds_center"\n')
        Fizzler.write('$FLOW_NOISE_TEXTURE "effects/fizzler_noise"\n')
        Fizzler.write('$FLOW_UVSCROLLDISTANCE "0.25"\n')
        Fizzler.write('$FLOW_TIMEINTERVALINSECONDS "1.2"\n')
        Fizzler.write('$FLOW_NOISE_SCALE 0.003\n')
        Fizzler.write('$FLOW_LERPEXP 1.5\n')
        Fizzler.write('$FLOW_WORLDUVSCALE 0.008\n')
        Fizzler.write('$FLOW_NORMALUVSCALE 0.008\n')
        Fizzler.write('$FLOW_COLOR "{' + Color + '}"\n')
        Fizzler.write('$FLOW_VORTEX_COLOR "{' + Color + '}"\n')
        Fizzler.write('$surfaceprop glass\n')
        Fizzler.write('"%keywords" Portal2\n')
        Fizzler.write('$translucent 1\n')
        Fizzler.write('$additive 1\n')
        Fizzler.write('$FLOW_VORTEX_POS1 "[-160 64 64]"\n')
        Fizzler.write('$FLOW_VORTEX_SIZE 35\n')
        Fizzler.write('"360?$outputintensity" 2.8\n')
        Fizzler.write('"SonyPS3?$outputintensity" .7\n')
        Fizzler.write(' \n')
        Fizzler.write('"srgb_pc?$outputintensity" 2.3\n')
        Fizzler.write('"!srgb_pc?$outputintensity" 1.7\n')
        Fizzler.write('Proxies\n')
        Fizzler.write('{\n')
        Fizzler.write('FizzlerVortex\n')
        Fizzler.write('{\n')
        Fizzler.write('}\n')
        Fizzler.write('}\n')
        Fizzler.write('}\n')
        Fizzler.close
    def MakeFolders():
        path1 = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/" + dlcfolder
        path2 = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/" + dlcfolder + "/pak01_dir"
        path3 = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/" + dlcfolder + "/pak01_dir/materials"
        path4 = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/" + dlcfolder + "/pak01_dir/materials/effects"
        os.mkdir(path1)
        os.mkdir(path2)
        os.mkdir(path3)
        os.mkdir(path4)
        print ("Made folders in " + path1)
    def MoveAssets():
        source_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/CustomFizAssets/effects/"
        destination_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/" + dlcfolder + "/pak01_dir/materials/effects/"
        files_to_move = ['fizzler_bounds.vtf', 'fizzler_bounds.vtf','fizzler_bounds_l.vtf','fizzler_bounds_r.vtf','fizzler_edges.vmt','fizzler_flow.vtf','fizzler_noise.vtf','fizzler_ripples.vtf','fizzler_ripples_dim.vtf','fizzler_underground_bounds.vtf','fizzler_underground_elevator_bounds.vtf','fizzler_underground_flow.vtf','fizzler_underground_noise.vtf','fizzler_underground_ripples.vtf','fizzler_underground_ripples2.vtf','fizzler_underground_wide_center_bounds.vtf','fizzler_underground_wide_side_l_bounds.vtf','fizzler_underground_wide_side_r_bounds.vtf']
        for file in files_to_move:
            source = source_folder + file
            destination = destination_folder + file
            shutil.copyfile(source, destination)
            print('Copied', file, "to", destination_folder)
        source_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/CustomFizAssets/vmt/"
        destination_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/" + dlcfolder + "/pak01_dir/materials/effects/"
        files_to_move = ['fizzler.vmt','fizzler_center.vmt','fizzler_l.vmt','fizzler_r.vmt','fizzler_underground.vmt','fizzler_underground_elevator.vmt','fizzler_underground_side_emitters.vmt','fizzler_underground_wide_center.vmt','fizzler_underground_wide_side_l.vmt','fizzler_underground_wide_side_r.vmt']
        for file in files_to_move:
            source = source_folder + file
            destination = destination_folder + file
            shutil.copyfile(source, destination)
            print('Copied', file, "to", destination_folder)
    def Packer():
        print ()
        print ()
        print ()
        print ()
        print ("All functions have been done")
        print ("Go to " + dlcfolder + " and move the pak01_dir in vpk.exe. Then copy it to the new DLC folder made.")
        print ("You can find the vpk.exe in the bin folder of Portal2")
        print ("Now quit Portal 2 and open it again.")
        print ("Wait for the dots to turn orange then restart.")
        print ("Hopefully everything should be fine.")
        print ("If you have any questions dm Areng#0001 on discord.")
        time.sleep(2.5)
        print ("You may now close this window.")
        time.sleep(10)
    MakeFolders()
    MoveAssets()
    editfiles("fizzler")
    editfiles("fizzler_center")
    editfiles("fizzler_l")
    editfiles("fizzler_r")
    editfiles("fizzler_underground")
    editfiles("fizzler_underground_elevator")
    editfiles("fizzler_underground_side_emitters")
    editfiles("fizzler_underground_wide_center")
    editfiles("fizzler_underground_wide_side_l")
    editfiles("fizzler_underground_wide_side_r")
    Packer()
else: 
    quit