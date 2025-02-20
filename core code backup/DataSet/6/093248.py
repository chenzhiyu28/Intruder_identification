from numpy import *
FRAMES = [{'numObj': 10, 'x': array([0.01318526, 0.        , 0.02637051, 0.        , 0.03955577,
       0.        , 0.05274103, 0.00329631, 0.06592628, 0.00824079],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 0.001, 'frameNumber': 1}, {'numObj': 10, 'x': array([0.01318526, 0.        , 0.02637051, 0.        , 0.03955577,
       0.        , 0.05274103, 0.00329631, 0.06592628, 0.00824079],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 0.098, 'frameNumber': 2}, {'numObj': 11, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.07004668,  0.00824079,
       -0.78287464], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11170749, 0.13159479,
       1.0609511 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 0.163, 'frameNumber': 3}, {'numObj': 11, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00824079,
       -0.78287464], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479,
       1.0609511 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 0.218, 'frameNumber': 4}, {'numObj': 10, 'x': array([0.01318526, 0.        , 0.02637051, 0.        , 0.03955577,
       0.        , 0.05274103, 0.00329631, 0.06592628, 0.00824079],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 0.271, 'frameNumber': 5}, {'numObj': 10, 'x': array([0.01318526, 0.        , 0.02637051, 0.        , 0.03955577,
       0.        , 0.05274103, 0.00329631, 0.06592628, 0.00824079],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 0.324, 'frameNumber': 6}, {'numObj': 11, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00824079,
       -0.78287464], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479,
       1.0609511 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 0.428, 'frameNumber': 7}, {'numObj': 13, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00824079,
       -0.78287464,  1.3448962 ,  1.3514888 ], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479,
       1.0609511 , 5.2087603 , 5.234294  ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0.       , 0.       , 0.       , 0.       , 0.       , 0.       ,
       0.       , 0.       , 0.       , 0.       , 0.       , 1.2850258,
       1.2850258], dtype=float32), 'time': 0.532, 'frameNumber': 8}, {'numObj': 11, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00824079,
       -0.78287464], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479,
       1.0609511 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 0.636, 'frameNumber': 9}, {'numObj': 10, 'x': array([0.01318526, 0.        , 0.02637051, 0.        , 0.03955577,
       0.        , 0.05274103, 0.00329631, 0.06592628, 0.00824079],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 0.744, 'frameNumber': 10}, {'numObj': 10, 'x': array([0.01318526, 0.        , 0.02637051, 0.        , 0.03955577,
       0.        , 0.05274103, 0.00329631, 0.06592628, 0.00824079],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 0.847, 'frameNumber': 11}, {'numObj': 11, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.00164816,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00824079,
       -0.78287464], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05271527, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479,
       1.0609511 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 0.951, 'frameNumber': 12}, {'numObj': 10, 'x': array([0.01318526, 0.        , 0.02637051, 0.        , 0.03955577,
       0.        , 0.05274103, 0.00329631, 0.07004668, 0.00824079],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11170749, 0.13159479],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 1.005, 'frameNumber': 13}, {'numObj': 12, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.07004668,  0.00412039,
       -0.78287464,  0.44500244], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11170749, 0.13178816,
       1.0609511 , 4.725787  ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.91787565], dtype=float32), 'time': 1.109, 'frameNumber': 14}, {'numObj': 11, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00412039,
       -0.78287464], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13178816,
       1.0609511 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 1.213, 'frameNumber': 15}, {'numObj': 16, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00824079,
       -0.78287464,  0.7070594 ,  0.8306712 ,  0.8364397 ,  0.72189283,
        0.7268373 ], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479,
       1.0609511 , 3.7041035 , 3.7053857 , 3.7311175 , 3.781812  ,
       3.807715  ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
      dtype=float32), 'velocity': array([0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.55072534, 0.55072534, 0.55072534, 0.55072534,
       0.55072534], dtype=float32), 'time': 1.317, 'frameNumber': 16}, {'numObj': 15, 'x': array([0.01318526, 0.        , 0.02637051, 0.        , 0.03955577,
       0.        , 0.05274103, 0.00329631, 0.06592628, 0.00412039,
       0.67244816, 0.6773926 , 0.68233705, 0.25876066, 0.26040882],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13178816,
       3.522784  , 3.548687  , 3.5745897 , 4.1320763 , 4.158396  ],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
      dtype=float32), 'velocity': array([0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.91787565, 0.91787565, 0.91787565, 1.1014507 , 1.1014507 ],
      dtype=float32), 'time': 1.421, 'frameNumber': 17}, {'numObj': 11, 'x': array([0.01318526, 0.        , 0.02637051, 0.        , 0.03955577,
       0.        , 0.05274103, 0.00329631, 0.07004668, 0.00824079,
       0.52741027], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11170749, 0.13159479,
       3.3339672 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.55072534], dtype=float32), 'time': 1.533, 'frameNumber': 18}, {'numObj': 10, 'x': array([0.01318526, 0.        , 0.02637051, 0.        , 0.03955577,
       0.        , 0.05274103, 0.00329631, 0.06592628, 0.00824079],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 1.638, 'frameNumber': 19}, {'numObj': 10, 'x': array([0.01318526, 0.        , 0.02637051, 0.        , 0.03955577,
       0.        , 0.05274103, 0.00329631, 0.07004668, 0.00412039],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11170749, 0.13178816],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 1.743, 'frameNumber': 20}, {'numObj': 17, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00412039,
       -0.78287464,  0.40791887,  0.41203928,  0.41615966,  0.42028007,
        0.42440045,  0.42852086], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13178816,
       1.0609511 , 2.5786152 , 2.6046617 , 2.6307085 , 2.6567552 ,
       2.6828017 , 2.7088485 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
      dtype=float32), 'velocity': array([0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.55072534, 0.55072534, 0.55072534, 0.55072534,
       0.55072534, 0.55072534], dtype=float32), 'time': 1.846, 'frameNumber': 21}, {'numObj': 13, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.07004668,  0.00412039,
       -0.78287464,  0.23733464, -0.6328924 ], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11170749, 0.13178816,
       1.0609511 , 2.5204198 , 2.4511817 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.91787565, 0.91787565], dtype=float32), 'time': 1.951, 'frameNumber': 22}, {'numObj': 19, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00824079,
        0.28348303,  0.28677934,  0.20272332,  0.20519556,  0.2768904 ,
        0.2801867 , -0.21508451, -0.21755674, -0.29337198], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479,
       2.2500768 , 2.2762403 , 2.1528585 , 2.179113  , 2.1977494 ,
       2.223913  , 2.2841303 , 2.3103848 , 2.328568  ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0.], dtype=float32), 'velocity': array([ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.91787565,  0.91787565,  1.1014507 ,  1.1014507 ,  1.1014507 ,
        1.1014507 , -1.468601  , -1.468601  , -1.468601  ], dtype=float32), 'time': 2.056, 'frameNumber': 23}, {'numObj': 30, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.07004668,  0.00412039,
       -0.78287464, -0.80100435,  0.        , -0.74331886,  0.        ,
       -0.7523837 ,  0.        , -0.8306712 ,  0.        ,  0.19036214,
       -0.5710864 ,  0.19283438, -0.57850313,  0.24392726,  1.0366908 ,
        0.24722357,  0.9888943 ,  0.05603734,  0.05686142,  0.115371  ],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11170749, 0.13178816,
       1.0609511 , 1.9801358 , 2.1360116 , 2.0306094 , 2.1623821 ,
       2.0553727 , 2.1887527 , 2.0534742 , 2.2151232 , 2.0215867 ,
       1.9485663 , 2.047841  , 1.9738723 , 1.9361125 , 1.6532708 ,
       1.9622762 , 1.7128152 , 1.7923192 , 1.8186768 , 1.8423271 ],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.55072534, 0.55072534, 0.55072534, 0.55072534,
       0.55072534, 0.55072534, 0.55072534, 0.55072534, 0.7343005 ,
       0.7343005 , 0.7343005 , 0.7343005 , 0.91787565, 0.91787565,
       1.1014507 , 1.1014507 , 1.2850258 , 1.2850258 , 1.2850258 ],
      dtype=float32), 'time': 2.111, 'frameNumber': 24}, {'numObj': 15, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.07004668,  0.00824079,
       -0.7317818 ,  0.        , -0.24227908, -0.24475133, -0.24722356],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11170749, 0.13159479,
       1.8090129 , 1.951418  , 2.5729284 , 2.5991828 , 2.625437  ],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
      dtype=float32), 'velocity': array([0.       , 0.       , 0.       , 0.       , 0.       , 0.       ,
       0.       , 0.       , 0.       , 0.       , 1.2850258, 1.2850258,
       1.2850258, 1.2850258, 1.2850258], dtype=float32), 'time': 2.215, 'frameNumber': 25}, {'numObj': 24, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.07004668,  0.00824079,
        0.14338967,  0.7169484 ,  0.1458619 ,  0.7293095 ,  0.14833415,
        0.15080637,  0.15327862, -0.65267026, -0.66255915, -0.67244816,
       -0.30161273, -0.30655724,  0.2999646 , -0.5999292 ], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11170749, 0.13159479,
       1.5227537 , 1.3510456 , 1.5490079 , 1.3743395 , 1.5752623 ,
       1.6015167 , 1.627771  , 1.613444  , 1.6378902 , 1.6623362 ,
       1.5800722 , 1.6059749 , 2.3808951 , 2.3235157 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.91787565,  0.91787565,  0.91787565,  0.91787565,  0.91787565,
        0.91787565,  0.91787565,  0.91787565,  0.91787565,  0.91787565,
       -1.468601  , -1.468601  , -1.2850258 , -1.2850258 ], dtype=float32), 'time': 2.321, 'frameNumber': 26}, {'numObj': 35, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00824079,
       -0.78287464,  0.04367616, -0.48043782,  0.        , -0.48950267,
        0.        , -0.49856755,  0.0461484 , -0.50763243, -0.56366974,
        0.        , -0.62135524, -0.04779656, -0.6320682 , -0.04202801,
        0.20519556, -0.6155867 ,  0.2076678 , -0.62300336,  0.21014003,
       -0.6304201 ,  0.21261227, -0.6378368 ,  0.21508451, -0.7169484 ],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479,
       1.0609511 , 1.3969547 , 1.3124669 , 1.4240078 , 1.3372304 ,
       1.4503783 , 1.3619939 , 1.4760275 , 1.3867575 , 1.3934289 ,
       1.5031193 , 1.3975897 , 1.5287429 , 1.421686  , 1.3442394 ,
       2.179113  , 2.1004026 , 2.2053673 , 2.1257088 , 2.2316215 ,
       2.1510148 , 2.257876  , 2.1763208 , 2.2841303 , 2.1793342 ],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0.], dtype=float32), 'velocity': array([ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.91787565,  0.91787565,  0.91787565,  0.91787565,
        0.91787565,  0.91787565,  0.91787565,  0.91787565,  1.1014507 ,
        1.1014507 ,  1.1014507 ,  1.1014507 ,  1.1014507 ,  1.2850258 ,
       -1.1014507 , -1.1014507 , -1.1014507 , -1.1014507 , -1.1014507 ,
       -1.1014507 , -1.1014507 , -1.1014507 , -1.1014507 , -1.1014507 ],
      dtype=float32), 'time': 2.426, 'frameNumber': 27}, {'numObj': 21, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.07004668,  0.00412039,
        0.        , -0.47466928,  0.        ,  0.04120393,  0.03708354,
        0.5191695 ,  0.03790762,  0.49279898,  0.03873169,  0.2538162 ,
       -0.21755674], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11170749, 0.13178816,
       1.2657847 , 1.1734139 , 1.2921551 , 1.3178817 , 1.1860936 ,
       1.0670784 , 1.2124512 , 1.1084331 , 1.2388089 , 1.1322012 ,
       1.1397243 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0.], dtype=float32), 'velocity': array([ 0.       ,  0.       ,  0.       ,  0.       ,  0.       ,
        0.       ,  0.       ,  0.       ,  0.       ,  0.       ,
        1.1014507,  1.1014507,  1.1014507,  1.1014507,  1.2850258,
        1.2850258,  1.2850258,  1.2850258,  1.2850258, -1.468601 ,
       -1.468601 ], dtype=float32), 'time': 2.53, 'frameNumber': 28}, {'numObj': 25, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00824079,
       -0.78287464,  0.        ,  0.3658909 ,  0.        ,  0.3757798 ,
        0.        ,  0.38566875,  0.        ,  0.3955577 ,  0.        ,
        0.        ,  0.03543538,  0.        ,  0.        , -0.15080637],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479,
       1.0609511 , 0.975709  , 0.90450644, 1.0020795 , 0.9289525 ,
       1.02845   , 0.9533987 , 1.0548205 , 0.9778448 , 1.0811911 ,
       1.1075616 , 1.1333783 , 1.1603026 , 1.1866732 , 1.6015167 ],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  1.2850258 ,  1.2850258 ,  1.2850258 ,  1.2850258 ,
        1.2850258 ,  1.2850258 ,  1.2850258 ,  1.2850258 ,  1.2850258 ,
        1.2850258 ,  1.2850258 ,  1.2850258 ,  1.2850258 , -0.91787565],
      dtype=float32), 'time': 2.635, 'frameNumber': 29}, {'numObj': 25, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.07004668,  0.00824079,
       -0.42852086, -0.43923387, -0.44994688, -0.4960953 ,  0.13597296,
       -0.19036216,  0.14009336, -0.22414938, -0.230742  , -0.23733462,
       -0.27441818, -0.28183484, -0.2571125 , -0.26370513, -0.27029777],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11170749, 0.13159479,
       0.9638549 , 0.9879513 , 1.0120476 , 1.0196526 , 0.85953844,
       0.8491509 , 0.88558507, 0.8681268 , 0.8936599 , 0.919193  ,
       0.93632406, 0.96163005, 0.99579245, 1.0213256 , 1.0468588 ],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.36715025,  0.36715025,  0.36715025,  0.36715025, -1.2850258 ,
       -1.2850258 , -1.2850258 , -1.2850258 , -1.1014507 , -1.1014507 ,
       -1.1014507 , -1.1014507 , -1.1014507 , -1.1014507 , -1.1014507 ],
      dtype=float32), 'time': 2.738, 'frameNumber': 30}, {'numObj': 23, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00412039,
       -0.2076678 , -0.21343635, -0.21920489,  0.0692226 , -0.23074201,
        0.09559312, -0.21508451,  0.09888943, -0.56202155, -0.5801513 ,
       -0.598281  , -0.6164108 , -0.20189925], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13178816,
       0.9263464 , 0.9520783 , 0.9778101 , 0.73512244, 0.701395  ,
       0.75874686, 0.73387563, 0.7849105 , 0.5936455 , 0.61279535,
       0.63194525, 0.6510951 , 0.90061456], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
       -1.1014507 , -1.1014507 , -1.1014507 , -0.91787565, -0.91787565,
       -0.91787565, -0.91787565, -0.91787565, -0.91787565, -0.91787565,
       -0.91787565, -0.91787565, -0.91787565], dtype=float32), 'time': 2.842, 'frameNumber': 31}, {'numObj': 26, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.07004668,  0.00824079,
       -0.5801513 , -0.57108647, -0.6164108 , -0.2801867 ,  0.06180589,
       -0.20601964,  0.06427813, -0.23568647,  0.06675036, -0.22250122,
        0.0692226 , -0.2768904 , -0.2076678 , -0.2389828 , -0.24722356,
       -0.22991791], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11170749, 0.13159479,
       0.61279535, 0.65662414, 0.6510951 , 0.85169387, 0.65635926,
       0.6262455 , 0.6826137 , 0.6438517 , 0.708868  , 0.67634517,
       0.73512244, 0.6844914 , 0.7085696 , 0.7264448 , 0.7514945 ,
       0.7844877 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.36715025,  0.36715025,  0.36715025,  0.36715025, -0.7343005 ,
       -0.7343005 , -0.7343005 , -0.7343005 , -0.7343005 , -0.7343005 ,
       -0.7343005 , -0.7343005 , -0.36715025, -0.36715025, -0.36715025,
       -0.36715025], dtype=float32), 'time': 2.946, 'frameNumber': 32}, {'numObj': 31, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.07004668,  0.00824079,
       -0.78287464,  0.0922968 , -0.2768904 , -0.26700145,  0.40050218,
       -0.26288107,  0.02389828, -0.2966683 ,  0.02472236, -0.30655724,
        0.        , -0.34281668, -0.29007566, -0.35352972,  0.        ,
        0.01977789, -0.21755674,  0.02060196, -0.2266216 ,  0.        ,
       -0.23568647], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11170749, 0.13159479,
       1.0609511 , 0.73258317, 0.6844914 , 0.66004527, 0.5886829 ,
       0.7181423 , 0.76437145, 0.73338354, 0.790729  , 0.7578297 ,
       0.8174859 , 0.77108395, 0.79243284, 0.7951803 , 0.870227  ,
       0.63258326, 0.59432465, 0.65894085, 0.6190881 , 0.68563336,
       0.6438517 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
      dtype=float32), 'velocity': array([ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        , -0.7343005 , -0.7343005 , -0.55072534, -0.55072534,
       -0.55072534, -0.55072534, -0.55072534, -0.55072534, -0.55072534,
       -0.55072534, -0.55072534, -0.55072534, -0.55072534, -0.55072534,
       -0.36715025, -0.36715025, -0.36715025, -0.36715025, -0.36715025,
       -0.36715025], dtype=float32), 'time': 3.05, 'frameNumber': 33}, {'numObj': 16, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00824079,
       -0.78287464, -0.22744569, -0.23733464, -0.24722356, -0.2571125 ,
       -0.26700145], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479,
       1.0609511 , 0.5622608 , 0.58670694, 0.611153  , 0.63559914,
       0.66004527], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
      dtype=float32), 'velocity': array([ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        , -0.55072534, -0.55072534, -0.55072534, -0.55072534,
       -0.55072534], dtype=float32), 'time': 3.154, 'frameNumber': 34}, {'numObj': 15, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00824079,
       -0.78287464, -0.21755674, -0.22744569, -0.25711253, -0.2678255 ],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479,
       1.0609511 , 0.5378147 , 0.5622608 , 0.578313  , 0.6024093 ],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
      dtype=float32), 'velocity': array([ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        , -0.36715025, -0.36715025, -0.36715025, -0.18357512],
      dtype=float32), 'time': 3.207, 'frameNumber': 35}, {'numObj': 11, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00824079,
       -0.78287464], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479,
       1.0609511 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 3.311, 'frameNumber': 36}, {'numObj': 12, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00824079,
       -0.27194592, -0.28430712], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479,
       0.5124656 , 0.53575945], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
       -0.18357512, -0.18357512], dtype=float32), 'time': 3.415, 'frameNumber': 37}, {'numObj': 11, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00824079,
       -0.78287464], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479,
       1.0609511 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 3.52, 'frameNumber': 38}, {'numObj': 12, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00412039,
       -0.30326092, -0.3164462 ], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13178816,
       0.5252633 , 0.5481009 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.36715025, 0.36715025], dtype=float32), 'time': 3.623, 'frameNumber': 39}, {'numObj': 10, 'x': array([0.01318526, 0.        , 0.02637051, 0.        , 0.03955577,
       0.        , 0.05274103, 0.00329631, 0.06592628, 0.00824079],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 3.728, 'frameNumber': 40}, {'numObj': 11, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.07004668,  0.00412039,
       -0.78287464], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11170749, 0.13178816,
       1.0609511 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 3.832, 'frameNumber': 41}, {'numObj': 10, 'x': array([0.01318526, 0.        , 0.02637051, 0.        , 0.03955577,
       0.        , 0.05274103, 0.00329631, 0.06592628, 0.00824079],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 3.936, 'frameNumber': 42}, {'numObj': 11, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00824079,
       -0.78287464], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479,
       1.0609511 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 4.04, 'frameNumber': 43}, {'numObj': 10, 'x': array([0.01318526, 0.        , 0.02637051, 0.        , 0.03955577,
       0.        , 0.05274103, 0.00329631, 0.06592628, 0.00412039],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13178816],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 4.144, 'frameNumber': 44}, {'numObj': 10, 'x': array([0.01318526, 0.        , 0.02637051, 0.        , 0.03955577,
       0.        , 0.05274103, 0.00329631, 0.06592628, 0.00412039],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13178816],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 4.248, 'frameNumber': 45}, {'numObj': 11, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.07004668,  0.00412039,
       -0.78287464], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11170749, 0.13178816,
       1.0609511 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 4.352, 'frameNumber': 46}, {'numObj': 10, 'x': array([0.        , 0.01318526, 0.02637051, 0.        , 0.03955577,
       0.        , 0.05274103, 0.00329631, 0.06592628, 0.00412039],
      dtype=float32), 'y': array([0.02637051, 0.02283753, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13178816],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 4.404, 'frameNumber': 47}, {'numObj': 12, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00824079,
       -0.78287464, -0.42192823], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13159479,
       1.0609511 , 0.7308011 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        , -0.18357512], dtype=float32), 'time': 4.51, 'frameNumber': 48}, {'numObj': 10, 'x': array([0.01318526, 0.        , 0.02637051, 0.        , 0.03955577,
       0.        , 0.05274103, 0.00329631, 0.07004668, 0.00412039],
      dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11170749, 0.13178816],
      dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 4.613, 'frameNumber': 49}, {'numObj': 11, 'x': array([ 0.01318526,  0.        ,  0.02637051,  0.        ,  0.03955577,
        0.        ,  0.05274103,  0.00329631,  0.06592628,  0.00412039,
       -0.78287464], dtype=float32), 'y': array([0.02283753, 0.02637051, 0.04567507, 0.05274103, 0.06851261,
       0.07911155, 0.09135014, 0.10543054, 0.11418767, 0.13178816,
       1.0609511 ], dtype=float32), 'z': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'velocity': array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), 'time': 4.718, 'frameNumber': 50}]
