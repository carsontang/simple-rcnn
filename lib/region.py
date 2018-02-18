# region_proposer.py
"""
This module contains the RegionProposer class. RegionProposer proposes
candidate regions of an image using the algorithm specified in
"Selective Search for Object Recognition" by Uijlings et. al.
"""
import cv2

class Region:
    """
    a box consists of [x1 y1 x2 y2]. Refer to https://goo.gl/f9ipkV.
    """
    def __init__(self):
        pass

    def warp(self, bbox):
        pass

class RegionProposer:
    def __init__(self):
        pass

    def get_regions(self, image):
        cv2.setUseOptimized(True)
        cv2.setNumThreads(8)

        # ss stands for "selective search"
        ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
        ss.setBaseImage(image)
        ss.switchToSelectiveSearchFast()

        # Run selective search on the image to fetch regions.
        # Regions are returned as coordinates

        region_coordinates = ss.process()

        return region_coordinates