""" 3.15 LAB: Musical note frequencies

On a piano, a key has a frequency, say f0. Each higher key (black or white) has a frequency of f0 * r^n, where
n is the distance (number of keys) from that key and r is 2(1^12).

Given an initial key frequency, output that frequency and the next 3 higher key frequencies

Output each floating-point value with two digits after the decimal point, then the units ("Hz"), 
then a newline, using the following statement: print(f'{your_value:.2f} Hz')

"""
import math

initial_key_frequency = float(input('Input note frequency:\n'))

higher_key_1 = initial_key_frequency * (math.pow(2, (1/12)))
higher_key_2 = higher_key_1 * (math.pow(2, (1/12)))
higher_key_3 = higher_key_2 * (math.pow(2, (1/12)))

print(f'{initial_key_frequency:.2f} Hz\n{higher_key_1:.2f} Hz\n{higher_key_2:.2f} Hz\n{higher_key_3:.2f} Hz')