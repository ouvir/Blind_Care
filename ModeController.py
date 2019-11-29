class ModeController:

    def __init__(self, Tag_info):
        self.Tag_info = Tag_info

    def Mode(self):
        if self.Tag_info == True:
            mode_info = 1
            #mode_info = 1 : start to ColorSensor
        else:
            mode_info = 0
            #mode_info = 0 : start to UltraSonicSensor
        return mode_info
''' 
    mode_info = ModeController(Tag_info)
    mode_info.Mode()
 >> Use <Tag_info> And <mode_info> Return.  
'''
