y = 1
while True:
    if y == 1:
        print('********************************************************************************')
        print('********************************************************************************')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                 << ชนิดน้ำมัน >>                              **')
        print('**                                                                            **')
        print('**                                1.GASOLINE 95                               **')
        print('**                                2.GASOLINE 91                               **')
        print('**                                3.GASOHOL 91                                **')
        print('**                                4.Gasohol E20                               **')
        print('**                                5.GASOHOL 95                                **')
        print('**                                6.DIESEL                                    **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('********************************************************************************')
        print('********************************************************************************')

        b = str((input('เลือกน้ำมันจาก 1-6 : ')))
        while not(b in ['1', '2', '3', '4', '5', '6']):
            b = str(input('เลือกไหม่ : '))
        print('********************************************************************************')
        print('********************************************************************************')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                          << เลือกใช้งานฟังก์ชั่น >>                              **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                              1.เงินเป้นลิตร                                   **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                              2.ลิตรเป็นเงิน                                   **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('********************************************************************************')
        print('********************************************************************************')
        c = (input('เลือกใช้งานฟังก์ชั่น 1-2 : '))
        if '1' in c:
            g1 = input('เลือกจำนวนเงิน :  ')
            m1 = float(g1)
        elif '2' in c:
            g2 = input('เลือกจำนวนลิตร : ')
            m2 = float(g2)
        else:
            print(" Please try again ")
        k = 0
        if '1' in c:
            if '1' in b:
                k = k + (m1 / 29.15)
                print('Ans', '%.2f' % k, 'ลิตร')
            elif '2' in b:
                k = k + (m1 / 25.30)
                print('Ans', '%.2f' % k, 'ลิตร')
            elif '3' in b:
                k = k + (m1 / 21.68)
                print('Ans', '%.2f' % k, 'ลิตร')
            elif '4' in b:
                k = k + (m1 / 20.2)
                print('Ans', '%.2f' % k, 'ลิตร')
            elif '5' in b:
                k = k + (m1 / 21.2)
                print('Ans', '%.2f' % k, 'ลิตร')
            elif '6' in b:
                k = k + (m1 / 21.1)
                print('Ans', '%.2f' % k, 'ลิตร')
            else:
                print('Invalid information, please Enter again.')
        elif '2' in c:
            if '1' in c:
                k = k + (m2 * 29.15)
                print('ราคาน้ำมัม =', k, 'บาท')
            elif '2' in c:
                k = k + (m2 * 25.30)
                print('ราคาน้ำมัน =', k, 'บาท')
            elif '3' in c:
                k = k + (m2 * 21.68)
                print('ราคา น้ำมัน =', k, 'บาท')
            elif '4' in c:
                k = k + (m2 * 20.2)
                print('ราคา น้ำมัน =', k, 'บาท')
            elif '5' in c:
                k = k + (m2 * 21.2)
                print('ราคา น้ำมัน =', k, 'บาท')
            elif '6' in c:
                k = k + (m2 * 21.1)
                print('ราคา น้ำมัน =', k, 'บาท')
            else:
                print('Invalid information, please Enter again.')

        x = int(
            input("1) กด 1 เพื่อเริ่มฟังก์ชั่นใหม่  ,  2)กด 0 เพื่อออกจากระบบ :"))
        y = x
    elif y == 0:
        print('********************************************************************************')
        print('********************************************************************************')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                 THANK YOU                                  **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('********************************************************************************')
        print('********************************************************************************')

        break
