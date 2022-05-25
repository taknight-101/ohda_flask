
def robust_s_remove(text):
        text = text[::-1]
        ind = 0
        flag = False
        for index, i in enumerate(text):

            if i =='s' and index == 0 :
                ind = index

            elif i == 's' and (index - ind) == 1 :
                ind =    index

            elif i !='s' and index == 0 :
                flag = True
                text = text[::-1]
                print(text)
                break
        if flag :
            return

        # print("hi" , ind)
        ind = len(text) -1 - ind
        text = text[::-1]
        print(text[:ind])

robust_s_remove("hellossss")
robust_s_remove("sos")
robust_s_remove("ssoSSss")
robust_s_remove("esso")