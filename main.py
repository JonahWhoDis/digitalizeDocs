import os
import shutil
from re import search
import PyPDF4
import json
import Pillow

def save_file_temp (file,category, date):
    destination = "public/temp"
    shutil.move("scans/"+file, "public/temp/"+category+"_"+date+".pdf")
    print("save_file")


def get_cat_and_date(file_list):
    # define keyterms
    Rechnung = "Rechnung"
    Angebot = "Angebot"
    for file in file_list:
        pdfFileObj = open("scans/"+file, 'rb')
        # open the pdf file
        object = PyPDF4.PdfFileReader(pdfFileObj)
        # extract text and do the search
        text = object.getPage(0).extractText()
        # print(Text)
        print (text)
        category_R = search(Rechnung, text)
        catergory_A = search(Angebot, text)
        if category_R == "Rechnung":
            date = search(r'\d{2}-\d{2}-\d{4}', text)
            print("Rechnung")
            save_file_temp(file,category_R,date)
            return
        if catergory_A == "Angebot":
            date = search(r'\d{2}-\d{2}-\d{4}', text)
            save_file_temp(file, catergory_A, date)


def get_temp_files():

    list = []
    for file in os.listdir("public/temp"):

        list.append(
            {
                "project": "Projekt A",
                "company": "Peter baut Tief",
                "filepath": "Test.pdf",
                "category": "Rechnung",
                "date": "02-02-2021"
            }
        )


    return list


def set_companies(company_name):
    f = open('companies.json', )
    data = json.load(f)
    data.append(company_name)
    with open('companies.json', "w") as company:
        json.dump(data, company)


def get_companies():
    f = open('companies.json', )
    data = json.load(f)
    f.close()
    return data


def set_projects(project_name):
    f = open('projects.json', )
    data = json.load(f)
    data.append(project_name)
    with open('projects.json', "w") as project:
        json.dump(data, project)


def get_projects():
    f = open('projects.json', )
    data = json.load(f)
    f.close()
    return data


def read_files():
    # Folder scan
    path = "scans"
    dirs = os.listdir(path)
    dirs.sort()
    file_list = []
    # Liste an zu kontrollierenden Files erstellen
    for file in dirs:
        if file.endswith('.pdf'):
            file_list.append(file)
    print(file_list)
    return file_list


if __name__ == "__main__":
    file_list=read_files()
    get_cat_and_date(file_list)
