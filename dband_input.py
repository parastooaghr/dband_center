#Creates dband.in file from PDOS result.
all_files = os.listdir('./')
dband_filename = 'CuNi_dband.in'
dband_file = open('./' + dband_filename, 'w')
for filename in all_files:
    if 'PDOS.pdos_atm#' in filename and '(d)' in filename:
        dband_file.write(filename + '\n')
dband_file.close()
        
