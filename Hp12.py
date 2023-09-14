sn=input("Enter season:")
ch1=['September','september','October','october','November','november']
ch2=['December','december','January','january','February','february']
ch3=['March','march','April','april','May','may']
if sn in ch1:
    print(sn,"is the Autumn season")
elif sn in ch2:
    print(sn,"is the Winter season")
elif sn in ch3:
    print(sn,"is the Spring season")
else:
    print(sn,"is the Summer season")
