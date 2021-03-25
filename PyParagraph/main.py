import os
import re

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname,'Resources', 'paragraph_1.txt')

# Open and read text file
with open(file_path) as file:
  paragraph = file.read()

  # Word Count
  words = paragraph.split(" ")
  word_count = len(words)

  # Sentence Count
  sentences = re.split("(?<=[.!?]) +", paragraph)
  sentence_count = len(sentences)

  # Average letter Count
  #   first get letter counts for each word
  letter_counts = []
  for word in words:
    letter_counts.append(len(word))
  #   then average this for this whole paragraph 
  average_letters = round((sum(letter_counts)/len(letter_counts)),2)
  
  # Average sentence count
  #   first get word counts for each sentence. Must be re-split into words first 
  word_counts = []
  for sentence in sentences:
    words_in_sentence = sentence.split(" ")
    word_counts.append(len(words_in_sentence))
  #   then average this for this whole paragraph 
  average_sentence = round((sum(word_counts)/len(word_counts)),2)

  # Print to terminal 
  print("Paragraph Analysis")
  print("-------------------")
  print(f"Approximate Word Count: {word_count}")
  print(f"Approximate Sentence Count: {sentence_count}")
  print(f"Average Letter Count: {average_letters}")
  print(f"Average Sentence Length: {average_sentence}")

  # Write to txt file
  output_file = os.path.join(dirname, "Analysis", "paragraph_analysis.txt")

  with open(output_file, "w", newline="") as writer:
    nl = "\n"
    writer.write(f"Paragraph Analysis {nl}------------------ {nl}Approximate Word Count: {word_count}{nl}") 
    writer.write(f"Approximate Sentence Count: {sentence_count} {nl}Average Letter Count: {average_letters}{nl}") 
    writer.write(f"Average Sentence Length: {average_sentence}") 