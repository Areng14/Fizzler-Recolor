import os
import shutil
import random
import time
import colorama
from colorama import Fore
#Imports shit


var1 = input("Is the assets in the portal 2 directory? (yes/no): ")
if var1 == "yes":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    print (Fore.RED + "Warning! If the fizzler files are NOT found, this program will crash sorry!")
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
    EditWhat = int(input(Fore.YELLOW + "What fizzler are we editing? (Integer) "))
    print ()
    dlcfolderint = int(input("What is your highest dlc folder? (Integer) "))
    print ()
    Color = input("RGB Color code (r for random),(Red: Green: Blue:): ")
    if Color == "r":
        Random1 = random.randint(0,255)
        Random2 = random.randint(0,255)
        Random3 = random.randint(0,255)
        Color = str(Random1) + " " + str(Random2) + " " + str(Random3)
    dlcfolderint += 1
    dlcfolder = "portal2_dlc" + str(dlcfolderint)
    #Gets information about the game dlcs
    def NormalFiz():
        def editfiles(FileName):
            Directory = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/" + dlcfolder + "/pak01_dir/materials/effects/"
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
            path1 = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/" + dlcfolder
            path2 = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/" + dlcfolder + "/pak01_dir"
            path3 = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/" + dlcfolder + "/pak01_dir/materials"
            path4 = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/" + dlcfolder + "/pak01_dir/materials/effects"
            os.mkdir(path1)
            os.mkdir(path2)
            os.mkdir(path3)
            os.mkdir(path4)
            print ("Made folders in " + path1)
            #Makes the DLC folders
        def MoveAssets():
            source_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/FizzlerRecolorAssets/effects/Normal/"
            destination_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/" + dlcfolder + "/pak01_dir/materials/effects/"
            files_to_move = ['fizzler_bounds.vtf', 'fizzler_bounds.vtf','fizzler_bounds_l.vtf','fizzler_bounds_r.vtf','fizzler_edges.vmt','fizzler_flow.vtf','fizzler_noise.vtf','fizzler_ripples.vtf','fizzler_ripples_dim.vtf','fizzler_underground_bounds.vtf','fizzler_underground_elevator_bounds.vtf','fizzler_underground_flow.vtf','fizzler_underground_noise.vtf','fizzler_underground_ripples.vtf','fizzler_underground_ripples2.vtf','fizzler_underground_wide_center_bounds.vtf','fizzler_underground_wide_side_l_bounds.vtf','fizzler_underground_wide_side_r_bounds.vtf']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "to", destination_folder)
            source_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/FizzlerRecolorAssets/effects/Normal/"
            destination_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/" + dlcfolder + "/pak01_dir/materials/effects/"
            files_to_move = ['fizzler.vmt','fizzler_center.vmt','fizzler_l.vmt','fizzler_r.vmt','fizzler_underground.vmt','fizzler_underground_elevator.vmt','fizzler_underground_side_emitters.vmt','fizzler_underground_wide_center.vmt','fizzler_underground_wide_side_l.vmt','fizzler_underground_wide_side_r.vmt']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "to", destination_folder)
            #Moves assets to the DLC folder
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
            Directory = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/bee2/materials/bee2/fizz/abs_fizz/"
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
            source_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/FizzlerRecolorAssets/effects/Absolute/"
            destination_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/bee2/materials/bee2/fizz/abs_fizz/"
            files_to_move = ['abs_fizz_bounds.vtf','abs_fizz_bounds_l.vtf','abs_fizz_bounds_r.vtf','absolute_center.vmt','absolute_field.vmt','absolute_left.vmt','absolute_right.vmt','retro_absolute_center.vmt','retro_absolute_field.vmt','retro_absolute_field_hallway.vmt','retro_absolute_left.vmt','retro_absolute_right.vmt',]
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "to", destination_folder)
        def Packer():
            print ()
            print ()
            print ()
            print ("All functions have been completed!")
            print ("Relaunch Portal2 and it will show the absolute fizzler recolored!")
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
            Directory = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/bee2/materials/bee2/fizz/fourthreaper/"
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
            source_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/FizzlerRecolorAssets/effects/CompressedSmoke/"
            destination_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/bee2/materials/bee2/fizz/fourthreaper/"
            files_to_move = ['compressed_smoke_field.vmt','clean_csf_right.vmt','clean_csf_left.vmt','clean_csf_center.vmt',]
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "to", destination_folder)
        def Packer():
            print ()
            print ()
            print ()
            print ("All functions have been completed!")
            print ("Relaunch Portal2 and it will show the compressed smoke field fizzler recolored!")
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
            Directory = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/bee2/materials/bee2/fizz/fourthreaper/"
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
            source_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/FizzlerRecolorAssets/effects/Force/"
            destination_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/bee2/materials/bee2/fizz/fourthreaper/"
            files_to_move = ['force_deflection_field.vmt','clean_fdf_right.vmt','clean_fdf_left.vmt','clean_fdf_center.vmt','old_fdf_right.vmt','cold_fdf_left.vmt','old_fdf_center.vmt',]
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "to", destination_folder)
        def Packer():
            print ()
            print ()
            print ()
            print ("All functions have been completed!")
            print ("Relaunch Portal2 and it will show the force detection field recolored!")
            print ("If you have any questions dm Areng#0001 on discord.")
            time.sleep(2.5)
            print ("You may now close this window.")
            input1 = input("Press any key to exit")
            quit
        MoveAssets()
        editfiles("force_deflection_field")
        Packer()
    def Force():
        def editfiles(FileName):
            Directory = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/bee2/materials/bee2/fizz/fourthreaper/"
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
            source_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/FizzlerRecolorAssets/effects/Force/"
            destination_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/bee2/materials/bee2/fizz/fourthreaper/"
            files_to_move = ['force_deflection_field.vmt','clean_fdf_right.vmt','clean_fdf_left.vmt','clean_fdf_center.vmt','old_fdf_right.vmt','old_fdf_left.vmt','old_fdf_center.vmt','old_fdf_short.vmt']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "to", destination_folder)
        def Packer():
            print ()
            print ()
            print ()
            print ("All functions have been completed!")
            print ("Relaunch Portal2 and it will show the force detection field recolored!")
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
            Directory = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/bee2/materials/bee2/fizz/fourthreaper/"
            FileName2 = Directory + FileName + ".vmt"
            reading_file = open(FileName2,'r')
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace('$FLOW_COLOR "[0.6 0.6 0.15]""','$FLOW_COLOR "{' + Color + '}"')
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
            source_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/FizzlerRecolorAssets/effects/Matter/"
            destination_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/bee2/materials/bee2/fizz/fourthreaper/"
            files_to_move = ['matter_inquisition_field.vmt','clean_mif_right.vmt','clean_mif_left.vmt','clean_mif_center.vmt','old_mif_right.vmt','old_mif_left.vmt','old_mif_center.vmt','old_mif_short.vmt']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "to", destination_folder)
        def Packer():
            print ()
            print ()
            print ()
            print ("All functions have been completed!")
            print ("Relaunch Portal2 and it will show the force detection field recolored!")
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
            Directory = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/bee2/materials/bee2/fizz/thedarkbomber/"
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
            source_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/FizzlerRecolorAssets/effects/closed/"
            destination_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/bee2/materials/bee2/fizz/thedarkbomber/"
            files_to_move = ['closed_solid_field.vmt','clean_csfi_right.vmt','clean_csfi_left.vmt','clean_csfi_center.vmt','50s_csfi_right.vmt','50s_csfi_left.vmt','50s_csfi_center.vmt','50s_csfi.vmt','invis_paintable.vmt']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "to", destination_folder)
        def Packer():
            print ()
            print ()
            print ()
            print ("All functions have been completed!")
            print ("Relaunch Portal2 and it will show the force detection field recolored!")
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
            Directory = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/bee2/materials/bee2/fizz/switch/"
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
            source_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/FizzlerRecolorAssets/effects/switch/"
            destination_folder = "C:/Program Files (x86)/Steam/steamapps/common/Portal 2/bee2/materials/bee2/fizz/switch/"
            files_to_move = ['switch_field.vmt','switch_fizz_bounds.vtf','switch_fizz_bounds_l.vtf','switch_fizz_bounds_r.vtf','switch_left.vmt','switch_right.vmt','switch_center.vmt']
            for file in files_to_move:
                source = source_folder + file
                destination = destination_folder + file
                shutil.copyfile(source, destination)
                print('Copied', file, "to", destination_folder)
        def Packer():
            print ()
            print ()
            print ()
            print ("All functions have been completed!")
            print ("Relaunch Portal2 and it will show the force detection field recolored!")
            print ("If you have any questions dm Areng#0001 on discord.")
            time.sleep(2.5)
            print ("You may now close this window.")
            input1 = input("Press any key to exit")
            quit
        MoveAssets()
        editfiles("switch_field")
        Packer()
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
    else:
        print ("Not a valid option!")
        time.sleep(5)
        quit


        
else: 
    quit