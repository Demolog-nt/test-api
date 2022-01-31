class TextQueries(str):
    INSERT = f"INSERT into text_from_testapi (filename, filetext) VALUES($1, $2)"
    SELECT = "select filetext from text_from_testapi where filename = $1"
