def IDExtracter(URL):
    URL_param = URL.split("?")
    URL_param2 = URL_param[1].split("&")
    for n in URL_param2:
        if n[0:3] == 'aid':
            URL_iid = n
    id = URL_iid.split("=")[1]
    return id