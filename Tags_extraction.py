
# coding: utf-8

# In[26]:


import pydicom
ds = pydicom.read_file("ttfm.dcm")
bs = pydicom.read_file("bmode.dcm")


dtags = list(ds.keys())
btags = list(bs.keys())


# In[4]:


# import re
# ds = "(0012,0012)\n(0013,0013)" 
# dicomTagExp = re.compile(r"\(([0-9a-fA-F]{4})\W*,\W*([0-9a-fA-F]{4})\)")
# for match in dicomTagExp.finditer(ds):
#   dTag = match.groups()
#   print(dTag)


# In[28]:


str1 = ''.join(str(e) for e in dtags)

f = open("SAVE_TAGS1.txt", "w")

f.write(str1)

f.close()


# In[29]:


str2 = ''.join(str(e) for e in btags)

f = open("SAVE_TAGS2.txt", "w")

f.write(str2)

f.close()

