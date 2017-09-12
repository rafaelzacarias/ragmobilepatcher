
import hashlib

fnamelst = ["files/patched_config.unity3d","files/patched_framework.unity3d", "files/patched_functionsystem.unity3d"]
new_dict = {}

for fname in fnamelst:
    new_dict[fname] = hashlib.md5(open(fname,'rb').read()).hexdigest()


for item in new_dict:
    print item, new_dict[item]
    
    
with open("files.json") as fjson:
    for line in fjson:
        print line