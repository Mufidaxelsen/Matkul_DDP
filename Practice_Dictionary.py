capitals = {
    "USA": "Washington D.C",
    "India": "New Delhi",
    "South Korea": "Seoul",
    "Japan": "Tokyo"
}


print(capitals.get("USA"))        
print(capitals.get("Indonesia"))  


capitals["USA"] = "Los Angeles"


capitals["Indonesia"] = "Jakarta"


capitals.pop("India", None)       
capitals.pop("Japan", None)       


print(capitals)
