import numpy as np
import matplotlib.pyplot as plt
import re as r
import easyocr
#import os
#os.environ['KMP_DUPLICATE_LIB_OK']='True'

re = easyocr.Reader(['en'])
#pl = []
chk = []
a = ''
a1 = ''

#pl = []
#sym = ['{', ']', '[', '}']


class get_number_plate:

    def get_bboxes_from(self, output):
        """ returns list of bboxes """
        return output["instances"].__dict__['_fields']['pred_boxes'].__dict__['tensor']

    def crop(self, bbox, in_img):
        """ bbox is a list with xmin, ymin, xmax, ymax """
        xmin, ymin, xmax, ymax = bbox
        cropped_im = in_img[int(ymin):int(ymax), int(xmin):int(xmax)]
        return cropped_im

    def ocr(self, imm):
        op = re.readtext(imm, add_margin=0.1, canvas_size=960000)
        # stt = []
        for i in range(len(op)):
            for j in range(len(op[i])):
                if type(op[i][j]) == str:
                    return (op[i][j].replace(" ", ""))
   
    def remove_un(self, arr):
        pl = []
        sym = ['{', ']', '[', '}','.']
        arr = list(arr)
        
        for m in arr:
            if '.' in m:
                arr.remove('.')

        arr = ''.join(arr)
        #print(arr)
        
        '''
        for j in arr:
            if len(j) == 10 or len(j) >= 9:
                for p in j:
                    #pl.append(p)
                    print(p)
        '''
        if len(arr) == 10 or len(arr) >= 9:
            arr = list(arr)
        
        #print(arr)


        for j in arr:
            if j in sym:
                arr.remove(j)
        arr = (''.join(arr))
        #print (arr)
        return arr

    def get_num_plate(self, lis):

        print(lis)
        #pl = []
        sta = ['AP','AR','AS','BR','CG','GA','GJ','HR' ,'HP' ,'JK','JH','KA','KL','MP','MH','MN','ML','MZ','NL' ,'OD','PB' ,'RJ','SK','TN','TS','TR','UA','UK','UP','WB','AN','CH','DN','DD','DL' ,'LD','PY']
        opp = []
        #sym = ['{', ']', '[', '}']
        print(lis)
        for p in range(len(lis)):
            #print(lis[p])
            pl1 = self.remove_un(lis[p])
            #print(pl1)
            pattern_1 = r.compile(r'\w\w\d\d\w\w\d\d\d\d')
            pattern_2 = r.compile(r'\w\w\d\d\w\d\d\d\d')

            global a

            if r.search(pattern_1, pl1) or r.search(pattern_2, pl1):

                a = 'pattern matched!!'
            else:
                a = 'pattern not matched!!'
                global a1
                a1 = pl1
                #print(a1)
            
            for p in sta:
                if p == pl1[:2].upper():
                #print('correct state')
                    opp.append(pl1.upper())
        
        
        print(opp)
        try:
            opp.remove(a1)
        except Exception as e:
            print(' ')

        #print(set(opp))
        return set(opp)
       

        
        '''
        for i in lis:

            if len(i) == 10 or len(i) >= 9:

                for p in i:
                    pl.append(p)
        
     
        for j in pl:
            if j in sym:
                pl.remove(j)
        pl1 = (''.join(pl))

        print(pl)
       
   
        pattern_1 = r.compile(r'\w\w\d\d\w\w\d\d\d\d')
        pattern_2 = r.compile(r'\w\w\d\d\w\d\d\d\d')
        global a
        if r.search(pattern_1, pl1) or r.search(pattern_2, pl1):

            a = 'pattern matched!!'
        else:
            a = 'pattern not matched!!'

        sta = ['AP','AR','AS','BR','CG','GA','GJ','HR' ,'HP' ,'JK','JH','KA','KL','MP','MH','MN','ML','MZ','NL' ,'OD','PB' ,'RJ','SK','TN','TS','TR','UA','UK','UP','WB','AN','CH','DN','DD','DL' ,'LD','PY']
        

        for p in sta:
            if p == pl1[:2].upper():
                #print('correct state')
                return pl1.upper(), a
         ''' 
            

        
            
        
    
        
        

    def disp(self, im):
        oc = self.ocr(im)
        plt.imshow(im)
        plt.show()
        plt.close()
        return oc

    def run_easy_ocr(self, output, im):
        bboxes = self.get_bboxes_from(output)
        # print(bboxes)
        for bbox in bboxes:
            crop_im = self.crop(bbox, in_img=im)
            # display cropped image
            ocr_op = self.disp(crop_im)
            chk.append(ocr_op)
        nump = self.get_num_plate(chk)
        print(nump)
        return nump

