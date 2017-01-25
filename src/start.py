class start():
  def check_string (self, string):
    string_comment = ""
    letter = "letter"
    if type (string) is not str:
      raise TypeError ("Argument should be a string")
    if len(string) == 0:
      string_comment = "Stop annoying me with empty strings"
    else:
      if len(string) > 1:
        letter = "letters"
      string_comment = "You have " + str(len(string)) + " " + letter + " in '" + string + "'"

    return (string, string_comment)
