from jwt import encode, decode

def create_token(data:dict):
    token =  encode(payload=data, key="toor_not_upload_to_git", algorithm="HS256")
    return token

def validate_token(token:str)->dict:
    data:dict = decode(token,key="toor_not_upload_to_git", algorithm=["HS256"])
    return data

