"""
My Game Fast :P
http://www.mygamefast.com
"""
from direct.showbase.ShowBase import ShowBase   # import the bits of panda
from panda3d.core import GeoMipTerrain          # that we need

class MyApp(ShowBase):                          # our 'class'
    def __init__(self):
        ShowBase.__init__(self)                        # initialise
        terrain = GeoMipTerrain("worldTerrain")        # create a terrain
        terrain.setHeightfield("HM.jpg")            # set the height map
        #terrain.setColorMap("512xA_TN.jpg")               # set the colour map
        terrain.setBruteforce(True)                    # level of detail
        root = terrain.getRoot()                       # capture root
        root.reparentTo(render)                        # render from root
        root.setSz(60)                                 # maximum height
        terrain.generate()                             # generate

app = MyApp()                                   # our 'object'
app.run()