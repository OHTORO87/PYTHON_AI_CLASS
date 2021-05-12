import  openpyxl as xl

exf = xl.load_workbook('c:\\dd\\ess.xlsx')

aws = exf.active
#엑셀의 자료를 불러오기
for i in aws.rows:
    index = i[0].row
    name = i[0].value
    kor = i[1].value
    eng = i[2].value
    mat = i[3].value
#불러온 자료를 수정하기
    tot = kor + eng + mat
    avg = tot / 3
    
    aws.cell(row = index, column = 5).value = tot
    aws.cell(row = index, column = 6).value = avg


    print('{} {} {} {} {} {:.2f} '.format(name, kor, eng, mat, tot, avg))
#수정된 값을 엑셀로 출력
exf.save('c:\\dd\\outss.xlsx')
exf.close()