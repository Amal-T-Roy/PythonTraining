import pickle

def Read():
    with open('File.bin','rb+') as f:
        Continue = True
        while Continue == True:
                try:
                    pickle.dump(['Hi','Bro'],f)
                    row = pickle.load(f)
                    print(row)
                except Exception as e:
                    print(e.__doc__)
                    Continue = False