#Reading Tags 
import pydicom
ds = pydicom.read_file("ttfm.dcm")
bs = pydicom.read_file("bmode.dcm")

#Saving Tags 
dtags = list(ds.keys())
btags = list(bs.keys())


#Converting To String
str1 = ''.join(str(e) for e in dtags)


#Writing It Into File
f = open("SAVE_TAGS1.txt", "w")
f.write(str1)

f.close()
