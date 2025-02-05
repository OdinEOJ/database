import firebase_admin
import uuid
from firebase_admin import credentials, firestore

cred = credentials.Certificate("quizMaskin\quizmaskin69-firebase-adminsdk-fbsvc-edd7ce0114.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

def mellomrom(num):
    for i in range(num):
        print("")


# velg tema

# vanskelighetsgrad (mulgiple choice, multiple choice med tid og fyll inn med tid)

# powerups

# hent ut spørsmål og svar fra databasen

# arkade stil highscore system når quiz er ferdig

# vise highscore liste


#######################################################
# måte å legge til spørsmål og svar inn i databasen på en enkel måte

def leggTilSpørmål():
    collection = str(input("hvilket tema er spørsmålet under: "))
    docID = str(uuid.uuid4())
    doc_ref = db.collection(collection).document(docID)
    doc_ref.set({
        'spørsmål': input("hva er spørsmålet: "),
        'vanskelighetsgrad': input("hvilken vanskelighetsgrad på spørsmålet: "),
        'tema': collection,
        'svarMPC': input("svar på spørsmålet multiple choice (a, b, c, d): "),
        'svar': input("svar på spørsmålet (tekst): "),
    })
    print(f"spørsmål med id-en: {docID} er lagt til")


#######################################################


# start quiz
def meny():
    print("-----------Hovedmeny----------")
    print("   1. start quiz")
    print("   0. Avslutt")
    valg = input("Velg fra menyen: ")
    print("------------------------------")
    return valg


def main():
    run = True
    while run:
        valgt = meny()
        if valgt == "1":
            main2()
        elif valgt == "0":
            run = False
        
#######################################################

def meny2():
    mellomrom(2)
    print("-----------Hovedmeny----------")
    print("   1. Legg til ny bruker")
    print("   2. Slett en bruker")
    print("   3. legge til spørsmål")
    print("   0. Avslutt")
    valg2 = input("Velg fra menyen: ")
    return valg2

def main2():
    run = True
    while run:
        valgt2 = meny2()
        if valgt2 == "3":
            leggTilSpørmål()
        elif valgt2 == "0":
            run = False
        
main()
