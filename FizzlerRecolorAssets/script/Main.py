from asyncore import write
from cgi import print_arguments
from codecs import ignore_errors
from posixpath import relpath
import re
import subprocess
from dataclasses import replace
from genericpath import isfile
from distutils.dir_util import copy_tree
import os
import shutil
import random
import string
import time
import atexit
import colorama
import sys
from colorama import Fore

print ("Fizzler Recolor")
print ("By Areng")
print ()
print ("")
print ("If the program crashes please contact Areng on discord (Areng#0001)")

#Imports shit
RelPath = os.path.realpath(__file__)
RelPath = RelPath.replace("\\","/")
RelPath = RelPath.replace("/FizzlerRecolorAssets/script/Main.py","")
RelPath = RelPath.replace("/script.py","")

P2Directory = ""
ReadData = open(RelPath + "/Readme.txt",'r')
for x in range(12):
    ReadData1 = ReadData.readline()
ReadData.close
ReadData1 = ReadData1.replace('\\', '/')

isFile = os.path.isfile(ReadData1 + "/portal2.exe")
print (isFile)
print (ReadData1)
def Clear():
    for x in range(1000):
        print ()
if isFile == False:
    Clear()
    print (ReadData1)
    print ("is an invalid Directory! Please put in a correct directory for Portal 2")
    quit()

while True:
    Clear()
    P2Directory = ReadData1
    def CheckAssets():
        Checkr = os.path.exists(P2Directory + "/FizzlerRecolorAssets")
        if Checkr == False:
            print ("No Assets for Fizzler Recolor found in the Portal 2 Directory!")
            time.sleep(0.5)
            print ("Installing assets!")
            src = RelPath + "/FizzlerRecolorAssets"
            dest = P2Directory + r"/FizzlerRecolorAssets/"
            destination = shutil.copytree(src, dest, copy_function = shutil.copy) 
            print ("Succesfully installed assets into " + destination)
        elif Checkr == True:
            print ("Assets for fizzler recolor found!")
            pass
        else:
            quit
    def FindDLC():
        for y in range(1,100):
            isFile1 = os.path.exists(P2Directory + "/portal2_dlc" + str(y))
            if isFile1 == False:
                dlcfolder = "/portal2_dlc2"
                writefile = open(P2Directory + "/FizzlerRecolorAssets/data/dlc_data.txt",'w')
                writefile.write(dlcfolder)
                writefile.close
                return (dlcfolder)

    CheckAssets()
    print ("Closing Portal 2 to prevent any conflictions.")
    os.system("TASKKILL /F /IM portal2.exe")
    print ("Current Portal 2 Directory: " + P2Directory)
    print (Fore.RED + "If you are recoloring [BEEMOD] fizzlers, Export first then recolor via this program.")
    print (Fore.BLUE + "1. Fizzler [VANILLA] (All maps)")
    time.sleep(0.1)
    print ("2. Absolute Fizzler [BEEMOD] (On your maps ONLY)")
    time.sleep(0.1)
    print ("3. Compressed Smoke Field [BEEMOD] (On your maps ONLY)")
    time.sleep(0.1)
    print ("4. Force Deflection Field [BEEMOD] (On your maps ONLY)")
    time.sleep(0.1)
    print ("5. Matter Inquisition Field [BEEMOD] (On your maps ONLY)")
    time.sleep(0.1)
    print ("6. Closed Solid Field [BEEMOD] (On your maps ONLY)")
    time.sleep(0.1)
    print ("7. Portal Switcher Fizzler [BEEMOD] (On your maps ONLY)")
    time.sleep(0.1)
    print ("8. Death Fizzler [BEEMOD] (On your maps ONLY)")
    time.sleep(0.1)
    print ("9. Physics repulsion field [BEEMOD] (On your maps ONLY)")
    time.sleep(0.1)
    print ("10. Reset all")
    time.sleep(0.1)
    print ("11. Quit")
    EditWhat = int(input(Fore.YELLOW + "What option do you choose? (Integer) "))
    print ()
    if EditWhat == 1:
        dlcfolder = FindDLC()
    print ()
    if EditWhat == 10:
        pass
    if EditWhat == 11:
        pass
    if EditWhat == 12:
        pass
    else:
        Color = input("RGB Color code (r for random)(Red: Green: Blue:): ")
        

        if Color == "r":
            Random1 = random.randint(0,255)
            Random2 = random.randint(0,255)
            Random3 = random.randint(0,255)
            Color = str(Random1) + " " + str(Random2) + " " + str(Random3)
            print ()
            print (Fore.GREEN + "LOGS:")
            print ("Fizzler color is " + Color)

        else:
            print ("Fizzler color going to be changed to: " + Color)
            Color = Color.replace(',','')
            print ()
            print (Fore.GREEN + "LOGS:")
            print ("Fizzler color is " + Color)
            WriteData = open(P2Directory + "/FizzlerRecolorAssets/data/data.txt",'w')
            WriteData.write(P2Directory + '\n')
            WriteData.write("question = 1\n")
            WriteData.write("color = " + Color)
            WriteData.close
    #Gets information about the game dlcs
    def NormalFiz():

        def editfiles(FileName):
            Directory = P2Directory + dlcfolder + "/pak02_dir/materials/effects/"
            FileName2 = Directory + FileName + ".vmt"
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_COLOR "[0.025 0.08 0.1]"','$FLOW_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_VORTEX_COLOR "[0.64 2.058 2.56]"','$FLOW_VORTEX_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            print ("Successfully edited colors for " + FileName)
            #Writes the vmt

        def MakeFolders():
            path2 = P2Directory + dlcfolder + "/pak02_dir"
            path3 = P2Directory + dlcfolder + "/pak02_dir/materials"
            path4 = P2Directory + dlcfolder + "/pak02_dir/materials/effects"
            os.mkdir(path2)
            os.mkdir(path3)
            os.mkdir(path4)
            print ("Made folders in " + path2)
            print ("Made folders in " + path3)
            print ("Made folders in " + path4)
            #Makes the DLC folders

        def MoveAssets():
            source_folder = P2Directory + "/FizzlerRecolorAssets/effects/Normal/"
            destination_folder =P2Directory + dlcfolder + "/pak02_dir/materials/effects/"
            files_to_move = ['fizzler_bounds.vtf', 'fizzler_bounds.vtf','fizzler_bounds_l.vtf','fizzler_bounds_r.vtf','fizzler_edges.vmt','fizzler_flow.vtf','fizzler_noise.vtf','fizzler_ripples.vtf','fizzler_ripples_dim.vtf','fizzler_underground_bounds.vtf','fizzler_underground_elevator_bounds.vtf','fizzler_underground_flow.vtf','fizzler_underground_noise.vtf','fizzler_underground_ripples.vtf','fizzler_underground_ripples2.vtf','fizzler_underground_wide_center_bounds.vtf','fizzler_underground_wide_side_l_bounds.vtf','fizzler_underground_wide_side_r_bounds.vtf']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "from", source_folder, "to", destination_folder)
            source_folder = P2Directory + "/FizzlerRecolorAssets/effects/Normal/"
            destination_folder = P2Directory + dlcfolder + "/pak02_dir/materials/effects/"
            files_to_move = ['fizzler.vmt','fizzler_center.vmt','fizzler_l.vmt','fizzler_r.vmt','fizzler_underground.vmt','fizzler_underground_elevator.vmt','fizzler_underground_side_emitters.vmt','fizzler_underground_wide_center.vmt','fizzler_underground_wide_side_l.vmt','fizzler_underground_wide_side_r.vmt']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "from", source_folder, "to", destination_folder)
            #Moves assets to the DLC folder

        def Packer():
            pathtoopener = P2Directory + "/FizzlerRecolorAssets/packer/vpk.exe"
            pathtofile = P2Directory + dlcfolder + "/pak02_dir"
            subprocess.call([pathtoopener, pathtofile])
            location = P2Directory + dlcfolder
            dir = "pak02_dir"
            path = os.path.join(location, dir)
            shutil.rmtree(path, ignore_errors = True)
            print ()
            print ()
            print ()
            print (Fore.YELLOW + "Fizzler colors have been changed!")
            print ("Open Portal 2 and check if the fizzler colors have changed.")
            print ("If it has been changed, congrats!")
            print ("If it is not changed please contact Areng on discord.")
            print ("If you have any questions dm Areng#0001 on discord.")
            time.sleep(2.5)
            print ("You may now close this window.")
            input1 = input("Press any key to exit")
            quit
            #End Script
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



    def ABSFizzler():

        def editfiles(FileName):
            Directory = P2Directory + "/bee2/materials/bee2/fizz/abs_fizz/"
            FileName2 = Directory + FileName + ".vmt"
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_COLOR "[0.05 0.4 0.6]"','$FLOW_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_VORTEX_COLOR "[0.4 3.2 4.8]"','$FLOW_VORTEX_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            print ("Successfully edited colors for " + FileName)
            #Writes the vmt

        def MoveAssets():
            source_folder = P2Directory + "/FizzlerRecolorAssets/effects/Absolute/"
            destination_folder = P2Directory + "/bee2/materials/bee2/fizz/abs_fizz/"
            files_to_move = ['abs_fizz_bounds.vtf','abs_fizz_bounds_l.vtf','abs_fizz_bounds_r.vtf','absolute_center.vmt','absolute_field.vmt','absolute_left.vmt','absolute_right.vmt','retro_absolute_center.vmt','retro_absolute_field.vmt','retro_absolute_field_hallway.vmt','retro_absolute_left.vmt','retro_absolute_right.vmt',]
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "from", source_folder, "to", destination_folder)

        def Packer():
            print ()
            print ()
            print ()
            print (Fore.YELLOW + "Fizzler colors have been changed!")
            print ("Relaunch Portal2 and it will show the absolute fizzler recolored!")
            print ("Do not reexport beemod after this or else all beemod fizzlers will return to normal.")
            print ("If you have any questions dm Areng#0001 on discord.")
            time.sleep(2.5)
            print ("You may now close this window.")
            input1 = input("Press any key to exit")
            quit
        MoveAssets()
        editfiles("absolute_field")
        Packer()



    def CPF():

        def editfiles(FileName):
            Directory = P2Directory + "/bee2/materials/bee2/fizz/fourthreaper/"
            FileName2 = Directory + FileName + ".vmt"
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_COLOR "[0.3 0.1 0.4]"','$FLOW_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_VORTEX_COLOR "[5 2.5 5]"','$FLOW_VORTEX_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            print ("Successfully edited colors for " + FileName)
            #Writes the vmt

        def MoveAssets():
            source_folder = P2Directory + "/FizzlerRecolorAssets/effects/CompressedSmoke/"
            destination_folder = P2Directory + "/bee2/materials/bee2/fizz/fourthreaper/"
            files_to_move = ['compressed_smoke_field.vmt','clean_csf_right.vmt','clean_csf_left.vmt','clean_csf_center.vmt',]
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "from", source_folder, "to", destination_folder)

        def Packer():
            print ()
            print ()
            print ()
            print (Fore.YELLOW + "Fizzler colors have been changed!")
            print ("Relaunch Portal2 and it will show the compressed smoke field fizzler recolored!")
            print ("Do not reexport beemod after this or else all beemod fizzlers will return to normal.")
            print ("If you have any questions dm Areng#0001 on discord.")
            time.sleep(2.5)
            print ("You may now close this window.")
            input1 = input("Press any key to exit")
            quit
        MoveAssets()
        editfiles("compressed_smoke_field")
        Packer()



    def Force():

        def editfiles(FileName):
            Directory = P2Directory + "/bee2/materials/bee2/fizz/fourthreaper/"
            FileName2 = Directory + FileName + ".vmt"
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_COLOR "[0.3 0.15 0.0375]"','$FLOW_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_VORTEX_COLOR "[10 5 1.25]"','$FLOW_VORTEX_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            print ("Successfully edited colors for " + FileName)
            #Writes the vmt

        def MoveAssets():
            source_folder = P2Directory + "/FizzlerRecolorAssets/effects/Force/"
            destination_folder = P2Directory + "/bee2/materials/bee2/fizz/fourthreaper/"
            files_to_move = ['force_deflection_field.vmt','clean_fdf_right.vmt','clean_fdf_left.vmt','clean_fdf_center.vmt','old_fdf_right.vmt','cold_fdf_left.vmt','old_fdf_center.vmt',]
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "from", source_folder, "to", destination_folder)

        def Packer():
            print ()
            print ()
            print ()
            print (Fore.YELLOW + "Fizzler colors have been changed!")
            print ("Relaunch Portal2 and it will show the force detection field recolored!")
            print ("Do not reexport beemod after this or else all beemod fizzlers will return to normal.")
            print ("If you have any questions dm Areng#0001 on discord.")
            time.sleep(2.5)
            print ("You may now close this window.")
            input1 = input("Press any key to exit")
            quit
        MoveAssets()
        editfiles("force_deflection_field")
        Packer()



    def Matter():

        def editfiles(FileName):
            Directory = P2Directory + "/bee2/materials/bee2/fizz/fourthreaper/"
            FileName2 = Directory + FileName + ".vmt"
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_COLOR "[0.6 0.6 0.15]"','$FLOW_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_VORTEX_COLOR "[10 10 2.5]"','$FLOW_VORTEX_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            print ("Successfully edited colors for " + FileName)
            #Writes the vmt

        def MoveAssets():
            source_folder = P2Directory + "/FizzlerRecolorAssets/effects/Matter/"
            destination_folder = P2Directory + "/bee2/materials/bee2/fizz/fourthreaper/"
            files_to_move = ['matter_inquisition_field.vmt','clean_mif_right.vmt','clean_mif_left.vmt','clean_mif_center.vmt','old_mif_right.vmt','old_mif_left.vmt','old_mif_center.vmt','old_mif_short.vmt']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "from", source_folder, "to", destination_folder)

        def Packer():
            print ()
            print ()
            print ()
            print (Fore.YELLOW + "Fizzler colors have been changed!")
            print ("Relaunch Portal2 and it will show the Matter inquisition field recolored!")
            print ("Do not reexport beemod after this or else all beemod fizzlers will return to normal.")
            print ("If you have any questions dm Areng#0001 on discord.")
            time.sleep(2.5)
            print ("You may now close this window.")
            input1 = input("Press any key to exit")
            quit
        MoveAssets()
        editfiles("matter_inquisition_field")
        Packer()



    def Closed():

        def editfiles(FileName):
            Directory = P2Directory + "/bee2/materials/bee2/fizz/thedarkbomber/"
            FileName2 = Directory + FileName + ".vmt"
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_COLOR "[0.196 0.196 0.196]"','$FLOW_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_VORTEX_COLOR "[0.232 0.232 0.232]"','$FLOW_VORTEX_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            print ("Successfully edited colors for " + FileName)
            #Writes the vmt

        def MoveAssets():
            source_folder = P2Directory + "/FizzlerRecolorAssets/effects/closed/"
            destination_folder = P2Directory + "/bee2/materials/bee2/fizz/thedarkbomber/"
            files_to_move = ['closed_solid_field.vmt','clean_csfi_right.vmt','clean_csfi_left.vmt','clean_csfi_center.vmt','50s_csfi_right.vmt','50s_csfi_left.vmt','50s_csfi_center.vmt','50s_csfi.vmt','invis_paintable.vmt']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "from", source_folder, "to", destination_folder)

        def Packer():
            print ()
            print ()
            print ()
            print (Fore.YELLOW + "Fizzler colors have been changed!")
            print ("Relaunch Portal2 and it will show the Closed solid field recolored!")
            print ("Do not reexport beemod after this or else all beemod fizzlers will return to normal.")
            print ("If you have any questions dm Areng#0001 on discord.")
            time.sleep(2.5)
            print ("You may now close this window.")
            input1 = input("Press any key to exit")
            quit
        MoveAssets()
        editfiles("closed_solid_field")
        Packer()



    def Switch():

        def editfiles(FileName):
            Directory = P2Directory + "/bee2/materials/bee2/fizz/switch/"
            FileName2 = Directory + FileName + ".vmt"
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_COLOR "{0 64 255}"','$FLOW_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_VORTEX_COLOR "{0 128 255}"','$FLOW_VORTEX_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            print ("Successfully edited colors for " + FileName)
            #Writes the vmt

        def MoveAssets():
            source_folder = P2Directory + "/FizzlerRecolorAssets/effects/switch/"
            destination_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/bee2/materials/bee2/fizz/switch/"
            files_to_move = ['switch_field.vmt','switch_fizz_bounds.vtf','switch_fizz_bounds_l.vtf','switch_fizz_bounds_r.vtf','switch_left.vmt','switch_right.vmt','switch_center.vmt']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "from", source_folder, "to", destination_folder)

        def Packer():
            print ()
            print ()
            print ()
            print (Fore.YELLOW + "Fizzler colors have been changed!")
            print ("Relaunch Portal2 and it will show the Portal Switcher Fizzler recolored!")
            print ("Do not reexport beemod after this or else all beemod fizzlers will return to normal.")
            print ("If you have any questions dm Areng#0001 on discord.")
            time.sleep(2.5)
            print ("You may now close this window.")
            input1 = input("Press any key to exit")
            quit
        MoveAssets()
        editfiles("switch_field")
        Packer()


    
    def Death():

        def editfiles(FileName):
            Directory = P2Directory + "/bee2/materials/bee2/fizz/lp/"
            FileName2 = Directory + FileName + ".vmt"
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_COLOR "[0.9 0.1 0.1]"','$FLOW_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_VORTEX_COLOR "[10 2.5 2.5]"','$FLOW_VORTEX_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            print ("Successfully edited colors for " + FileName)
            #Writes the vmt

        def MoveAssets():
            source_folder = P2Directory + "/FizzlerRecolorAssets/effects/death/"
            destination_folder = P2Directory + "/bee2/materials/bee2/fizz/lp/"
            files_to_move = ['death_field_clean_center.vmt','death_field_clean_left.vmt','death_field_clean_right.vmt','death_field_clean_short.vmt','death_field_old_center.vmt','death_field_old_center.vmt','death_field_old_left.vmt','death_field_old_right.vmt','death_field_old_short.vmt']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "from", source_folder, "to", destination_folder)

        def Packer():
            print ()
            print ()
            print ()
            print (Fore.YELLOW + "Fizzler colors have been changed!")
            print ("Relaunch Portal2 and it will show the Death Fizzler recolored!")
            print ("Do not reexport beemod after this or else all beemod fizzlers will return to normal.")
            print ("If you have any questions dm Areng#0001 on discord.")
            time.sleep(2.5)
            print ("You may now close this window.")
            input1 = input("Press any key to exit")
            quit
        MoveAssets()
        editfiles("death_field_clean_center")
        editfiles("death_field_old_center")
        Packer()



    def Pys():

        def editfiles(FileName):
            Directory = P2Directory + "/bee2/materials/bee2/fizz/phys_shield/"
            FileName2 = Directory + FileName + ".vmt"
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_COLOR "[0.025 0.64 0.1]"','$FLOW_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_VORTEX_COLOR "[0.64 012 2.56]"','$FLOW_VORTEX_COLOR "{' + Color + '}"')
                #Finds and replaces the defult color code with the new one
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(FileName2,'w')
            writing_file.write(new_file_content)
            writing_file.close()
            print ("Successfully edited colors for " + FileName)
            #Writes the vmt

        def MoveAssets():
            source_folder = P2Directory + "/FizzlerRecolorAssets/effects/phys_shield/"
            destination_folder = P2Directory + "/bee2/materials/bee2/fizz/phys_shield/"
            files_to_move = ['50s_pshield.vmt','50s_pshield_center.vmt','50s_pshield_left.vmt','50s_pshield_right.vmt','clean_pshield_center.vmt','clean_pshield_left.vmt','clean_pshield_right.vmt','physics_shield.vmt','physler_flow.vtf','physler_noise.vtf']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "from", source_folder, "to", destination_folder)

        def Packer():
            print ()
            print ()
            print ()
            print (Fore.YELLOW + "Fizzler colors have been changed!")
            print ("Relaunch Portal2 and it will show the Physics repulsion field recolored!")
            print ("Do not reexport beemod after this or else all beemod fizzlers will return to normal.")
            print ("If you have any questions dm Areng#0001 on discord.")
            time.sleep(2.5)
            print ("You may now close this window.")
            input1 = input("Press any key to exit")
            quit
        MoveAssets()
        editfiles("physics_shield")
        editfiles("50s_pshield")
        Packer()

    

    def Restore():

        def MoveAssets():
            source_folder = P2Directory + "/FizzlerRecolorAssets/effects/phys_shield/"
            destination_folder = P2Directory + "/bee2/materials/bee2/fizz/phys_shield/"
            files_to_move = ['50s_pshield.vmt','50s_pshield_center.vmt','50s_pshield_left.vmt','50s_pshield_right.vmt','clean_pshield_center.vmt','clean_pshield_left.vmt','clean_pshield_right.vmt','physics_shield.vmt','physler_flow.vtf','physler_noise.vtf']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "from", source_folder, "to", destination_folder)
            
            source_folder = P2Directory + "/FizzlerRecolorAssets/effects/death/"
            destination_folder = P2Directory + "/bee2/materials/bee2/fizz/lp/"
            files_to_move = ['death_field_clean_center.vmt','death_field_clean_left.vmt','death_field_clean_right.vmt','death_field_clean_short.vmt','death_field_old_center.vmt','death_field_old_center.vmt','death_field_old_left.vmt','death_field_old_right.vmt','death_field_old_short.vmt']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "from", source_folder, "to", destination_folder)

            source_folder = P2Directory + "/FizzlerRecolorAssets/effects/switch/"
            destination_folder = P2Directory + "/bee2/materials/bee2/fizz/switch/"
            files_to_move = ['switch_field.vmt','switch_fizz_bounds.vtf','switch_fizz_bounds_l.vtf','switch_fizz_bounds_r.vtf','switch_left.vmt','switch_right.vmt','switch_center.vmt']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "from", source_folder, "to", destination_folder)

            source_folder = P2Directory + "/FizzlerRecolorAssets/effects/closed/"
            destination_folder = P2Directory + "/bee2/materials/bee2/fizz/thedarkbomber/"
            files_to_move = ['closed_solid_field.vmt','clean_csfi_right.vmt','clean_csfi_left.vmt','clean_csfi_center.vmt','50s_csfi_right.vmt','50s_csfi_left.vmt','50s_csfi_center.vmt','50s_csfi.vmt','invis_paintable.vmt']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "from", source_folder, "to", destination_folder)

            source_folder = P2Directory + "/FizzlerRecolorAssets/effects/Matter/"
            destination_folder = P2Directory + "/bee2/materials/bee2/fizz/fourthreaper/"
            files_to_move = ['matter_inquisition_field.vmt','clean_mif_right.vmt','clean_mif_left.vmt','clean_mif_center.vmt','old_mif_right.vmt','old_mif_left.vmt','old_mif_center.vmt','old_mif_short.vmt']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "from", source_folder, "to", destination_folder)

            source_folder = P2Directory + "/FizzlerRecolorAssets/effects/Force/"
            destination_folder = P2Directory + "/bee2/materials/bee2/fizz/fourthreaper/"
            files_to_move = ['force_deflection_field.vmt','clean_fdf_right.vmt','clean_fdf_left.vmt','clean_fdf_center.vmt','old_fdf_right.vmt','old_fdf_left.vmt','old_fdf_center.vmt',]
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "from", source_folder, "to", destination_folder)

            source_folder = P2Directory + "/FizzlerRecolorAssets/effects/CompressedSmoke/"
            destination_folder = P2Directory + "/bee2/materials/bee2/fizz/fourthreaper/"
            files_to_move = ['compressed_smoke_field.vmt','clean_csf_right.vmt','clean_csf_left.vmt','clean_csf_center.vmt',]
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "from", source_folder, "to", destination_folder)
            
            path = P2Directory + dlcfolder
            os.remove(path + "pak02_dir.vpk")
        MoveAssets()
        print ()
        print ()
        print ()
        print ("All fizzler colors restored!")
        print ("If the colors are not restored please DM Areng on discord.")
        print("If you have any questions feel free to dm Areng#0001 on discord.")
        time.sleep(2.5)
        print ("You may now close this window.")
        input1 = input("Press any key to exit")
        quit

    if EditWhat == 1:
        NormalFiz()
    elif EditWhat == 2:
        ABSFizzler()
    elif EditWhat == 3:
        CPF()
    elif EditWhat == 4:
        Force()
    elif EditWhat == 5:
        Matter()
    elif EditWhat == 6:
        Closed()
    elif EditWhat == 7:
        Switch()
    elif EditWhat == 8:
        Death()
    elif EditWhat == 9:
        Pys()
    elif EditWhat == 10:
        Restore()
    elif EditWhat == 11:
        quit()
    else:
        print ("Not a valid option!")
        time.sleep(5)
        Clear()
        pass
