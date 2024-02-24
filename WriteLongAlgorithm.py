
index = 3
done = False


'''
elif index == 16:
            BBBSAppend.write(f"{i.text}\n")
        elif index < 32:
            BBBSAppend.write(f"{i.text},")
'''


while not done:
    if index ==25:
        done=True
    else:
        index+=1
        indexMult = index*16
        string1 = "{i.text}"
        string2 = r'\n'
        string3 = ","
        print(f'''elif index < {indexMult}:
    BBBSAppend.write(f"{string1}{string3}")
elif index == {indexMult}:
    BBBSAppend.write(f"{string1}{string2}")
              
              ''')
