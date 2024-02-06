#### 06/02

read the setting files and run the experiments
1 run the scene_generation.py to generate the scenes
basically to get the training data for future use. Currently use the ns_ap.json, can change in the future.
generation file is render_images.py, maybe don't need to change in the future

2 run the instruction_generation to generate the instructions
this one use the scenes.json generated in the last step, in my experiment it would be ns_ap_sceces.json in the scene output folder. 
the output of instructions is the detailed instructions for the agents to read, can control the generation position

for instruction deneration part, the final output is a dict. save the obj name with the movements in numbers, then ue them for further simulation
