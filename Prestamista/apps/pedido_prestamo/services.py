import requests
from collections import OrderedDict


def borrow_money(dni, genero, email):
    """
    Metodo que me dice si se le puede prestar plata a la persona que
    corresponde con los datos ingresados.

    Ejemplo de uso:
    ---------------
        is_error, is_approved = borrow_money(30156149, "M", "fran@mail.com")
        print("error: {}".format(is_error))
        print("approved: {}".format(is_approved))

    URL que se obtiene:
    -------------------
        http://scoringservice.moni.com.ar:7001/api/v1/scoring/?
        email=fran%40mail.com&document_number=30156149&gender=M
    """
    URL = "http://scoringservice.moni.com.ar:7001/api/v1/scoring/"

    params = OrderedDict()
    params["email"] = email
    params["document_number"] = dni
    params["gender"] = genero
    # params = {
    #     "document_number": dni,
    #     "gender": genero,
    #     "email": email
    # }
    # print(type(params))
    # print(params)

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        response_json = response.json()
        # print(response.url)
        is_error = response_json.get("error")
        is_approved = response_json.get("approved")

    return is_error, is_approved
