def recommend(level):
    if level == "High":
        return "Immediate review & restrict credit"
    elif level == "Medium":
        return "Monitor account & send warning"
    else:
        return "Normal operations"
