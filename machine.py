import sys
import subprocess

if __name__ == "__main__":

    batch_count = int(sys.argv[1])
    batch_size  = int(sys.argv[2])
    start       = int(sys.argv[3])
    processes = []

    print("Lancement de la machine à brutes.")

    for k in range(batch_count):
        p = subprocess.Popen(["python3", "creer_brutes.py", str(start + k * batch_size), str(batch_size)])
        processes.append(p)

    for p in processes: p.wait()

    print(f"\n{batch_count * batch_size} brutes créées avec succès, d'id {start} à {start + batch_count * batch_size - 1}.\n")
