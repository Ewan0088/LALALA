import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json

# Download necessary NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Raw content data
raw_contents = [
    "Kitai jak salah bak mata sidak.Laban sidak enda nemu jerita kebendar ia...",
    "Anang ngayah diri nulong ?urang bukai.",
    "Bisi nyamai tiap ari makai wai",
    "Nyamai dabai wai",
    "Namahal jaku baka tuk?",
    "Nyak meh aku ndak nemu.la ya nabes ke apa.. ka keni ke ndai ninga munyi enjin",
    "Mensia baka aku ka makai nyamai aja",
    "Kala nguji. Enggai bula. Nadai ngasi wai.",
    "Aku laban enda ba tisi nuan belama.",
    "Penatai nuan baka penurun kumang ari langit",
    "Bila nuan ka pulai sarawak?",
    "Bila urang ka mayar utang aku aku nyau ka krismas wai.",
    "Lantang ati kitak wai",
    "Nyamai wai!",
    "Penatai aku ngasuh pengidup nuan kacau.",
    "Penatai nuan kelalu manah.",
    "Nadai ngawa! Terima kasih laban nulong sarawak.",
    "Ambai..Ukai nasib makai rian tua labuh di kubuk..Ukai nasib makai entekai tua labuh dilanggu..Ngarap tahun tu bebungai timun buah rampu..Bisi ke ayam mata ajar bejaku..",
    "Asai jaik laban enda ulih nulong.",
    "Anang kelalu ka ngayah ke diri ka nulong urang bukai, laban bisi kelebih ag bedau tentu ya nemu reti ngucap terima kasih."
]

# List to store filtered tokens for all sentences
all_filtered_tokens = []

for sentence in raw_contents:
    # Lowercasing
    lowercased_data = sentence.lower()

    # Tokenization
    tokens = word_tokenize(lowercased_data)

    # Remove Stop Words
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

    # Print Results for Each Sentence
    print(filtered_tokens)

    # Append filtered tokens to the list
    all_filtered_tokens.append(filtered_tokens)

# Save preprocessed data to a JSON file (open in append mode)
with open("cleanedData.json", "a") as json_file:
    json.dump(all_filtered_tokens, json_file,)