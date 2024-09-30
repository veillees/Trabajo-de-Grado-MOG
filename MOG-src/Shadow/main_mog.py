"""
===============================================================================
Main script 
Creates the Black Hole image
===============================================================================
@author: Eduard Larrañaga, Luis Flórez - 2024
===============================================================================
"""
#import warnings
#warnings.filterwarnings('ignore')

from numpy import pi
from black_holes import schwarzschild
from black_holes import kerr
from black_holes import num_schwarzschild
from black_holes import scalar_hair_BH
from black_holes import schwarzschild_mog
from black_holes import kerr_mog
from accretion_structures import simple_disk 
from accretion_structures import thin_disk 
from accretion_structures import ring_disk 
from accretion_structures import ring_disk_2
from detectors import image_plane 
from common.common import Image
import warnings
warnings.filterwarnings("ignore")




'''
===============================================================================
============================ BLACK HOLE DEFINITION ============================
===============================================================================
'''

##### SCHWARZSCHILD BH
#M = 1 # Mass
#blackhole = schwarzschild.BlackHole(M)

###### MOG BH
#M = 1   # Mass
#alpha = 0.5 # MOG alpha parameter
#blackhole = schwarzschild_mog.BlackHole(M,alpha)

###### KERR_MOG BH
M = 1   # Mass
a = 0.6 # Angular Monmentum
alpha = 0.5
blackhole = kerr_mog.BlackHole(M,a,alpha)

##### KERR BH
#M = 1   # Mass
#a = 0.6 # Angular Monmentum
#blackhole = kerr.BlackHole(M,a)


##### NUMERICAL SCHWARZSCHILD BH
#blackhole = num_schwarzschild.BlackHole(M)


##### SCALAR HAIR BH
#M = 1
#blackhole = scalar_hair_BH.BlackHole()

'''
===============================================================================
=========================== DETECTOR PARAMETERS ===============================
===============================================================================
'''
D = 100*M              # Distance to the BH
iota = (pi/180)*(87)    # Inclination Angle
x_side = 25*M
x_pixels = 400

detector = image_plane.detector(D=D, iota=iota, x_pixels=x_pixels, 
                                x_side=x_side, ratio='16:9')


'''
===============================================================================
============================ ACCRETION STRUCTURE ==============================
===============================================================================
'''

#acc_structure = simple_disk.structure(blackhole, 6, 20)


########### NOVIKOV-THORNE THIN DISK
#R_min = blackhole.ISCOco 
#R_max = 20*M
acc_structure = thin_disk.structure(blackhole)

########### RINGS DISK

#acc_structure = ring_disk.structure(blackhole)


'''
===============================================================================
============================ IMAGE FILENAME ===================================
===============================================================================
'''
filename = 'StaticMOGBlackHoleTD_adan'
savefig = False








'''
===============================================================================
==================================== MAIN =====================================
===============================================================================
'''
image = Image(blackhole, acc_structure, detector)

# Photons creation
image.create_photons()

# Create the image data
image.create_image()

# Plot the image
image.plot(savefig=savefig, filename=filename, cmap='inferno')
#image.plotContours(savefig=savefig, filename=filename)
