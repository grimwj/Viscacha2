import glob, re

def new_level(thr: str, _k: float=0.35) -> float :
    '''
    Calculate the new starting level. 
    Function that take the threshold, subtracts this value for a constant k.
    '''
    # excel creates comma-separated values, so replace comma with dot
    threshold = float(thr.replace(",", "."))
    
    level = round(threshold - _k, 2)
    print(f'\nYour new starting level is: {level}.\n')
    
    return level

def replacer(new_lev: float, _path: str = '../shape_dots*.txt'):
    '''
    Walk to the behavioral folder and replace the values.
    '''
    folder_glob = glob.glob(_path)
    
    # walk throu each file and replace the threshold line
    for task in folder_glob:
        with open(task, 'r') as f:
            lines = f.readlines()
        
        with open(task, 'w') as f:
            for line in lines:
                new_line = re.sub(
                    r'^([ ]{4}|[\t])Start=0.[\d]{2}', 
                    f'   Start={new_lev}'.rjust(len(line)-1),
                    line
                )
                f.write(new_line)
                
    return
        
if __name__ == '__main__':
    '''
    |-----------------------------------------------------------------------------|
    | ASK FOR THE RESULTING THRESHOLD FROM ShapeBrt.txt AND REPLACE THE OLD       |
    | THRESHOLD IN STIMULI TEXT FILES                                             |
    |-----------------------------------------------------------------------------|
    '''
    # ask for new threshold
    comma_threshold = (input('Threshold here (EXCEL FORMAT! Comma separated values!): '))
    
    # call it
    replacer(new_level(comma_threshold))
    
    input('Press any key to quit.')
    