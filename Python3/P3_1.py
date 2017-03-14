"""Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers."""
import re

txt_file = open('actualdata.txt', 'r')
all_lines = txt_file.readlines()
formatted_data = str(all_lines)
x = re.findall('[0-9]+', formatted_data)	
nums = list(map(int, x))
print (sum(nums))