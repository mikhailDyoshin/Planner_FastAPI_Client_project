import requests
from Client import Client

if __name__ == '__main__':

    email = 'myemail@gmail.com'
    password = '12345strong'

    client = Client()

    """ *********************** GET ALL *********************** """
    get_all_responce = client.get_all()
    get_all_status = get_all_responce['status']
    get_all_json = get_all_responce['json']

    print(f'GET_ALL:\nstatus: {get_all_status}\njson: {get_all_json}\n')

    IDs = [data['_id'] for data in get_all_json]
    print(IDs, '\n')


    """ *********************** GET SINGLE *********************** """
    if IDs:
        get_single_responce = client.get_single(IDs[0])

        get_single_status = get_single_responce['status']
        get_single_json = get_single_responce['json']

        print(f'GET_SINGLE:\nstatus: {get_single_status}\njson: {get_single_json}\n')


    """ *********************** SIGN UP *********************** """
    sign_up_responce = client.sign_up(email, password)
    sign_up_status = sign_up_responce['status']
    sign_up_json = sign_up_responce['json']

    print(f'SIGN_UP:\nstatus: {sign_up_status}\njson: {sign_up_json}\n')


    """ *********************** SIGN IN *********************** """
    sign_in_responce = client.sign_in(email, password)
    sign_in_status = sign_in_responce['status']
    sign_in_json = sign_in_responce['json']

    token = sign_in_json['access_token']
    token_type = sign_in_json['token_type']

    print(f'SIGN_IN:\nstatus: {sign_in_status}\njson: {sign_in_json}\n')


    """ *********************** POST *********************** """
    data = {
        "title": "FastAPI Book Launch", 
        "image": "https://linktomyimage.com/image.png",
        "description": "We will be discussing the contents of theFastAPI book in this event.Ensure to come with your own copy to win gifts!",
        "tags": [
        "python",
        "fastapi",
        "book",
        "launch"
        ],
        "location": "Google Meet",
    }

    post_responce = client.post(token, token_type, data)
    post_responce_status =post_responce['status']
    post_responcejson =post_responce['json']


    """ *********************** PUT *********************** """
    if IDs:
        put_responce = client.put(token, token_type, IDs[0], {'title': "Some new title"})
        put_status = put_responce['status']
        put_json = put_responce['json']

        print(f'PUT:\nstatus: {put_status}\njson: {put_json}\n')


    """ *********************** DELETE *********************** """
    if IDs:
        delete_responce = client.delete(token, token_type, IDs[0])
        delete_status = delete_responce['status']
        delete_json = delete_responce['json']

        print(f'DELETE:\nstatus: {delete_status}\njson: {delete_json}\n')
