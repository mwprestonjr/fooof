"""Test functions for FOOOF synth.transform"""

import numpy as np

from fooof.synth.gen import gen_power_spectrum
from fooof.synth.params import SynParams
from fooof.synth.transform import *

###################################################################################################
###################################################################################################

def test_rotate_spectrum():

    # Create a spectrum to use for test rotations
    freqs, spectrum = gen_power_spectrum([1, 100], [1, 1], [])

    # Check that rotation transforms the power spectrum
    rotated_spectrum = rotate_spectrum(freqs, spectrum, delta=0.5, f_rotation=25.)
    assert not np.all(rotated_spectrum == spectrum)

    # Check that 0 rotation returns the same spectrum
    rotated_spectrum = rotate_spectrum(freqs, spectrum, delta=0., f_rotation=25.)
    assert np.all(rotated_spectrum == spectrum)

def test_translate_spectrum():

    # Create a spectrum to use for test translation
    freqs, spectrum = gen_power_spectrum([1, 100], [1, 1], [])

    # Check that translation transforms the power spectrum
    translated_spectrum = translate_spectrum(spectrum, delta=1.)
    assert not np.all(translated_spectrum == spectrum)

    # Check that 0 translation returns the same spectrum
    translated_spectrum = translate_spectrum(spectrum, delta=0.)
    assert np.all(translated_spectrum == spectrum)

def test_rotate_syn_spectrum():

    syn_params = SynParams([1, 1], [10, 0.5, 1], 0)
    freqs, spectrum = gen_power_spectrum([3, 40], *syn_params)

    rotated_spectrum, new_syn_params = rotate_syn_spectrum(freqs, spectrum, 0.5, 20, syn_params)

    assert not np.all(rotated_spectrum == spectrum)
    assert new_syn_params.aperiodic_params[1] == 1.5

def test_translate_syn_spectrum():

    syn_params = SynParams([1, 1], [10, 0.5, 1], 0)
    freqs, spectrum = gen_power_spectrum([3, 40], *syn_params)

    translated_spectrum, new_syn_params = translate_syn_spectrum(spectrum, 0.5, syn_params)
    assert not np.all(translated_spectrum == spectrum)
    assert new_syn_params.aperiodic_params[0] == 1.5

def cal_rot_offset():

    assert calc_rot_offset(20, 0.5)
