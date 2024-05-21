# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"7B0B000","system":"readv2"},{"code":"7B17100","system":"readv2"},{"code":"7B0B.11","system":"readv2"},{"code":"4G8Z.00","system":"readv2"},{"code":"4G41.00","system":"readv2"},{"code":"4G8..00","system":"readv2"},{"code":"7B42400","system":"readv2"},{"code":"K12..12","system":"readv2"},{"code":"7B29400","system":"readv2"},{"code":"7B17111","system":"readv2"},{"code":"K14y.00","system":"readv2"},{"code":"7B05000","system":"readv2"},{"code":"K120.00","system":"readv2"},{"code":"7B17011","system":"readv2"},{"code":"4G7..00","system":"readv2"},{"code":"Kyu3100","system":"readv2"},{"code":"7B07211","system":"readv2"},{"code":"K12z.00","system":"readv2"},{"code":"K14z.00","system":"readv2"},{"code":"K100600","system":"readv2"},{"code":"7B1Cy00","system":"readv2"},{"code":"K120.12","system":"readv2"},{"code":"7B18000","system":"readv2"},{"code":"K121.11","system":"readv2"},{"code":"7B07200","system":"readv2"},{"code":"7B07.12","system":"readv2"},{"code":"7B07.11","system":"readv2"},{"code":"7B0Bz00","system":"readv2"},{"code":"7B18.00","system":"readv2"},{"code":"4G6..00","system":"readv2"},{"code":"K140z00","system":"readv2"},{"code":"7B42300","system":"readv2"},{"code":"7B18100","system":"readv2"},{"code":"4G44.00","system":"readv2"},{"code":"7B19100","system":"readv2"},{"code":"7B19y00","system":"readv2"},{"code":"7B19000","system":"readv2"},{"code":"K140100","system":"readv2"},{"code":"7B18011","system":"readv2"},{"code":"K140000","system":"readv2"},{"code":"Kyu3000","system":"readv2"},{"code":"K14..00","system":"readv2"},{"code":"7B1C.00","system":"readv2"},{"code":"K12..11","system":"readv2"},{"code":"7B25000","system":"readv2"},{"code":"K120z00","system":"readv2"},{"code":"7B1C000","system":"readv2"},{"code":"7B0By00","system":"readv2"},{"code":"K1A..00","system":"readv2"},{"code":"7B29100","system":"readv2"},{"code":"7B19200","system":"readv2"},{"code":"4G43.00","system":"readv2"},{"code":"K141.00","system":"readv2"},{"code":"7B43900","system":"readv2"},{"code":"7B17200","system":"readv2"},{"code":"7B18200","system":"readv2"},{"code":"K120000","system":"readv2"},{"code":"7B1Cz00","system":"readv2"},{"code":"7B19z00","system":"readv2"},{"code":"7B17000","system":"readv2"},{"code":"7B19.00","system":"readv2"},{"code":"7B0B.00","system":"readv2"},{"code":"K140.00","system":"readv2"},{"code":"4G4..00","system":"readv2"},{"code":"7B07400","system":"readv2"},{"code":"N20.0","system":"readv2"},{"code":"N21.0","system":"readv2"},{"code":"N22.8","system":"readv2"},{"code":"N21.9","system":"readv2"},{"code":"N21.1","system":"readv2"},{"code":"N20.9","system":"readv2"},{"code":"N21.8","system":"readv2"},{"code":"M09.4","system":"readv2"},{"code":"M39.1","system":"readv2"},{"code":"M44.2","system":"readv2"},{"code":"M14.1","system":"readv2"},{"code":"M06.1","system":"readv2"},{"code":"M14.9","system":"readv2"},{"code":"M75.4","system":"readv2"},{"code":"M14","system":"readv2"},{"code":"M14.8","system":"readv2"},{"code":"M09.3","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('urolithiasis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["calculous-urolithiasis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["calculous-urolithiasis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["calculous-urolithiasis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
