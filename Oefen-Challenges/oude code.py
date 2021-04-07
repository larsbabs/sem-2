def uni_rating():
    if lengte_calc(lengte) == "te kort":
        rating = "te kort"
    elif (lengte_calc(lengte) == "redelijk") and (others_calc(others) == "geen") and (numbers_calc(numbers) == "geen"):
        rating = "matig"
    elif (lengte_calc(lengte) == "redelijk") and (others_calc(others) == "redelijk") and (numbers_calc(numbers) == "redelijk"):
        rating = "goed"
    elif (lengte_calc(lengte) == "lang") and (others_calc(others) == "goed") and (numbers_calc(numbers) == "goed"):
        rating = "onbreekbaar"
    elif (lengte_calc(lengte) == "redelijk") and (others_calc(others) == "goed") and (numbers_calc(numbers) == "goed"):
        rating = "onbreekbaar"    
    elif (lengte_calc(lengte) == "lang") and (others_calc(others) == "redelijk") and (numbers_calc(numbers) == "redelijk"):
        rating = "zeer goed"
        elif (lengte_calc(lengte) == "lang") and (others_calc(others) == "redelijk") and (numbers_calc(numbers) == "redelijk"):
        rating = "zeer goed"
    return rating
