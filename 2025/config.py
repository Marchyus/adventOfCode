import os
import re
from pathlib import Path


def get_inputs(file_path):
    #current_file_name = __file__.replace("\\", "/").split("/")[-1]
    # Get current day
    current_file_name = os.path.basename(file_path)
    current_day = ''.join(re.findall(r'\d+', current_file_name))

    if not current_day:
        return {'success': False, 'message': 'No numbers in file name'}
    
    # check if files exist, if not - create
    base_dir = os.path.dirname(os.path.abspath(__file__))

    part_a_filename = f'day{current_day}_a.txt'
    part_a_test_filename = f'day{current_day}_a_test.txt'
    part_b_filename = f'day{current_day}_b.txt'
    part_b_test_filename = f'day{current_day}_b_test.txt'

    part_a_filepath = os.path.join(base_dir, 'inputs', part_a_filename)
    part_a_test_filepath = os.path.join(base_dir, 'inputs', part_a_test_filename)
    part_b_filepath = os.path.join(base_dir, 'inputs', part_b_filename)
    part_b_test_filepath = os.path.join(base_dir, 'inputs', part_b_test_filename)

    if not os.path.exists(part_a_filepath):
        open(part_a_filepath, 'a').close()
    if not os.path.exists(part_a_test_filepath):
        open(part_a_test_filepath, 'a').close()
    if not os.path.exists(part_b_filepath):
        open(part_b_filepath, 'a').close()
    if not os.path.exists(part_b_test_filepath):
        open(part_b_test_filepath, 'a').close()

    # Read inputs
    part_a = Path(part_a_filepath).read_text().splitlines()
    part_a_test = Path(part_a_test_filepath).read_text().splitlines()
    part_b = Path(part_b_filepath).read_text().splitlines()
    part_b_test = Path(part_b_test_filepath).read_text().splitlines()  


    # return findings
    return {
        'success': True, 
        'part_a': part_a,
        'part_b': part_b,
        'part_a_test': part_a_test,
        'part_b_test': part_b_test
        }
        

if (__name__ == '__main__'):
    print(get_inputs(__file__))