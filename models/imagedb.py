class ImageQueries(str):
    INSERT = f"INSERT into images_from_testapi (filename, filecontent) VALUES($1, $2)"
    SELECT = "select filecontent from images_from_testapi where filename = $1"
