import glob
import os

filepath = 'path/to/file/*.csv'

# Looks under the data folder for .csv files
for filename in glob.glob(filepath):
    fin = open(filename)

    # Check if need to remove delimiter from end of each line
    print('Checking {}'.format(filename))
    line = fin.readline()

    # Delimiter '|' has already been removed before, can continue to next file
    if line[-2] != '|':
        fin.close()
        continue

    # Create a new temp file to write to
    fout = open(filename + '.tmp', 'w')

    # Reset file pointer to start of file
    fin.seek(0)

    # Remove delimiter from the end of each line
    print('Cleaning {}'.format(filename))
    for line in fin:
        fout.write(line[:-2] + '\n')
    
    fout.close()
    fin.close()

    # Replace old file with new file
    os.remove(filename)
    os.rename(filename + '.tmp', filename)