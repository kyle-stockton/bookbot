def get_num_words(text):
  return len(text.split())

def get_num_characters(text):
  char_counts = {}
  for chr in text:
    key = chr.lower()
    if key not in char_counts:
      char_counts[key] = 0
    char_counts[key] += 1
  return char_counts

def sort_character_dictionary(char_counts):
  def sort_on(items):
    return items["num"]
  char_list = [{"char": k, "num": char_counts[k]} for k in char_counts]
  char_list.sort(reverse=True, key=sort_on)
  return char_list