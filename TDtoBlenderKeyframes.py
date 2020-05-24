import bpy, os, math

filename = 'keys.txt'
#directory = '/home/zeffii/Desktop'  # <-- if you have linux or osx
directory = r'C:\Work\TD\CTRL'  # <-- if windows, the r is important
fullpath = os.path.join(directory, filename)

l = []

with open(fullpath, 'r', newline='') as f:
    for ln in f:
        l.append( ln.split("\t") )        
    l.pop(0)
    #print(l)

#each row is a keyframe with a specific value for a specific parameter.
#the for loop goes through each row to create the keyframes based on the parameter index. this is the dumb way to approach this.
for row in l:

    param = int(row[0])-1
    frame = int(float(row[1]))

    val = float(row[2])

    if param < 3:
        bpy.data.objects["CameraPivot"].location[param] = val
        bpy.data.objects["CameraPivot"].keyframe_insert(data_path='location', index=param, frame=frame)
    elif param < 6:
        bpy.data.objects["Camera"].location[param-3] = val
        bpy.data.objects["Camera"].keyframe_insert(data_path='location', index=param-3, frame=frame)    
    elif param < 9:
        bpy.data.objects["CameraPivot"].rotation_euler[param-6] = math.radians(val)
        bpy.data.objects["CameraPivot"].keyframe_insert(data_path='rotation_euler', index=param-6, frame=frame)    