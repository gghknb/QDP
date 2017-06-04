import csv



#엑셀 파일 열기
result1 = open("xgb_result.csv","r")
result2 = open("lstm_result.csv","r")
#result1 = open("sample_1.csv","r")
#result2 = open("sample_2.csv","r")
combine_result = open("combine_result.csv","w",newline="")

print("Open finish")
# initialize 
matrix1 = []
matrix2 = []
result_matrix = []
index = 0
index2 = 1
csvReader_xgb = csv.reader(result1)
csvReader_lstm = csv.reader(result2)
csvWriter_combine = csv.writer(combine_result)


print("Initialize finish")
# read 2 csv file data 
for lines in csvReader_xgb :
    if index is 0 :
        matrix1.append(lines[1])
    else :
        matrix1.append(float(lines[1]))
    index = index + 1
for lines in csvReader_lstm :
    if index2 is 1 :
        matrix2.append(lines[0])
    else :
        matrix2.append(float(lines[0]))
    index2 = index2 + 1

print("Read finish")

for i in range(0,index) : 
    if i is 0 :
        csvWriter_combine.writerow(["test_id","is_duplicate"])
    else :
        A = matrix1[i]
        B = matrix2[i]
        combine = (A * 1/2) + (B * 1/2)                          
        csvWriter_combine.writerow([i,combine])
print("Write finish")

result1.close()
result2.close()
combine_result.close()


