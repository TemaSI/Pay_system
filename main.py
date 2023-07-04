from fastapi import FastAPI


app = FastAPI()


from business import business_api
from card_managment_transfer import card_api
from user_authentication import user_api

