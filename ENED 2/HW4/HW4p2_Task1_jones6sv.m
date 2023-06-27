% Activity Hw4p2: 
% File: HW4p2_Task1_jones6sv
% Date: 1 January 2019
% By: Steven Paul Jones II (jones6sv)
%
% Section: 017
% Team: 242
%
% ELECTRONIC SIGNATURE 
% Steven Paul Jones II
%
% The electronic signature above indicates the script
% submitted for evaluation is my individual work, and I
% have a general understanding of all aspects of its
% development and execution.
%
% prompts the user for the total number 
% (n) of bolts, the mean (𝒙̅) length of the sample of bolts, and the sample standard deviation (s). Your script 
% will then ask the user to enter the length of a random bolt from the sample. Your script will determine the 
% quality of the bolt based on the corresponding z-value (z = (𝒙-𝒙̅) /s, x is the length of a bolt, s is the sample 
% standard deviation, and 𝒙̅ is the sample mean). 
n = input('Enter the total number of bolts: ');
x_bar = input('Enter the mean length of the sample of bolts: ');
s = input('Enter the sample standard deviation: ');
x = input('Enter the length of a random bolt from the sample: ');
z = (x-x_bar)/s;
if z >= -1 && z <= 1
    disp('SUPERIOR');
elseif z > 1 && z <= 2 || z > -1 && z <= -2
    disp('PREMIUM QUALITY');
elseif z > 2 && z <= 3 || z > -2 && z <= -3
    disp('BAD QUALITY');
else
    disp('POOR');
end