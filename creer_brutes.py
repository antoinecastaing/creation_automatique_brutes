import sys
import json
from playwright.sync_api import sync_playwright




username = "username"
password = "password"
user_id = int(sys.argv[1])
nombre_essais = 40
bonus_legendaires = ['flail', 'leek', 'piopio', 'whip', 'chef', 'flashFlood', 'hypnosis', 'immortality', 'reconnaissance', 'sabotage', 'untouchable', 'bear', 'panther']
urls_deja_interceptees = set()





# Fonction principale 1
def creer_compte_et_brute():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        creer_compte(page)
        acceder_au_jeu(page)
        se_connecter(page)
        creer_brute(page)

        page.wait_for_timeout(2000)
        browser.close()

def creer_compte(page):

    print(f"\n\nCréation d'un compte.", f"({essai + 1}/{nombre_essais})")

    page.goto("https://eternaltwin.org/register/username", wait_until="networkidle")
    page.wait_for_selector('input[name="username"]')
    page.fill('input[name="username"]', f"{username}{user_id}")
    page.fill('input[name="display_name"]', f"{username}{user_id}")
    page.fill('input[name="password"]', password)
    page.fill('input[name="password2"]', password)
    page.get_by_role("button", name="Register").click()

def acceder_au_jeu(page):

        print(f"Accès au jeu.")

        games_link = page.get_by_role("link", name="Games").click()
        page.locator('a.btn[href="https://brute.eternaltwin.org/"]').click()

def se_connecter(page):

    print(f"Connexion au compte.")

    page.get_by_role("button", name="Connect").click()

def creer_brute(page):

    print(f"Création de {username.capitalize()}{user_id}.")

    page.wait_for_selector('svg[data-testid="PersonIcon"]', state="visible")
    field = page.locator("input.css-15yrxak")
    field.fill(f"{username}{user_id}")
    page.get_by_text("Validate").click()


# Fonction principale 2
def envoyer_au_camp_si_talent():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        context.on("response", recupere_informations_brute)

        page.goto(f"https://brute.eternaltwin.org/{username}{user_id}/cell", wait_until="domcontentloaded")
        page.wait_for_timeout(2_000)
        browser.close()

def recupere_informations_brute(reponse):

    # Récupère la requête contenant les informations de la brute
    url_de_la_bonne_requete = f"https://brute.eternaltwin.org/api/brute/{username}{user_id}/for-hook?"
    if reponse.url != url_de_la_bonne_requete or url_de_la_bonne_requete in urls_deja_interceptees: return
    urls_deja_interceptees.add(url_de_la_bonne_requete)

    # Récupère l'arme, la compétence ou l'animal de la brute
    bonus, = next(i for i in (reponse.json()["weapons"], reponse.json()["skills"], reponse.json()["pets"]) if i)

    print(f"Tu as obtenu: {bonus.capitalize()} {"🔥🔥🔥🔥🔥" if bonus in bonus_legendaires else "👎"}")

    if bonus in bonus_legendaires: envoyer_talent_au_camp(bonus)

def envoyer_talent_au_camp(bonus):

    with open("stockage_brutes/camp_talents.json", "r", encoding="utf-8") as f: camp_talents = json.load(f)

    camp_talents.update({f"{username}{user_id}": bonus.capitalize()})

    with open("stockage_brutes/camp_talents.json", "w", encoding="utf-8") as f: json.dump(camp_talents, f, indent=4)






for essai in range(nombre_essais):

    creer_compte_et_brute()
    envoyer_au_camp_si_talent()

    user_id += 1