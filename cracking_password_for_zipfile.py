#import pwd


#num = []
#for x in range(0,10000):
 #   num.append("{0:04d}".format(x))
  #  print(num)

#with open("C:/Users/USER/Desktop/Python/YouTube/wordList.txt","w") as file:
 #   for pin in num:
  #      file.write(f"{pin}\n")

from tqdm import tqdm

import zipfile
        #the password list path you want use
wordlist = "C:/Users/USER/Desktop/Python/YouTube/wordList.txt"
        #the zip file you want to crack its password
zip_file = "C:/Users/USER/Desktop/MyZipFileForCracking/download (1).zip"
        # initialise the zipfile obect
zip_file = zipfile.ZipFile(zip_file)
        #count the number of words in the word list
n_words = len(list(open(wordlist,"rb")))
        #print the total number of passwords
print("total passwors to test: ", n_words)
with open(wordlist,"rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except Exception as e:
            print(f"tried {word.strip()}",e)
            continue
        else:
            print("[+] password found: ",word.decode().strip())
            exit(0)
        print("[!] password not found, try other wordlist. ")




