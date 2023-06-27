% Activity Hw4p2: 
% File: HW4p2_Task2_jones6sv
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
% A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
%
% enter sample size
sample_size = (input("Enter sample size: "));
% is sigma known?
sigma_known = (input("Is sigma known? (y/n): "));
% if sigma is known
if sigma_known == 'y'
% enter sigma
    sigma = (input("Enter sigma: "));
% enter alpha
    alpha = (input("Enter alpha: "));
% enter Za/2
    Za2 = (input("Enter Za/2: "));
% calculate margin of error
    margin_of_error = Za2 * sigma / sqrt(sample_size);

% if sigma is unknown
elseif sigma_known == 'n'
% is normal distribution?
    normal_distribution = input("Is normal distribution? (y/n): ");

% if normal distribution
elseif normal_distribution == 'y'
% is sample size > 30?
elseif sample_size > 30
            % eneter s (sample standard deviation)
            s = (input("Enter s: "));
            % enter alpha
            alpha = (input("Enter alpha: "));
            % enter t(alpha/2, n-1)
            t_alpha2_n1 = (input("Enter t(alpha/2, n-1): "));
            % calculate margin of error
            margin_of_error = t_alpha2_n1 * s / sqrt(sample_size);
        
% if sample size < 30
        elseif sample_size < 30
            % enter sigma
            sigma = float(input("Enter sigma: "));
            % enter alpha
            alpha = float(input("Enter alpha: "));
            % enter Za/2
            Za2 = float(input("Enter Za/2: "));
            % calculate margin of error
            margin_of_error = Za2 * sigma / sqrt(sample_size);
            
% if not normal distribution
elseif normal_distribution == 'n'
        % This case is beyond the scope of this course
disp("This case is beyond the scope of this course")
end
mean = (input("Enter mean/ X bar: "));
XL = mean - margin_of_error;
XR = mean + margin_of_error;
display("XL = ", XL)
display("XR = ", XR)
