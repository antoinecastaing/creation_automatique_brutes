import sys
import json
from playwright.sync_api import sync_playwright

password = "Bonjoures123!"



def monter_niveau():

    print(f"\n{brute.capitalize()} monte de niveau ! 🔥🔥🔥")
    print(f"\nbonuses actuels: {[i for i in bonuses]}\n")

    level_up.first.click()
    page.wait_for_timeout(1000)

    validate_buttons = page.locator("p:has-text('Validate')")
    choices = page.locator("h6")

    # Affichage des améliorations
    for i in range(2): print(f"Choix {"b" if i else "a"}: {choices.nth(i).inner_text().strip()}")

    # Sélection des améliorations
    choix = int(ord(input("> ").strip() or "a") - 97)
    validate_buttons.nth(choix).click()

    if not choix and choices.nth(0).inner_text().strip() not in ["HP", 'Strength', "Agility", "Speed"]: bonuses.append(choices.nth(0).inner_text().strip())

def aller_cellule():

    print(f"\n\n\n\n\nEntraînement de {brute.capitalize()}.")

    page.goto("https://eternaltwin.org/login", wait_until="networkidle")

    print(f"\nConnexion au compte.")

    page.wait_for_selector('input[name="login"]')
    page.fill('input[name="login"]', brute)
    page.fill('input[name="password"]', password)
    page.get_by_role("button", name="Sign in").click()
    
    acceder_au_jeu(page)
    se_connecter(page)


    
    
def acceder_au_jeu(page):

    print(f"Accès au jeu.")

    games_link = page.get_by_role("link", name="Games").click()
    page.locator('a.btn[href="https://brute.eternaltwin.org/"]').click()

def se_connecter(page):

    print(f"Accès à la cellule.")

    page.get_by_role("button", name="Connect").click()


def envoyer_au_camp_exception():

    with open("stockage_brutes/camp_exception.json", "r", encoding="utf-8") as f:
        exceptions = json.load(f)
        exceptions.update({brute: bonuses})

    with open("stockage_brutes/camp_exception.json", "w", encoding="utf-8") as f:
        json.dump(exceptions, f, indent=4)

def envoyer_au_cimetiere():
    with open("stockage_brutes/cimetiere.json", "r", encoding="utf-8") as f:
        cimetiere = json.load(f)
        cimetiere.update({brute: bonuses})

    with open("stockage_brutes/cimetiere.json", "w", encoding="utf-8") as f:
        json.dump(cimetiere, f, indent=4)



def enlever_talent_du_camp():

    with open("stockage_brutes/camp_talents.json", "w", encoding="utf-8") as f:
        json.dump(talents, f, indent=4)

def combat():
    arena_link.first.click()
    page.wait_for_url(f"**/{brute}/arena**")


    images = page.locator('img[src="/images/rankings/lvl_11.webp"]')
    images.first.wait_for(state="visible")
    images.first.click()

    print(f"\nLancement du combat. {j + 1}/6")

    start_fight = page.locator('h5:has-text("Start fight")')
    start_fight.wait_for(state="visible")
    start_fight.click()

    quit_fight = page.locator(f'span:has-text("{brute}\'s cell")')
    quit_fight.wait_for(state="visible")
    quit_fight.click()

    print(f"Fin du combat.")




with open("stockage_brutes/camp_talents.json", "r", encoding="utf-8") as f:
    talents = json.load(f)
    nombre_de_talents = len(talents)


for i in range(nombre_de_talents):

    brute, bonus = talents.popitem()
    bonuses = [bonus]

    enlever_talent_du_camp()


    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        aller_cellule()


        for j in range(6):

            arena_link = page.locator(f'a[href="/{brute}/arena"]')
            level_up = page.locator('button:has-text("Level up!")')
            choice = arena_link.or_(level_up).first
            choice.wait_for(state="visible")

            # Vérifie si on passe niveau 2
            if level_up.first.is_visible(): monter_niveau()

            combat()


        # Vérifie si on passe niveau 3
        level_up = page.locator('button:has-text("Level up!")')
        try: level_up.wait_for(state="visible", timeout=1000)
        except: pass
        if level_up.count() > 0 and level_up.first.is_visible(): monter_niveau()


        page.wait_for_timeout(1000)
        page.close()
        context.close()
        browser.close()


        exception = input(f"Envoyer {brute} au cimetière ? Voici ses bonus: {bonuses}")

        if exception: envoyer_au_camp_exception()
        else: envoyer_au_cimetiere()
            
