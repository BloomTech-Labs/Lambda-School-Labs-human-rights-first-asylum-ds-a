"""
Optical Character Recognition
"""

import os
os.environ["OMP_NUM_THREADS"]= '1'
os.environ["OMP_THREAD_LIMIT"] = '1'
os.environ["MKL_NUM_THREADS"] = '1'
os.environ["NUMEXPR_NUM_THREADS"] = '1'
os.environ["OMP_NUM_THREADS"] = '1'
os.environ["PAPERLESS_AVX2_AVAILABLE"]="false"
os.environ["OCR_THREADS"] = '1'

from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes
from fastapi import APIRouter, File
import sqlalchemy
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from PyPDF2 import PdfFileReader
from io import BytesIO


"""
This file will contain functions and other operations with regards to reading in PDF files, converting them to 
text, and returning that text to the API call

Further development should incorporate changes to move the OCR text into the next phase of the pipeline for 
extracting entities for saving into the DB.
"""


router = APIRouter()

load_dotenv(find_dotenv())
database_url = os.getenv('DATABASE_URL')


# "Could not parse rfc1738 URL from string" error | Needs to be fixed during DB integration
# engine = sqlalchemy.create_engine(database_url)

@router.post('/insert')
async def insertDoc(file: bytes = File(...)):
    '''
    This function inserts a PDF and the OCR converted text into a database

    '''
    text = ocr_func(file)
    # query = """INSERT INTO pdfs(pdf, plaintext) VALUES (%s, %s)""" 
    # vals = (file, text)
    # engine.execute(query, vals)
    # Return text as response
    return {'Text': text}


def ocr_func(pdfBytes: bytes = File(...), txt_folder: str = './temp/'):
    '''
    Takes an uploaded .pdf file, converts it to plain text, and saves it as a
    .txt file
    range slice size can be changed to put more images in memory, but provides 
    no speed boost, as the bottleneck is pytesseract.image_to_string
    '''
    fileReader = PdfFileReader(BytesIO(pdfBytes))
    maxPages = fileReader.numPages
    del fileReader
    fulltext = []
    for page in range(1, maxPages+1):
        pil_image = convert_from_bytes(pdfBytes, dpi=300, first_page=page,
                                            last_page=page, 
                                            fmt= 'jpg',
                                            thread_count=1, grayscale=True)
        fulltext += [str(pytesseract.image_to_string(image)) for image in pil_image]
        pil_image.clear()
    return (''.join(fulltext).split('\n\n'))
    
    # print('num pages', list(range(num_pages)))
    # for i in range(num_pages):
    #     filename = 'page_' + str(i) + '.jpg'
    #     print('fileName', filename)
        