import re

test_input_stream = '1001010000'


def convert_to_ami_form(input_stream):
    pass


# NRZ-Inverted

def nrz_inverted(input_stream):
    output = []
    for i in range(1, len(input_stream)):
        if input_stream[i] == '1':
            try:
                if output[i - 1] == 'high':
                    output[i] = 'low'
                else:
                    output[i] = 'high'
            except IndexError:
                continue
        else:
            try:
                output[i] = output[i - 1]
            except IndexError:
                continue
    return output


# Bipolar AMI

def bipolar_ami(input_stream):
    output = []
    previous = None
    for i in range(1, len(input_stream)):
        if input_stream[i] == 1:
            if previous == 'low':
                output[i] = 'high'
            else:
                output[i] = 'low'
                previous = 'low'
        else:
            output[i] = 'neutral'
    return output


# Pseudoternary

def pseudoternary(input_stream):
    output = []
    previous = None
    for i in range(1, len(input_stream)):
        if input[i] == 0:
            if previous == 'low':
                output[i] = 'high'
                previous = 'high'
            else:
                output[i] = 'low'
                previous = 'low'
        else:
            output[i] = 'neutral'


# Manchester
def manchester(input_stream):
    output = []
    for i in range(1, len(input_stream)):
        if input_stream[i] == 1:
            output[2 * i - 1] = 'low'
            output[2 * i] = 'high'
        else:
            output[2 * i - 1] = 'high'
            output[2 * i] = 'low'


# Differential Manchester
def differential_manchester(input_stream):
    output = ''
    for i in range(1, len(output)):
        if output[i] == 1:
            output[1] = 'high'
            output[2] = 'low'
        else:
            output[1] = 'low'
            output[2] = 'high'
            for i in range(2, len(input_stream)):
                if (input(i) == 1):
                    output[2 * i - 1] = output(2 * i - 2);
                    output[2 * i] = output(2 * i - 3)
                else:
                    output[2 * i - 1] = output(2 * i - 3);
                    output[2 * i] = output(2 * i - 2)


# If bit = ‘0’, transition at the beginning and wait for time T/2.
# Else if bit = ‘1’, do not transition and wait for time T/2
# Transition for clock (at the middle of each bit in every cycle).
# Wait for time T/2.
# Repeat step 1 to 4 again.


def B8ZS(input_stream):
    convert_to_ami_form(input_stream)
    for i in range(1, len(input_stream)):
        pass


# for (i = 1 to inputStream.length()) {
# Convert it to Alternate Mark Inversion (AMI) form
# If octet of all zeros and last voltage pulse preceding was positive encode as 000+-0-+
# If octet of all zeros and last voltage pulse preceding was negative encode as 000-+0+-

# HDB3 from NRZ-L
def HDB3_from_NRZL(input_stream):
    convert_to_ami_form(input_stream)
    if re.search('0000', input_stream):
        beginning_of_zeroes = re.search('0000', input_stream).regs[0][0]
        # if odd number of + and -:
        slice_before_zeroes = input_stream[:beginning_of_zeroes]
        if (slice_before_zeroes.count('+') + slice_before_zeroes.count('-')) % 2 != 0:
            input_stream.replace(input_stream, 'B00V')
        else:
            input_stream.replace(input_stream, '000V')


HDB3_from_NRZL(test_input_stream)

# Get the signal
# Convert it to Alternate Mark Inversion (AMI) form
# Look for 4 consecutive zeros and replace them with either 000V or B00V, Rule: If number of + and – at the lefthand
# side of the consecutive 4 zeros is odd then use B00V else 000V
# If it is 000V then V polarity should be as same as the polarity of the preceding pulse of those 4 consecutive zeros.
# If it is B00V, B and V are in same polarity but opposite to the preceding pulse of those 4 consecutive zeros.
