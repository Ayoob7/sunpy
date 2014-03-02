# -*- coding: utf-8 -*-

import os

import numpy as np

import sunpy.data.test
import sunpy.map

from sunpy.instr import iris

def test_SJI_to_cube():
    test_data = os.path.join(sunpy.data.test.rootdir,'iris_l2_20130801_074720_4040000014_SJI_1400_t000.fits')
    iris_cube = iris.SJI_to_cube(test_data, start=0, stop=None, hdu=0)
    
    assert isinstance(iris_cube, sunpy.map.MapCube)
    assert isinstance(iris_cube.maps[0], sunpy.map.sources.IRISMap)
    assert len(iris_cube._maps) == 2
    assert iris_cube._maps[0].meta['DATE-OBS'] != iris_cube._maps[1].meta['DATE-OBS']

def test_iris_rot():
    test_data = os.path.join(sunpy.data.test.rootdir,'iris_l2_20130801_074720_4040000014_SJI_1400_t000.fits')
    iris_cube = iris.SJI_to_cube(test_data, start=0, stop=None, hdu=0)
    irismap = iris_cube.maps[0]
    irismap_rot = irismap.iris_rot()
    
    assert isinstance(irismap_rot, sunpy.map.sources.IRISMap)
    assert not np.allclose(irismap_rot.data, irismap.data)
    
    assert irismap_rot.meta['pc1_1'] == 1
    assert irismap_rot.meta['pc1_2'] == 0
    assert irismap_rot.meta['pc2_1'] == 0
    assert irismap_rot.meta['pc2_2'] == 1
