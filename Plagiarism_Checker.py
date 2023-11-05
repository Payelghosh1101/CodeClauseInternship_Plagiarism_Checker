from difflib import SequenceMatcher

with open('1st_file.txt') as file1, open('2nd_file.txt') as file2:
     
     file1_Data = file1.read()
     file2_Data = file2.read()

     similar = SequenceMatcher(None, file1_Data, file2_Data).ratio()

     result = int(similar * 100)

     print(f"\n{result}% Plagarized Content\n")
