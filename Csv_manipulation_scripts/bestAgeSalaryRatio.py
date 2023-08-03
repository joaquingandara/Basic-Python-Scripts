import camelot
import csv
#Pre: The pdf contains only one table.
def convertPdfToCsv(filePath,fileName):
    tables = camelot.read_pdf(filePath,flavor='stream') #flavor is specific because the table use does not have lines separating the rows.
    if tables.n != 1:
        print(f"Se detectaron {tables.n} tablas de {filePath}")
    else:
        tables[0].to_csv(f"{fileName}")

def bestSalaryAgeRatio(worker,worker_res):
    #Not clean way of taking out dolar sign and converting commas to dot.
    worker[5] = worker[5].replace("$",""); worker_res[5] = worker_res[5].replace("$","")
    workerRatio = float(worker[5].replace(",","")) / float(worker[3].replace(",",""))
    workerResRatio = float(worker_res[5].replace(",","")) / float(worker_res[3].replace(",",""))
    return True if workerRatio > workerResRatio else False 

def findYoungestHigestPaid(workers):
    next(workers) # Quick solution to increase iterator
    worker_res = next(workers)
    for worker in workers:
        if bestSalaryAgeRatio(worker,worker_res):
            worker_res = worker
    return worker_res

def processData():
    filePath = "workersInfo.pdf"; fileNameCsv = "workersInfo.csv"
    convertPdfToCsv(filePath,fileNameCsv)
    with open(fileNameCsv) as csv_file:
        workers= csv.reader(csv_file, delimiter=",") 
        worker_search = findYoungestHigestPaid(workers)
        print(f"{worker_search[0]} who works as a {worker_search[1]} has the best salary-age ratio with an age of {worker_search[3]} and a salary of ${worker_search[5]} usd per year")


if __name__ == "__main__":
    processData()
